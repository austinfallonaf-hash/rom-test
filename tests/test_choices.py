import struct
import unittest
from tools.choices import replace_choice, SOURCE


class ChoiceTests(unittest.TestCase):
    def setUp(self):
        self.original = b'BEFORE' + SOURCE + b'AFTER'
        self.entry = {'offset': '0x6', 'source_hex': SOURCE.hex(), 'labels': ['Yes', 'No']}

    def test_rebalances_lengths_without_growing_block(self):
        offset, raw = replace_choice(self.original, self.entry)
        self.assertEqual(offset, 6)
        self.assertEqual(len(raw), len(SOURCE))
        self.assertEqual(struct.unpack('>7H', raw), (3, 57, 69, 83, 2, 46, 79))

    def test_rejects_source_mismatch(self):
        with self.assertRaisesRegex(ValueError, 'source block'):
            replace_choice(bytes(len(self.original)), self.entry)

    def test_rejects_unknown_layout(self):
        row = dict(self.entry, source_hex='0000')
        with self.assertRaisesRegex(ValueError, 'source block'):
            replace_choice(self.original, row)

    def test_rejects_wrong_number_of_choices(self):
        with self.assertRaisesRegex(ValueError, 'two choice'):
            replace_choice(self.original, dict(self.entry, labels=['Yes']))

    def test_rejects_changed_total_length(self):
        with self.assertRaisesRegex(ValueError, 'total byte length'):
            replace_choice(self.original, dict(self.entry, labels=['Yes', 'Nah']))

    def test_rejects_overwide_label(self):
        with self.assertRaisesRegex(ValueError, '1..3'):
            replace_choice(self.original, dict(self.entry, labels=['Yeah', 'N']))

    def test_rejects_non_ascii_label(self):
        with self.assertRaisesRegex(ValueError, 'ASCII'):
            replace_choice(self.original, dict(self.entry, labels=['はい', 'No']))
