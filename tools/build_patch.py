#!/usr/bin/env python3
"""Build a guarded, in-place menu proof and IPS patch from the supplied ROM."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from tools.rom_text import EXPECTED_SHA256


FORMAT = re.compile(r'%[-+0-9.]*[dsxXf]')
COLOR = re.compile(re.escape(chr(92)) + r'C[0-9]{3}')


def validate_text(entry):
    source, target = entry['source'], entry['translation']
    if chr(0) in target:
        raise ValueError('Embedded terminator in translation')
    newline = chr(92) + 'N'
    if COLOR.findall(source) != COLOR.findall(target):
        raise ValueError('Color controls must be preserved in order')
    if chr(92) in COLOR.sub('', source).replace(newline, ''):
        raise ValueError('Unsupported source control sequence')
    for text in (source, target):
        if '%' in FORMAT.sub('', text).replace('%%', ''):
            raise ValueError('Unsupported printf specifier')
    plain = COLOR.sub('', target).replace(newline, '')
    if chr(92) in plain:
        raise ValueError('Unsupported or malformed control sequence')
    if FORMAT.findall(source) != FORMAT.findall(target):
        raise ValueError('Format placeholders must be preserved in order')
    widths = entry.get('format_cells')
    formats = FORMAT.findall(target)
    if widths is not None and (len(widths) != len(formats) or
                              any(type(n) is not int or not 1 <= n <= 32 for n in widths)):
        raise ValueError('Invalid format-cell reservations')
    # Reserve actual display cells, not the bytes in a printf specifier. For
    # strings, a missing explicit bound conservatively reserves a whole line.
    if widths is None:
        widths = []
        for spec in formats:
            digits = re.search(r'[1-9][0-9]*', spec)
            widths.append(16 if spec[-1] == 's' else max(6, int(digits[0]) if digits else 0))
    widths = [max(n, int(m[0]) if (m := re.search(r'[1-9][0-9]*', spec)) else 0)
              for n, spec in zip(widths, formats)]
    index = 0
    def reserve(match):
        nonlocal index
        text = 'X' * widths[index]
        index += 1
        return text
    visible = FORMAT.sub(reserve, COLOR.sub('', target))
    limit = entry.get('max_cells', 16)
    if any(len(line) > limit for line in visible.split(newline)):
        raise ValueError(f'English line exceeds the save-menu {limit}-cell limit')


def build(original, entries):
    if hashlib.sha256(original).hexdigest() != EXPECTED_SHA256:
        raise ValueError('ROM SHA-256 differs from the supplied Japanese original')
    output = bytearray(original)
    patch = bytearray(b'PATCH')
    spans = []
    for entry in entries:
        validate_text(entry)
        offset = int(entry['offset'], 0)
        source = entry['source'].encode('shift_jis') + b'\0'
        target = entry['translation'].encode('ascii') + b'\0'
        end = offset + len(source)
        if offset < 0x101000:
            raise ValueError('This prototype does not handle N64 checksum-region changes')
        if end > len(original) or original[offset:end] != source:
            raise ValueError(f'Original bytes do not match at {offset:#x}')
        if len(target) > len(source):
            raise ValueError(f'Translation exceeds byte budget at {offset:#x}')
        if any(offset < b and a < end for a, b in spans):
            raise ValueError('Overlapping entries')
        if offset >= 0x1000000 or len(source) > 65535:
            raise ValueError('Entry exceeds IPS format limits')
        spans.append((offset, end))
        target = target.ljust(len(source), b'\0')
        output[offset:end] = target
        patch.extend(offset.to_bytes(3, 'big') + len(target).to_bytes(2, 'big') + target)
    patch.extend(b'EOF')
    return bytes(output), bytes(patch)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('rom', type=Path)
    p.add_argument('--catalog', type=Path, default=Path('translation/menu-proof.json'))
    p.add_argument('--output', type=Path, default=Path('local/menu-proof.z64'))
    p.add_argument('--patch', type=Path, default=Path('local/menu-proof.ips'))
    a = p.parse_args()
    if a.rom.resolve() in (a.output.resolve(), a.patch.resolve()):
        p.error('Refusing to overwrite original ROM')
    if a.output.resolve() == a.patch.resolve():
        p.error('ROM and patch outputs must be different files')
    rom, patch = build(a.rom.read_bytes(), json.loads(a.catalog.read_text())['entries'])
    for path, content in [(a.output, rom), (a.patch, patch)]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    print(f'Wrote {a.output} and {a.patch}; original unchanged')


if __name__ == '__main__':
    main()
