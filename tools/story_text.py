"""Decode the verified Robopon glyph-index text resource (no ROM mutation)."""
import argparse
import hashlib
import json
import struct
from pathlib import Path
from tools.rom_text import EXPECTED_SHA256

TABLE = 0x18DF9C8
COUNT = 4115
POOL = 0x18E7A60
FONT = 0x19710D0
FONT_COUNT = 272


def records(rom):
    if hashlib.sha256(rom).hexdigest() != EXPECTED_SHA256:
        raise ValueError('Expected the exact original ROM')
    glyphs = [rom[FONT+i*2:FONT+i*2+2].decode('shift_jis') for i in range(FONT_COUNT)]
    for i in range(COUNT):
        descriptor = TABLE + i * 8
        size, relative = struct.unpack_from('>II', rom, descriptor)
        offset = POOL + relative
        if size % 2 or offset + size > 0x19560C2:
            raise ValueError(f'Invalid record {i}')
        raw = rom[offset:offset+size]
        codes = struct.unpack('>'+'H'*(size//2), raw)
        yield {'id': i, 'descriptor': hex(descriptor), 'offset': hex(offset),
               'byte_length': size, 'source_hex': raw.hex(),
               'source': ''.join(glyphs[c] if c < FONT_COUNT else f'<{c:04X}>' for c in codes),
               'translation': ''}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('rom', type=Path)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    rows = list(records(a.rom.read_bytes()))
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps({'records': rows}, ensure_ascii=False, indent=2)+'\n')
    print(f'Decoded {len(rows)} length-delimited records; unknown control words retained')


if __name__ == '__main__':
    main()
