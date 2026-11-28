"""Required, guarded readers for ship facility captions and Bot Book UI."""

FACILITY_CAPTIONS = (0xFB78E, 0xFB7BE, 0xFB7EE, 0xFB81E, 0xFB84E, 0xFB87E, 0xFB8AE, 0xFB8DE)

HEIGHT_WEIGHT = (0x1085DC, 0x1086D0, 0x108C78, 0x108D54, 0x109058, 0x109134)

# Keep the existing ten-word caption position block. For a leading Shift-JIS
# byte retain strlen//2; for ASCII use strlen. Both paths subtract cells*6.
FACILITY_START = 0xE081C
FACILITY_SOURCE = bytes.fromhex('00401821000310420040202100041840006218210003104000401821240400a000831023a7c20034')
FACILITY_TARGET = bytes.fromhex('8fc3003090630000000319c200621006000218400062182100031840240400a000831023a7c20034')

# The title renderer uses bytes*3. Double the byte count for an ASCII heading
# before that multiplication; retain its exact Japanese path and sign extension.
# strlen uses only a0/v0/v1, so its delay slot can preserve the first byte in t0.
TITLE_WORDS = {
    0x10CE3C: ('2462000c', '2464000c'),
    0x10CE44: ('00402021', '90880000'),
    0x10CE48: ('00402021', '2d040080'),
    0x10CE4C: ('00041840', '00821004'),
    0x10CE50: ('00621821', '00021840'),
    0x10CE54: ('00601021', '00621021'),
}


def required_words():
    words = {p: ('3c013f80', '3c013f40') for p in HEIGHT_WEIGHT}
    for i in range(0, len(FACILITY_SOURCE), 4):
        source, target = FACILITY_SOURCE[i:i+4], FACILITY_TARGET[i:i+4]
        if source != target:
            words[FACILITY_START+i] = (source.hex(), target.hex())
    words.update(TITLE_WORDS)
    return words


def require_layout(menu, layout):
    menu = {int(e['offset'], 0): e for e in menu}
    needed = set()
    if any(offset in menu for offset in FACILITY_CAPTIONS):
        needed.update(p for p in required_words() if FACILITY_START <= p < FACILITY_START+40)
    if 0x10D9F8 in menu:
        needed.update(TITLE_WORDS)
    if 0x10DA7C in menu:
        needed.update(HEIGHT_WEIGHT[::2])
    if 0x10DA8C in menu:
        needed.update(HEIGHT_WEIGHT[1::2])
    actual = {int(e['offset'], 0): (e['source_hex'], e['target_hex']) for e in layout}
    if any(actual.get(p) != required_words()[p] for p in needed):
        raise ValueError('Translated UI requires its exact caption centering and measurement layout')
