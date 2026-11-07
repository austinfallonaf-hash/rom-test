"""Build guarded native-text, UI and choice BPS patches from the exact original."""
import argparse
import json
import struct
from pathlib import Path
from tools.bps import make_patch
from tools.build_patch import build
from tools.story_text import records
from tools.dialogue import encode as encode_dialogue
from tools.choices import replace_choice
from tools.n64_checksum import repair6102


def build_story(original, menu, story, choices=(), layout=(), *, update_checksum=False):
    baseline = {r['id']: r for r in records(original)}
    menu_rom, _ = build(original, menu, update_checksum=update_checksum)
    output = bytearray(menu_rom)
    spans = [(int(r['offset'], 0), int(r['offset'], 0)+len(r['source'].encode('shift_jis'))+1) for r in menu]
    seen = set()
    for entry in story:
        index = entry['id']
        if index in seen or index not in baseline:
            raise ValueError('Duplicate or invalid story record')
        seen.add(index)
        actual = baseline[index]
        for field in ('descriptor', 'offset', 'byte_length', 'source_hex', 'source'):
            if actual[field] != entry[field]:
                raise ValueError(f'Record {index}: changed source metadata {field}')
        offset = int(actual['offset'], 0)
        size = actual['byte_length']
        codes = struct.unpack('>'+'H'*(size//2), bytes.fromhex(actual['source_hex']))
        text = entry['translation']
        if entry.get('kind') == 'dialogue':
            encoded = encode_dialogue(codes, text, allow_layout_newlines=entry.get('allow_layout_newlines', False))
        else:
            if any(c >= 272 for c in codes):
                raise ValueError('Control-bearing story records require separate handling')
            if not text or len(text) > min(16, size//2):
                raise ValueError(f'Record {index}: exceeds original glyph budget')
            if any(not 32 <= ord(c) <= 126 for c in text):
                raise ValueError('This prototype supports printable ASCII narration only')
            encoded = b''.join((ord(c)-32).to_bytes(2, 'big') for c in text)
        output[offset:offset+size] = encoded.ljust(size, bytes([0]))
        descriptor = int(actual['descriptor'], 0)
        # Offset remains unchanged. Count is in bytes and controls centering.
        output[descriptor:descriptor+4] = struct.pack('>I', len(encoded))
        spans.extend([(offset, offset+size), (descriptor, descriptor+4)])
    for entry in choices:
        offset, encoded = replace_choice(original, entry)
        if offset < 0x101000:
            raise ValueError('Choice patch would affect checksum-covered data')
        output[offset:offset+len(encoded)] = encoded
        spans.append((offset, offset+len(encoded)))
    for entry in layout:
        offset = int(entry['offset'], 0)
        source, target = bytes.fromhex(entry['source_hex']), bytes.fromhex(entry['target_hex'])
        if offset % 4 or len(source) != 4 or len(target) != 4:
            raise ValueError('Layout edits require one aligned instruction word')
        if (offset < 0x1000 or (offset < 0x101000 and not update_checksum)
                or original[offset:offset+4] != source):
            raise ValueError('Layout instruction source or checksum region differs')
        if any(offset < end and start < offset+4 for start, end in spans):
            raise ValueError('Layout instruction overlaps another edit')
        output[offset:offset+4] = target
        spans.append((offset, offset+4))
    if update_checksum:
        if output[:0x10] != original[:0x10] or output[0x18:0x1000] != original[0x18:0x1000]:
            raise ValueError('Unexpected header or bootcode change')
        output = bytearray(repair6102(output))
        if output[0x10:0x18] != original[0x10:0x18]:
            spans.append((0x10, 0x18))
    elif output[:0x101000] != original[:0x101000]:
        raise ValueError('Unexpected N64 checksum-region change')
    patch = make_patch(original, bytes(output), spans)
    return bytes(output), patch


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('rom', type=Path)
    p.add_argument('--menu', type=Path, default=Path('translation/save-menu.json'))
    p.add_argument('--story', type=Path, default=Path('translation/intro.json'))
    p.add_argument('--choices', type=Path, help='Optional guarded native Yes/No blocks')
    p.add_argument('--layout', type=Path, help='Optional guarded layout instruction words')
    p.add_argument('--update-checksum', action='store_true', help='Allow guarded UI edits in the CIC-6102 checksum region and repair CRC1/CRC2')
    p.add_argument('--output', type=Path, default=Path('local/intro-alpha.z64'))
    p.add_argument('--patch', type=Path, default=Path('local/intro-alpha.bps'))
    a = p.parse_args()
    if len({a.rom.resolve(), a.output.resolve(), a.patch.resolve()}) != 3:
        p.error('Input and output paths must be distinct')
    original = a.rom.read_bytes()
    result, patch = build_story(original, json.loads(a.menu.read_text())['entries'],
                                json.loads(a.story.read_text())['records'],
                                json.loads(a.choices.read_text())['entries'] if a.choices else [],
                                json.loads(a.layout.read_text())['entries'] if a.layout else [],
                                update_checksum=a.update_checksum)
    for path, content in [(a.output, result), (a.patch, patch)]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    print(f'Wrote {a.output} and {a.patch}; original unchanged')


if __name__ == '__main__':
    main()
