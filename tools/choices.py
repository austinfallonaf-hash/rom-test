"""Guarded replacement of the cabin event's two length-prefixed choice labels."""
import struct

SOURCE = bytes.fromhex('000200d000b8000300b800b800ba')  # 2:はい, 3:いいえ


def replace_choice(original, entry):
    offset = int(entry['offset'], 0)
    raw = bytes.fromhex(entry['source_hex'])
    if raw != SOURCE or original[offset:offset+len(raw)] != raw:
        raise ValueError('Choice source block does not match the known Yes/No layout')
    if len(entry['labels']) != 2:
        raise ValueError('Expected two choice labels')
    result = []
    for text in entry['labels']:
        if not 1 <= len(text) <= 3 or any(not 32 <= ord(c) <= 126 for c in text):
            raise ValueError('Choice labels require 1..3 printable ASCII glyphs')
        result.extend([len(text), *(ord(c)-32 for c in text)])
    encoded = struct.pack('>'+'H'*len(result), *result)
    if len(encoded) != len(raw):
        raise ValueError('Choice block must retain its exact total byte length')
    return offset, encoded
