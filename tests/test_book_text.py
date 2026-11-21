import struct
import unittest
from unittest.mock import patch
from tools import book_text
from tools.build_story import build_story


class BookTextTests(unittest.TestCase):
    def test_full_width_lines_use_native_ascii_without_control_words(self):
        line = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        for index in [3694, 3877]:
            raw = book_text.encode(index, [100]*18, line)
            self.assertEqual(len(raw), 72)
            self.assertEqual(struct.unpack('>36H', raw), tuple(ord(c)-32 for c in line))
        self.assertEqual(book_text.encode(3694, [100]*12, 'A B'), bytes.fromhex('002100000022'))

    def test_only_verified_ids_and_plain_source_widths_are_accepted(self):
        for index in [3693, 3878, True, '3694']:
            with self.subTest(index=index), self.assertRaisesRegex(ValueError, 'Unverified'):
                book_text.encode(index, [100]*15, 'Valid')
        for codes in [[100]*11, [100]*19, [100]*11+[0x2000], [100]*11+[-1]]:
            with self.subTest(codes=codes), self.assertRaisesRegex(ValueError, 'source'):
                book_text.encode(3694, codes, 'Valid')

    def test_no_newline_control_unicode_empty_or_overwide_bypass(self):
        for text in ['', 'x'*37, 'Hello\nworld', 'Hi\tthere', 'été', ['Hi']]:
            with self.subTest(text=text), self.assertRaisesRegex(ValueError, 'printable ASCII'):
                book_text.encode(3694, [100]*15, text)

    def test_tail_allocations_are_aligned_bounded_blank_and_padded_for_reader(self):
        with patch('tools.book_text.TAIL_START', 16), patch('tools.book_text.TAIL_END', 48):
            original = b'\0'*16+b'\xff'*32
            self.assertEqual(book_text.placement(original, {'book_storage_offset':16}, b'abcd'),
                             (16, b'abcd\0\0\0\0'))
            for offset in [True, '16', 17, -8, 8, 48]:
                with self.subTest(offset=offset), self.assertRaises(ValueError):
                    book_text.placement(original, {'book_storage_offset':offset}, b'abcd')
            with self.assertRaisesRegex(ValueError, 'reserved ROM tail'):
                book_text.placement(original, {'book_storage_offset':40}, b'x'*10)
            with self.assertRaisesRegex(ValueError, 'unused padding'):
                book_text.placement(original[:20]+b'a'+original[21:], {'book_storage_offset':16}, b'abcd')
            self.assertEqual(book_text.placement(original, {'book_storage_offset':40}, b'12345678')[0], 40)

    def test_half_width_reader_is_mandatory_and_unique(self):
        edit = {'offset':hex(book_text.SCALE_OFFSET), 'source_hex':'3c013f80', 'target_hex':'3c013f00'}
        book_text.require_layout([edit])
        for edits in [[], [dict(edit,target_hex='3c013f80')], [dict(edit,source_hex='00000000')], [edit,edit]]:
            with self.subTest(edits=edits), self.assertRaisesRegex(ValueError, 'half-width'):
                book_text.require_layout(edits)

    def fixture(self):
        data = bytearray(book_text.SCALE_OFFSET+4)
        data[0x101100:0x101300] = b'\xff'*512
        data[book_text.SCALE_OFFSET:book_text.SCALE_OFFSET+4] = bytes.fromhex('3c013f80')
        rows = []
        for i in range(2):
            descriptor, offset, size = 0x101000+i*8, 0x101020+i*32, 24+i*2
            raw = bytes.fromhex('0064')*(size//2)
            data[offset:offset+size] = raw
            struct.pack_into('>II', data, descriptor, size, offset-0x101020)
            rows.append({'id':3694+i, 'descriptor':hex(descriptor), 'offset':hex(offset),
                         'byte_length':size, 'source_hex':raw.hex(), 'source':'あ'*(size//2),
                         'kind':'book_line', 'translation':'A biography line much longer than JP',
                         'book_storage_offset':0x101100+i*80})
        original = bytes(data)
        for guard in [patch('tools.build_story.records', return_value=rows),
                      patch('tools.build_story.build', return_value=(original,b'')),
                      patch('tools.build_story.POOL',0x101020),
                      patch('tools.book_text.TAIL_START',0x101100),
                      patch('tools.book_text.TAIL_END',0x101300)]:
            guard.start(); self.addCleanup(guard.stop)
        layout = [{'offset':hex(book_text.SCALE_OFFSET),'source_hex':'3c013f80','target_hex':'3c013f00'}]
        return original, rows, layout

    def test_builder_repoints_lines_preserves_originals_and_keeps_rom_size(self):
        original, rows, layout = self.fixture()
        rom, bps = build_story(original, [], rows, layout=layout)
        for row in rows:
            raw = book_text.encode(row['id'],[100]*(row['byte_length']//2),row['translation'])
            offset = row['book_storage_offset']
            self.assertEqual(rom[offset:offset+len(raw)],raw)
            self.assertEqual(struct.unpack_from('>II',rom,int(row['descriptor'],0)),
                             (len(raw),offset-0x101020))
            src = int(row['offset'],0)
            self.assertEqual(rom[src:src+row['byte_length']],original[src:src+row['byte_length']])
        self.assertEqual(rom[book_text.SCALE_OFFSET:book_text.SCALE_OFFSET+4],bytes.fromhex('3c013f00'))
        self.assertEqual(len(rom),len(original)); self.assertEqual(bps[:4],b'BPS1')
        self.assertEqual(build_story(original,[],rows[::-1],layout=layout),(rom,bps))
        self.assertEqual(build_story(original,[],iter(rows),layout=layout),(rom,bps))

    def test_builder_rejects_colliding_book_allocations(self):
        original, rows, layout = self.fixture()
        rows[1]['book_storage_offset'] = rows[0]['book_storage_offset']
        with self.assertRaisesRegex(ValueError,'overlaps'):
            build_story(original,[],rows,layout=layout)

    def test_book_tail_cannot_be_a_donor_or_used_as_generic_label_storage(self):
        original, rows, layout = self.fixture()
        with self.assertRaisesRegex(ValueError,'reserved ROM-tail'):
            build_story(original,[],[dict(rows[0],storage={'record_id':3695,'byte_offset':0})],layout=layout)
        with self.assertRaisesRegex(ValueError,'only for verified'):
            build_story(original,[],[dict(rows[0],kind='label',translation='Short')],layout=layout)
        label = dict(rows[1],kind='label',translation='Merlin',storage={'record_id':3694,'byte_offset':80})
        del label['book_storage_offset']
        with self.assertRaisesRegex(ValueError,'donor'):
            build_story(original,[],[rows[0],label],layout=layout)

    def test_builder_cannot_use_book_width_without_layout_or_verified_id(self):
        original, rows, layout = self.fixture()
        with self.assertRaisesRegex(ValueError,'half-width'):
            build_story(original,[],rows)
        bad = dict(rows[0],id=100)
        with patch('tools.build_story.records',return_value=[bad]), self.assertRaisesRegex(ValueError,'Unverified'):
            build_story(original,[],[bad],layout=layout)
