"""Validate translated battle names against the original app/part composition tables."""
import argparse
import hashlib
import json
import struct
from pathlib import Path

from tools.rom_text import EXPECTED_SHA256

BIAS = 0x8001FDA0
RECIPE_TABLE, RECIPE_COUNT = 0xC6820, 196
PART_TABLE, PART_COUNT = 0xC6E40, 128
SUFFIX_TABLE, SUFFIX_COUNT = 0xC6F40, 48
TEXT_START, TEXT_END = 0xC7FA0, 0xC899C
EQUIP_BIAS = 0x7FEAE060
EQUIP_RECIPE_TABLE, EQUIP_PART_TABLE, EQUIP_SUFFIX_TABLE = 0x21D298, 0x21D8B8, 0x21D9B8
EQUIP_TEXT_START, EQUIP_TEXT_END = 0x21DAB0, 0x21E4AC


def compositions(rom, entries, *, equipment=False):
    bias = EQUIP_BIAS if equipment else BIAS
    recipe_table = EQUIP_RECIPE_TABLE if equipment else RECIPE_TABLE
    part_table = EQUIP_PART_TABLE if equipment else PART_TABLE
    suffix_table = EQUIP_SUFFIX_TABLE if equipment else SUFFIX_TABLE
    text_start = EQUIP_TEXT_START if equipment else TEXT_START
    text_end = EQUIP_TEXT_END if equipment else TEXT_END
    translated = {int(e['offset'], 0): e for e in entries}
    used = set()

    def text(pointer):
        offset = pointer-bias
        if not text_start <= offset < text_end:
            raise ValueError('Move-name pointer outside verified text pool')
        end = rom.find(b'\0', offset, text_end)
        if end < 0:
            raise ValueError('Unterminated move name')
        source = rom[offset:end].decode('shift_jis')
        row = translated.get(offset)
        if row is None or row['source'] != source:
            raise ValueError(f'Missing or mismatched move translation at {offset:#x}')
        result = row['translation']
        if not result or any(not 32 <= ord(c) <= 126 for c in result):
            raise ValueError('Move components must use printable ASCII')
        used.add(offset)
        return result

    if len(rom) < max(recipe_table+8*RECIPE_COUNT, part_table+2*PART_COUNT,
                      suffix_table+4*SUFFIX_COUNT, text_end):
        raise ValueError('Truncated move-name tables')
    suffixes = [text(struct.unpack_from('>I', rom, suffix_table+4*i)[0])
                for i in range(SUFFIX_COUNT)]
    parts = [struct.unpack_from('>BB', rom, part_table+2*i) for i in range(PART_COUNT)]
    if any(order not in (0, 1) or index >= SUFFIX_COUNT for order, index in parts):
        raise ValueError('Invalid part-name order or suffix index')
    names = []
    for i in range(RECIPE_COUNT):
        standalone, a, b, c, pointer = struct.unpack_from('>4BI', rom, recipe_table+8*i)
        if standalone not in (0, 1) or not 1 <= a <= 45 or max(b, c) > 45:
            raise ValueError('Invalid app recipe metadata')
        first = text(pointer)
        for order, suffix in parts:
            last = suffixes[suffix]
            result = first if standalone else last+first if order else first+last
            if len(result) > 16:
                raise ValueError(f'Move {i} exceeds sixteen display cells: {result!r}')
            names.append(result)
    return names, len(used)


def validate(rom, entries, *, include_equipment=False):
    names, components = compositions(rom, entries)
    extra = {}
    if include_equipment:
        equip_names, equip_components = compositions(rom, entries, equipment=True)
        if equip_names != names:
            raise ValueError('Equipment and battle move names differ')
        extra = {'equipment_components': equip_components, 'equipment_combinations_checked': len(equip_names)}
    return {'recipes': RECIPE_COUNT, 'part_types': PART_COUNT,
            'components': components, 'combinations_checked': len(names),
            'maximum_cells': max(map(len, names), default=0), **extra}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('rom', type=Path)
    parser.add_argument('--equipment', action='store_true', help='Also validate the independent equipment-screen table and require matching names')
    parser.add_argument('--catalog', required=True, type=Path)
    args = parser.parse_args()
    try:
        rom = args.rom.read_bytes()
        if hashlib.sha256(rom).hexdigest() != EXPECTED_SHA256:
            raise ValueError('Expected the exact Japanese original')
        result = validate(rom, json.loads(args.catalog.read_text())['entries'], include_equipment=args.equipment)
    except (OSError, ValueError, KeyError, struct.error) as error:
        parser.exit(1, f'Move-name validation failed: {error}\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
