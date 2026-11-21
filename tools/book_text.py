"""The verified four-record biography reader and its remaining ROM-tail space."""
import struct

FIRST_ID, END_ID = 3694, 3878
MAX_CELLS = 36
# The existing RAW2 sprite ends at 0x1FFD3C4. Leave its final twelve bytes of
# alignment padding intact; each text allocation is independently 8-byte aligned.
TAIL_START, TAIL_END = 0x1FFD3D0, 0x2000000
SCALE_OFFSET = 0x109C04


def encode(record_id, source_codes, text):
    if type(record_id) is not int or not FIRST_ID <= record_id < END_ID:
        raise ValueError('Unverified bot-book record')
    if not 12 <= len(source_codes) <= 18 or any(not 0 <= c < 272 for c in source_codes):
        raise ValueError('Bot-book source width or controls differ')
    if (not isinstance(text, str) or not 1 <= len(text) <= MAX_CELLS
            or any(not 32 <= ord(c) <= 126 for c in text)):
        raise ValueError('Bot-book line requires 1–36 printable ASCII cells')
    return struct.pack('>'+'H'*len(text), *(ord(c)-32 for c in text))


def require_layout(layout):
    matches = [x for x in layout if int(x['offset'], 0) == SCALE_OFFSET]
    if (len(matches) != 1 or matches[0]['source_hex'] != '3c013f80'
            or matches[0]['target_hex'] != '3c013f00'):
        raise ValueError('Bot-book lines require the guarded half-width reader')


def placement(original, entry, encoded):
    offset = entry.get('book_storage_offset')
    if type(offset) is not int or offset % 8:
        raise ValueError('Bot-book storage requires an aligned integer offset')
    padded = encoded.ljust((len(encoded)+7)//8*8, b'\0')
    if not TAIL_START <= offset < offset+len(padded) <= min(TAIL_END, len(original)):
        raise ValueError('Bot-book storage exceeds the reserved ROM tail')
    if original[offset:offset+len(padded)] != b'\xff'*len(padded):
        raise ValueError('Bot-book storage is not original unused padding')
    return offset, padded
