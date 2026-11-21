"""Build guarded native-text, UI and choice BPS patches from the exact original."""
import argparse
import json
import struct
from pathlib import Path
from tools.bps import make_patch
from tools.build_patch import build
from tools.story_text import POOL, records
from tools.dialogue import encode as encode_dialogue
from tools.fixed_grid import encode as encode_fixed_grid
from tools.ui_layout import require_layout as require_ui_layout
from tools.book_text import encode as encode_book_line, placement as book_placement, require_layout as require_book_layout
from tools.choices import replace_choice
from tools.n64_checksum import repair6102
from tools.move_names import validate as validate_move_names
from tools.graphics import replacement as replace_graphic, validate_loader


def build_story(original, menu, story, choices=(), layout=(), *, update_checksum=False, validate_moves=False, graphics=(), graphic_images=None):
    story = tuple(story)
    menu, layout = tuple(menu), tuple(layout)
    require_ui_layout(menu, layout)
    baseline = {r['id']: r for r in records(original)}
    menu_rom, _ = build(original, menu, update_checksum=update_checksum)
    if validate_moves:
        validate_move_names(original, menu, include_equipment=True)
    output = bytearray(menu_rom)
    spans = [(int(r['offset'], 0), int(r['offset'], 0)+len(r['source'].encode('shift_jis'))+1) for r in menu]
    seen, allocations, relocated = set(), {}, []
    if any(entry.get('kind') == 'book_line' for entry in story):
        require_book_layout(layout)
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
        has_storage = 'storage' in entry
        if 'book_storage_offset' in entry and entry.get('kind') != 'book_line':
            raise ValueError('ROM-tail book storage is only for verified bot-book lines')
        if entry.get('kind') == 'book_line':
            if has_storage:
                raise ValueError('Bot-book lines use their reserved ROM-tail placement')
            encoded = encode_book_line(index, codes, text)
            target, padded = book_placement(original, entry, encoded)
            if any(target < end and start < target+len(padded) for start, end in spans):
                raise ValueError('Bot-book storage overlaps another edit')
            output[target:target+len(padded)] = padded
            descriptor = int(actual['descriptor'], 0)
            output[descriptor:descriptor+8] = struct.pack('>II', len(encoded), target-POOL)
            spans.extend([(target, target+len(padded)), (descriptor, descriptor+8)])
            continue
        if entry.get('kind') == 'fixed_grid':
            if has_storage:
                raise ValueError('Fixed-grid records cannot use label storage')
            encoded = encode_fixed_grid(index, codes, text)
        elif entry.get('kind') == 'dialogue':
            if has_storage:
                raise ValueError('Only plain native labels may use storage')
            encoded = encode_dialogue(codes, text,
                                      allow_layout_newlines=entry.get('allow_layout_newlines', False),
                                      layout_pages_before=entry.get('layout_pages_before', ()))
        else:
            if any(c >= 272 for c in codes):
                raise ValueError('Control-bearing story records require separate handling')
            if not text or len(text) > (16 if has_storage else min(16, size//2)):
                raise ValueError(f'Record {index}: exceeds original glyph budget')
            if any(not 32 <= ord(c) <= 126 for c in text):
                raise ValueError('This prototype supports printable ASCII narration only')
            encoded = b''.join((ord(c)-32).to_bytes(2, 'big') for c in text)
        if has_storage:
            relocated.append((entry, actual, encoded))
            continue
        output[offset:offset+size] = encoded.ljust(size, bytes([0]))
        allocations[index] = (offset, len(encoded), size)
        descriptor = int(actual['descriptor'], 0)
        # Offset remains unchanged. Count is in bytes and controls centering.
        output[descriptor:descriptor+4] = struct.pack('>I', len(encoded))
        spans.extend([(offset, offset+size), (descriptor, descriptor+4)])
    # Full labels can borrow only an explicitly translated record's unused
    # trailing allocation. Its active bytes/count stay intact. Original label
    # bytes remain; only the label descriptor points to the verified pool tail.
    occupied = []
    for entry, actual, encoded in relocated:
        storage = entry['storage']
        if (not isinstance(storage, dict) or set(storage) != {'record_id', 'byte_offset'}
                or any(type(storage[k]) is not int for k in storage)):
            raise ValueError('Storage requires integer record_id and byte_offset')
        donor, relative = storage['record_id'], storage['byte_offset']
        if donor not in allocations:
            raise ValueError('Storage donor must be a translated, non-relocated record')
        start, used, size = allocations[donor]
        if relative % 2 or relative < used or relative+len(encoded) > size:
            raise ValueError('Storage must fit aligned unused donor padding')
        target, end = start+relative, start+relative+len(encoded)
        if target < POOL or end > len(output):
            raise ValueError('Storage must remain in the native text pool')
        if any(target < b and a < end for a, b in occupied):
            raise ValueError('Native label storage overlaps another label')
        occupied.append((target, end))
        output[target:end] = encoded
        descriptor = int(actual['descriptor'], 0)
        output[descriptor:descriptor+8] = struct.pack('>II', len(encoded), target-POOL)
        spans.append((descriptor, descriptor+8))
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
    if graphics:
        validate_loader(output, graphics)
        for entry in graphics:
            if graphic_images is None or entry['image_path'] not in graphic_images:
                raise ValueError('Missing recovered sprite input')
            for offset, content in replace_graphic(original, entry, graphic_images[entry['image_path']], graphics):
                end = offset+len(content)
                if any(offset < b and a < end for a,b in spans):
                    raise ValueError('Sprite replacement overlaps another edit')
                output[offset:end] = content
                spans.append((offset,end))
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
    p.add_argument('--graphics', type=Path, help='Optional guarded bitmap sprite/caption catalog')
    p.add_argument('--asset-root', type=Path, default=Path('.'), help='Root containing recovered sprite inputs')
    p.add_argument('--layout', type=Path, help='Optional guarded layout instruction words')
    p.add_argument('--validate-moves', action='store_true', help='Require complete battle move-name coverage and validate all app/part name combinations')
    p.add_argument('--update-checksum', action='store_true', help='Allow guarded UI edits in the CIC-6102 checksum region and repair CRC1/CRC2')
    p.add_argument('--output', type=Path, default=Path('local/intro-alpha.z64'))
    p.add_argument('--patch', type=Path, default=Path('local/intro-alpha.bps'))
    a = p.parse_args()
    if len({a.rom.resolve(), a.output.resolve(), a.patch.resolve()}) != 3:
        p.error('Input and output paths must be distinct')
    original = a.rom.read_bytes()
    graphics = json.loads(a.graphics.read_text())['entries'] if a.graphics else []
    images = {e['image_path']:(a.asset_root/e['image_path']).read_bytes() for e in graphics}
    result, patch = build_story(original, json.loads(a.menu.read_text())['entries'],
                                json.loads(a.story.read_text())['records'],
                                json.loads(a.choices.read_text())['entries'] if a.choices else [],
                                json.loads(a.layout.read_text())['entries'] if a.layout else [],
                                update_checksum=a.update_checksum, validate_moves=a.validate_moves, graphics=graphics, graphic_images=images)
    for path, content in [(a.output, result), (a.patch, patch)]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    print(f'Wrote {a.output} and {a.patch}; original unchanged')


if __name__ == '__main__':
    main()
