import unittest
from unittest.mock import patch
from tools.build_story import build_story


class StoryTests(unittest.TestCase):
    def setUp(self):
        self.offset, self.descriptor = 0x101020, 0x101000
        data = bytearray(0x101040)
        data[self.offset:self.offset+8] = bytes.fromhex('00b700b800b900ba')
        data[self.descriptor:self.descriptor+8] = (8).to_bytes(4, 'big') + (32).to_bytes(4, 'big')
        self.original = bytes(data)
        self.row = {'id': 1, 'descriptor': hex(self.descriptor), 'offset': hex(self.offset),
                    'byte_length': 8, 'source_hex': '00b700b800b900ba', 'source': 'あいうえ',
                    'translation': 'Hi!'}
        self.guards = [patch('tools.build_story.records', return_value=[self.row]),
                       patch('tools.build_story.build', return_value=(self.original, b''))]
        for guard in self.guards:
            guard.start()
            self.addCleanup(guard.stop)

    def test_glyphs_padding_count_and_pointer(self):
        result, patch_bytes = build_story(self.original, [], [dict(self.row)])
        self.assertEqual(result[self.offset:self.offset+8], bytes.fromhex('0028004900010000'))
        self.assertEqual(result[self.descriptor:self.descriptor+4], (6).to_bytes(4, 'big'))
        self.assertEqual(result[self.descriptor+4:self.descriptor+8], (32).to_bytes(4, 'big'))
        self.assertEqual(result[:0x101000], self.original[:0x101000])
        self.assertEqual(patch_bytes[:4], b'BPS1')

    def test_rejects_changed_source(self):
        with self.assertRaisesRegex(ValueError, 'source metadata'):
            build_story(self.original, [], [dict(self.row, source='違う')])

    def test_rejects_over_budget(self):
        with self.assertRaisesRegex(ValueError, 'budget'):
            build_story(self.original, [], [dict(self.row, translation='Hello')])

    def test_rejects_control_bearing_record(self):
        self.row['source_hex'] = '200000b800b900ba'
        with self.assertRaisesRegex(ValueError, 'Control-bearing'):
            build_story(self.original, [], [dict(self.row)])

    def test_rejects_duplicate_record(self):
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            build_story(self.original, [], [dict(self.row), dict(self.row)])

    def test_rejects_non_ascii_narration(self):
        with self.assertRaisesRegex(ValueError, 'ASCII'):
            build_story(self.original, [], [dict(self.row, translation='été')])

    def test_layout_word_only_changes_guarded_instruction(self):
        row = {'offset': '0x101030', 'source_hex': '00000000', 'target_hex': '24070040'}
        result, _ = build_story(self.original, [], [], layout=[row])
        self.assertEqual(result[:0x101030], self.original[:0x101030])
        self.assertEqual(result[0x101030:0x101034], bytes.fromhex('24070040'))
        self.assertEqual(result[0x101034:], self.original[0x101034:])

    def test_layout_word_guards_source_alignment_size_and_checksum(self):
        row = {'offset': '0x101030', 'source_hex': '00000000', 'target_hex': '24070040'}
        for change in [{'source_hex': '11111111'}, {'offset': '0x100000'},
                       {'offset': '0x101031'}, {'target_hex': '0040'}]:
            with self.subTest(change=change), self.assertRaises(ValueError):
                build_story(self.original, [], [], layout=[dict(row, **change)])

    def test_layout_word_cannot_overlap_dialogue_or_another_layout_word(self):
        row = {'offset': self.row['offset'], 'source_hex': '00b700b8', 'target_hex': '24070040'}
        with self.assertRaisesRegex(ValueError, 'overlaps'):
            build_story(self.original, [], [dict(self.row)], layout=[row])
        row = dict(row, offset='0x101030', source_hex='00000000')
        with self.assertRaisesRegex(ValueError, 'overlaps'):
            build_story(self.original, [], [], layout=[row, row])
