import json
import struct
import unittest
from pathlib import Path
from tools.dialogue import controls, encode


class DialogueTests(unittest.TestCase):
    def setUp(self):
        self.source = [0x200A, 2] + [183]*10 + [0x2000] + [184]*10 + [0x200A, 0]
        self.target = '[200A:0002]Hi[2000]Bye[200A:0000]'

    def test_preserves_commands_and_compacts_text(self):
        raw = encode(self.source, self.target)
        codes = struct.unpack('>'+'H'*(len(raw)//2), raw)
        self.assertEqual(codes, (0x200A, 2, 40, 73, 0x2000, 34, 89, 69, 0x200A, 0))
        self.assertEqual(controls(codes), controls(self.source))

    def test_rejects_changed_portrait(self):
        with self.assertRaisesRegex(ValueError, 'changed'):
            encode(self.source, self.target.replace('0002', '0003'))

    def test_rejects_removed_page_or_newline(self):
        with self.assertRaisesRegex(ValueError, 'changed'):
            encode(self.source, self.target.replace('[2000]', ''))

    def test_rejects_unknown_source_command(self):
        with self.assertRaisesRegex(ValueError, 'Unsupported'):
            encode([0x2010], 'Hi')

    def test_rejects_truncated_source_command(self):
        with self.assertRaisesRegex(ValueError, 'Truncated'):
            encode([0x200A], 'Hi')

    def test_rejects_wrong_argument_count(self):
        with self.assertRaisesRegex(ValueError, 'argument count'):
            encode(self.source, self.target.replace('[200A:0002]', '[200A]'))

    def test_checks_dynamic_name_width(self):
        source = [183]*30 + [0x200B, 0]
        with self.assertRaisesRegex(ValueError, '16 cells'):
            encode(source, 'abcdefghijkl[200B:0000]')

    def test_rejects_malformed_token(self):
        with self.assertRaisesRegex(ValueError, 'explicit control'):
            encode(self.source, self.target.replace('[2000]', '[200Z]'))

    def test_rejects_record_growth(self):
        with self.assertRaisesRegex(ValueError, 'budget'):
            encode([183]*2, 'Hello')

    def test_rejects_four_line_page(self):
        source = [0x2000]*3 + [183]*4
        with self.assertRaisesRegex(ValueError, 'three lines'):
            encode(source, 'a[2000]b[2000]c[2000]d')

    def test_real_cabin_catalog_preserves_all_controls(self):
        root = Path(__file__).resolve().parents[1]
        rows = json.loads((root/'translation/cabin.json').read_text())['records']
        dialogue = [r for r in rows if r.get('kind') == 'dialogue']
        self.assertEqual(len(dialogue), 26)
        for row in dialogue:
            with self.subTest(record=row['id']):
                source = struct.unpack('>'+'H'*(row['byte_length']//2), bytes.fromhex(row['source_hex']))
                raw = encode(source, row['translation'])
                target = struct.unpack('>'+'H'*(len(raw)//2), raw)
                self.assertEqual(controls(source), controls(target))
                self.assertLessEqual(len(raw), row['byte_length'])

    def test_allows_empty_trailing_cursor_line(self):
        source = [183, 0x2000, 184, 0x2000, 185, 0x2000]
        encode(source, 'a[2000]b[2000]c[2000]')

    def test_opt_in_allows_additional_layout_newline(self):
        source = [0x2003, 1] + [183]*20 + [0x2003, 0]
        raw = encode(source, '[2003:0001]One[2000]two[2003:0000]', allow_layout_newlines=True)
        self.assertEqual(controls(struct.unpack('>'+'H'*(len(raw)//2), raw)),
                         [(0x2003, 1), (0x2000,), (0x2003, 0)])

    def test_extra_newline_still_rejected_by_default(self):
        with self.assertRaisesRegex(ValueError, 'changed'):
            encode([183]*20, 'one[2000]two')

    def test_layout_opt_in_cannot_change_semantic_argument(self):
        with self.assertRaisesRegex(ValueError, 'changed'):
            encode(self.source, self.target.replace('0002', '0003'), allow_layout_newlines=True)

    def test_layout_opt_in_cannot_remove_original_line_break(self):
        with self.assertRaisesRegex(ValueError, 'changed'):
            encode(self.source, self.target.replace('[2000]', ''), allow_layout_newlines=True)

    def test_dandy_catalog_layout_and_original_controls(self):
        root = Path(__file__).resolve().parents[1]
        rows = json.loads((root/'translation/dandy.json').read_text())['records']
        added = [r for r in rows if 215 <= r['id'] <= 245]
        self.assertEqual(len(added), 31)
        for row in added:
            with self.subTest(record=row['id']):
                source = struct.unpack('>'+'H'*(row['byte_length']//2), bytes.fromhex(row['source_hex']))
                raw = encode(source, row['translation'], allow_layout_newlines=row.get('allow_layout_newlines',False))
                self.assertLessEqual(len(raw), row['byte_length'])
                expected = [c for c in controls(source) if c != (0x2000,)]
                actual = [c for c in controls(struct.unpack('>'+'H'*(len(raw)//2),raw)) if c != (0x2000,)]
                self.assertEqual(expected, actual)

    def test_rejects_excess_empty_cursor_lines(self):
        with self.assertRaisesRegex(ValueError, 'three lines'):
            encode([0x2000]*4, '[2000][2000][2000][2000]')
