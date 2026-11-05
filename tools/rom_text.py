#!/usr/bin/env python3
"""Inspect the supplied big-endian ROM; extract candidate text without modifying it."""
import argparse
import hashlib
import json
import re
from pathlib import Path

EXPECTED_SHA256 = '02cda6221c10cba0705f351227e2d6c77e071bdb4f7aa8b5cd3c7c047a2b1881'


def inspect(data):
    if len(data) < 64 or data[:4] != bytes.fromhex('80371240'):
        raise ValueError('Expected a big-endian .z64 ROM with a complete header')
    return {'size': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'matches_supplied_rom': hashlib.sha256(data).hexdigest() == EXPECTED_SHA256,
            'title': data[32:52].decode('ascii').rstrip(),
            'cartridge_id': data[59:63].decode('ascii'),
            'header_crc1': data[16:20].hex(), 'header_crc2': data[20:24].hex()}


def candidates(data):
    # Search printable ASCII and valid Shift-JIS double-byte sequences. This
    # deliberately excludes half-width kana: random binary often resembles it.
    pattern = rb'(?:[\x20-\x7e]|[\x81-\x9f\xe0-\xef][\x40-\x7e\x80-\xfc]){3,}\x00'
    for match in re.finditer(pattern, data):
        raw = match.group()[:-1]
        try:
            text = raw.decode('shift_jis')
        except UnicodeDecodeError:
            continue
        japanese = sum('\u3040' <= c <= '\u30ff' or '\u4e00' <= c <= '\u9fff' for c in text)
        if japanese < 3 or japanese / len(text) < .35:
            continue
        yield {'offset': f'0x{match.start():08X}', 'byte_length': len(raw),
               'source_hex': raw.hex(), 'source': text, 'translation': '',
               'status': 'unverified_candidate'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('rom', type=Path)
    parser.add_argument('--output', type=Path, required=True,
                        help='Local JSON output; includes extracted game text')
    args = parser.parse_args()
    data = args.rom.read_bytes()
    info = inspect(data)
    rows = list(candidates(data))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({'rom': info, 'candidates': rows}, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({**info, 'candidate_count': len(rows)}, indent=2))


if __name__ == '__main__':
    main()
