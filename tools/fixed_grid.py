"""Encode only the verified fixed-size native minigame text grids."""
import struct

# The native readers copy seven 20-byte rows (ROM 0x122428–0x122480),
# three 42-byte rows (0x1725C0–0x172620), or three 30-byte rows
# (0x1726E4–0x17273C). Keep full record sizes: these are not dialogue strings.
GRIDS = {**{i: (10, 7) for i in range(3323, 3328)},
         **{i: (21, 3) for i in range(3328, 3338, 2)},
         **{i: (15, 3) for i in range(3329, 3338, 2)}}


def encode(record_id, source_codes, text):
    if type(record_id) is not int or record_id not in GRIDS:
        raise ValueError('Unverified fixed-grid record')
    columns, rows = GRIDS[record_id]
    if len(source_codes) != columns*rows or any(c >= 272 for c in source_codes):
        raise ValueError('Fixed-grid source dimensions or controls differ')
    if not isinstance(text, str):
        raise ValueError('Fixed-grid translation requires ASCII rows')
    lines = text.split('\n')
    if len(lines) != rows or any(len(line) > columns for line in lines):
        raise ValueError('Fixed-grid row count or width differs')
    if any(not 32 <= ord(c) <= 126 for line in lines for c in line):
        raise ValueError('Fixed-grid translation requires printable ASCII')
    padded = ''.join(line.ljust(columns) for line in lines)
    return struct.pack('>'+'H'*len(padded), *(ord(c)-32 for c in padded))
