import hashlib
import struct
import unittest
import zlib
from unittest.mock import patch

from tools.build_patch import build
from tools.build_story import build_story
from tools.n64_checksum import BOOT_CRC32, calculate6102, repair6102


def image(word=0):
    rom = bytearray(0x101000)
    rom[:4] = bytes.fromhex('80371240')
    rom[0x1000:] = struct.pack('>I', word) * (0x100000//4)
    return rom


class ChecksumTests(unittest.TestCase):
    def test_independent_chksum64_vectors(self):
        # Computed using Andreas Sterbenz's standalone chksum64, not this module.
        for word, expected in [(0, (0xF8CA4DDC, 0x303A4DDC)),
                               (0xFFFFFFFF, (0xF8C24DDC, 0xC1544DDC)),
                               (0x12345678, (0x52AA96AE, 0x9F0E4DDC))]:
            with self.subTest(word=word):
                self.assertEqual(calculate6102(image(word)), expected)

    def test_requires_complete_big_endian_image(self):
        for rom in [b'', bytes(0x1000), bytes(0x101000)]:
            with self.subTest(size=len(rom)), self.assertRaises(ValueError):
                calculate6102(rom)

    def test_header_repair_changes_only_the_eight_checksum_bytes(self):
        rom = image(0x12345678)
        with patch('tools.n64_checksum.BOOT_CRC32', zlib.crc32(rom[0x40:0x1000])):
            fixed = repair6102(rom)
        self.assertEqual(fixed[:0x10], rom[:0x10])
        self.assertEqual(fixed[0x18:], rom[0x18:])
        self.assertEqual(struct.unpack_from('>II', fixed, 0x10), (0x52AA96AE, 0x9F0E4DDC))
        self.assertEqual(rom[0x10:0x18], bytes(8))

    def test_unknown_bootcode_rejected(self):
        with self.assertRaisesRegex(ValueError, 'bootcode'):
            repair6102(image())

    def test_covered_text_requires_explicit_repair_and_is_in_bps(self):
        rom = image()
        offset = 0xC7D1C
        source = 'ふつう'
        rom[offset:offset+7] = source.encode('shift_jis')+b'\0'
        original = bytes(rom)
        entry = {'offset':hex(offset), 'source':source, 'translation':'OK'}
        with patch('tools.build_patch.EXPECTED_SHA256', hashlib.sha256(original).hexdigest()):
            with self.assertRaisesRegex(ValueError, 'checksum'):
                build(original, [entry])
            with patch('tools.n64_checksum.BOOT_CRC32', zlib.crc32(original[0x40:0x1000])), \
                    patch('tools.build_story.records', return_value=[]):
                target, bps = build_story(original, [entry], [], update_checksum=True)
        self.assertEqual(target[offset:offset+7], b'OK'+bytes(5))
        self.assertEqual(struct.unpack_from('>II', target, 0x10), calculate6102(target))
        self.assertEqual(target[:0x10], original[:0x10])
        self.assertEqual(target[0x18:0x1000], original[0x18:0x1000])
        self.assertEqual(int.from_bytes(bps[-8:-4], 'little'), zlib.crc32(target))

    def test_boot_and_header_text_edits_still_rejected_with_opt_in(self):
        for offset in [0x10, 0x40, 0xFFC]:
            rom = image();rom[offset:offset+3]=b'A\0\0'
            with patch('tools.build_patch.EXPECTED_SHA256', hashlib.sha256(rom).hexdigest()):
                with self.subTest(offset=offset), self.assertRaisesRegex(ValueError, 'bootcode'):
                    build(bytes(rom), [{'offset':hex(offset),'source':'A','translation':'B'}], update_checksum=True)
