import json
import unittest
from pathlib import Path
from tools.build_patch import validate_text


class CatalogTests(unittest.TestCase):
    def test_catalog_has_valid_controls_widths_and_budgets(self):
        root = Path(__file__).resolve().parents[1]
        catalog = json.loads((root / 'translation/save-menu.json').read_text())
        self.assertEqual(len(catalog['entries']), 11)
        for row in catalog['entries']:
            with self.subTest(offset=row['offset']):
                validate_text(row)
                self.assertLessEqual(len(row['translation'].encode('ascii')),
                                     len(row['source'].encode('shift_jis')))

    def test_rejects_embedded_terminator(self):
        with self.assertRaisesRegex(ValueError, 'terminator'):
            validate_text({'source': 'abc', 'translation': 'a' + chr(0)})

    def test_rejects_doubled_newline_escape(self):
        with self.assertRaisesRegex(ValueError, 'control'):
            validate_text({'source': 'abc', 'translation': 'a' + chr(92) * 2 + 'Nb'})

    def test_rejects_unknown_control(self):
        with self.assertRaisesRegex(ValueError, 'control'):
            validate_text({'source': 'abc', 'translation': chr(92) + 'X'})

    def test_rejects_midword_autowrap(self):
        with self.assertRaisesRegex(ValueError, '16-cell'):
            validate_text({'source': 'abc', 'translation': 'Select a save file.'})

    def test_rejects_removed_format_parameter(self):
        with self.assertRaisesRegex(ValueError, 'placeholders'):
            validate_text({'source': '%s', 'translation': 'Name'})

    def test_allows_newline_and_preserved_parameter(self):
        validate_text({'source': '%s', 'translation': 'Hi' + chr(92) + 'N%s'})

    def test_small_popup_uses_its_own_limit(self):
        with self.assertRaisesRegex(ValueError, '6-cell'):
            validate_text({'source': 'abc', 'translation': 'Start Game', 'max_cells': 6})
