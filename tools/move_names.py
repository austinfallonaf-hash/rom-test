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


def compositions(rom, entries):
    translated = {int(e['offset'], 0): e for e in entries}
    used = set()

    def text(pointer):
        offset = pointer-BIAS
        if not TEXT_START <= offset < TEXT_END:
            raise ValueError('Move-name pointer outside verified text pool')
        end = rom.find(b'\0', offset, TEXT_END)
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

    if len(rom) < max(RECIPE_TABLE+8*RECIPE_COUNT, PART_TABLE+2*PART_COUNT,
                      SUFFIX_TABLE+4*SUFFIX_COUNT, TEXT_END):
        raise ValueError('Truncated move-name tables')
    suffixes = [text(struct.unpack_from('>I', rom, SUFFIX_TABLE+4*i)[0])
                for i in range(SUFFIX_COUNT)]
    parts = [struct.unpack_from('>BB', rom, PART_TABLE+2*i) for i in range(PART_COUNT)]
    if any(order not in (0, 1) or index >= SUFFIX_COUNT for order, index in parts):
        raise ValueError('Invalid part-name order or suffix index')
    names = []
    for i in range(RECIPE_COUNT):
        standalone, a, b, c, pointer = struct.unpack_from('>4BI', rom, RECIPE_TABLE+8*i)
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


def validate(rom, entries):
    names, components = compositions(rom, entries)
    return {'recipes': RECIPE_COUNT, 'part_types': PART_COUNT,
            'components': components, 'combinations_checked': len(names),
            'maximum_cells': max(map(len, names), default=0)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('rom', type=Path)
    parser.add_argument('--catalog', required=True, type=Path)
    args = parser.parse_args()
    try:
        rom = args.rom.read_bytes()
        if hashlib.sha256(rom).hexdigest() != EXPECTED_SHA256:
            raise ValueError('Expected the exact Japanese original')
        result = validate(rom, json.loads(args.catalog.read_text())['entries'])
    except (OSError, ValueError, KeyError, struct.error) as error:
        parser.exit(1, f'Move-name validation failed: {error}\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
