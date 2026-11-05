import hashlib
import unittest
from unittest.mock import patch
from tools.build_patch import build


class PatchTests(unittest.TestCase):
    def setUp(self):
        self.offset = 0x101020
        self.source = 'いいえ'
        self.rom = bytes(self.offset) + self.source.encode('shift_jis') + b'\0TAIL'
        self.entry = {'offset': hex(self.offset), 'source': self.source, 'translation': 'No'}
        self.guard = patch('tools.build_patch.EXPECTED_SHA256', hashlib.sha256(self.rom).hexdigest())
        self.guard.start()
        self.addCleanup(self.guard.stop)

    def test_patch_changes_only_budget_and_roundtrips_ips(self):
        result, ips = build(self.rom, [self.entry])
        self.assertEqual(len(result), len(self.rom))
        self.assertEqual(result[:self.offset], self.rom[:self.offset])
        self.assertEqual(result[self.offset:], b'No\0\0\0\0\0TAIL')
        replay = bytearray(self.rom)
        i = 5
        while ips[i:i+3] != b'EOF':
            offset = int.from_bytes(ips[i:i+3], 'big')
            size = int.from_bytes(ips[i+3:i+5], 'big')
            replay[offset:offset+size] = ips[i+5:i+5+size]
            i += 5 + size
        self.assertEqual(bytes(replay), result)

    def test_rejects_wrong_rom(self):
        with self.assertRaises(ValueError):
            build(self.rom + b'X', [self.entry])

    def test_rejects_wrong_source(self):
        with self.assertRaises(ValueError):
            build(self.rom, [dict(self.entry, source='はい')])

    def test_rejects_long_translation(self):
        with self.assertRaises(ValueError):
            build(self.rom, [dict(self.entry, translation='Too long for this slot')])

    def test_rejects_overlaps(self):
        with self.assertRaises(ValueError):
            build(self.rom, [self.entry, self.entry])
