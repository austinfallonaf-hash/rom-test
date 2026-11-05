import struct
import unittest
import zlib
from tools.bps import make_patch, number


class BpsTests(unittest.TestCase):
    def test_known_integer_encodings(self):
        for value, expected in [(0, '80'), (127, 'ff'), (128, '0080'), (255, '7f80'), (256, '0081')]:
            self.assertEqual(number(value), bytes.fromhex(expected))

    def test_footer_checksums(self):
        source, target = b'012345', b'01AB45'
        patch = make_patch(source, target, [(2, 4)])
        a, b, c = struct.unpack('<III', patch[-12:])
        self.assertEqual(a, zlib.crc32(source))
        self.assertEqual(b, zlib.crc32(target))
        self.assertEqual(c, zlib.crc32(patch[:-4]))

    def test_exact_small_patch_commands(self):
        patch = make_patch(b'012345', b'01AB45', [(2, 4)])
        # Header, 2-byte SourceRead, 2-byte TargetRead, 2-byte SourceRead.
        self.assertEqual(patch[:-12], b'BPS1\x86\x86\x80\x84\x85AB\x84')

    def test_rejects_overlapping_ranges(self):
        with self.assertRaises(ValueError):
            make_patch(b'abc', b'XYZ', [(0, 2), (1, 3)])

    def test_rejects_unrecorded_changes(self):
        with self.assertRaises(ValueError):
            make_patch(b'abc', b'XYZ', [(0, 1)])

    def test_rejects_different_sizes(self):
        with self.assertRaises(ValueError):
            make_patch(b'a', b'ab', [])

    def test_supports_offset_above_ips_limit(self):
        source = bytes(0x1000002)
        target = source[:-1] + b'X'
        patch = make_patch(source, target, [(len(source)-1, len(source))])
        self.assertLess(len(patch), 64)
        self.assertIn(b'X', patch[:-12])
