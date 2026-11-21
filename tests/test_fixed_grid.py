import struct
import unittest
from unittest.mock import patch
from tools.fixed_grid import GRIDS, encode
from tools.build_story import build_story


class FixedGridTests(unittest.TestCase):
    def test_all_verified_shapes_preserve_row_offsets_and_exact_size(self):
        self.assertEqual(len(GRIDS), 15)
        for index, (width, rows) in GRIDS.items():
            with self.subTest(index=index):
                text = '\n'.join(chr(65+i)*width for i in range(rows))
                b = encode(index, [100]*(width*rows), text)
                self.assertEqual(len(b), width*rows*2)
                for i in range(rows):
                    self.assertEqual(b[2*width*i:2*width*(i+1)],
                                     struct.pack('>H', 33+i)*width)

    def test_short_rows_are_blank_padded_without_shift_or_newline_controls(self):
        b = encode(3331, [100]*45, 'Jump\nUnused\nMove left/right')
        self.assertEqual(b[8:30], bytes(22))
        self.assertEqual(b[30:42], b''.join(struct.pack('>H', ord(c)-32) for c in 'Unused'))
        self.assertEqual(b[60:], b''.join(struct.pack('>H', ord(c)-32) for c in 'Move left/right'))

    def test_unknown_ids_and_dimensions_cannot_bypass_label_limits(self):
        for index in [3322, 3338, 1, True, '3323']:
            with self.subTest(index=index), self.assertRaisesRegex(ValueError, 'Unverified'):
                encode(index, [100]*70, '\n'.join(['Tap A']*7))
        for source in ([100]*69, [100]*71, [100]*69+[0x2000]):
            with self.assertRaisesRegex(ValueError, 'source'):
                encode(3323, source, '\n'.join(['Tap A']*7))

    def test_missing_extra_or_overwide_rows_fail(self):
        for text in ['One\nTwo', 'One\nTwo\nThree\nFour', 'x'*22+'\nTwo\nThree']:
            with self.subTest(text=text), self.assertRaisesRegex(ValueError, 'row'):
                encode(3328, [100]*63, text)

    def test_non_ascii_controls_and_non_string_rows_fail(self):
        for text in ['été\nTwo\nThree', 'One\t\nTwo\nThree', 'One\r\nTwo\nThree', ['One','Two','Three']]:
            with self.subTest(text=text), self.assertRaisesRegex(ValueError, 'ASCII'):
                encode(3328, [100]*63, text)

    def test_builder_keeps_full_descriptor_and_pointer(self):
        offset, descriptor = 0x101020, 0x101000
        raw = bytes.fromhex('00b7')*63
        data = bytearray(offset+len(raw))
        data[offset:] = raw
        struct.pack_into('>II', data, descriptor, len(raw), 32)
        original = bytes(data)
        row = {'id':3328,'descriptor':hex(descriptor),'offset':hex(offset),
               'byte_length':len(raw),'source_hex':raw.hex(),'source':'あ'*63,
               'kind':'fixed_grid','translation':'Tap A\nKeep power high\nToo fast tires you'}
        with patch('tools.build_story.records', return_value=[row]), \
             patch('tools.build_story.build', return_value=(original,b'')):
            rom, bps = build_story(original, [], [row])
            self.assertEqual(rom[descriptor:descriptor+8], original[descriptor:descriptor+8])
            self.assertEqual(rom[offset:], encode(3328,[183]*63,row['translation']))
            self.assertEqual(rom[:descriptor], original[:descriptor])
            self.assertEqual(bps[:4], b'BPS1')
            with self.assertRaisesRegex(ValueError, 'cannot use label storage'):
                build_story(original, [], [dict(row,storage={'record_id':1,'byte_offset':0})])
            with self.assertRaisesRegex(ValueError, 'source metadata'):
                build_story(original, [], [dict(row,source='changed')])
