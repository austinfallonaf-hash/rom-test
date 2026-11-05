import json
import unittest
from pathlib import Path
from tools.build_patch import validate_text


class ShipUiTests(unittest.TestCase):
    def test_colors_and_printf_have_display_widths(self):
        slash = chr(92)
        entry = {'source': slash+'C004%s'+slash+'C000をすてますか？',
                 'translation': slash+'C004%s'+slash+'C000'+slash+'NDrop it?',
                 'format_cells': [16]}
        validate_text(entry)
        with self.assertRaisesRegex(ValueError, '16-cell'):
            validate_text(dict(entry, format_cells=[17]))

    def test_color_argument_cannot_change(self):
        slash = chr(92)
        with self.assertRaisesRegex(ValueError, 'Color controls'):
            validate_text({'source': slash+'C004abc'+slash+'C000',
                           'translation': slash+'C003abc'+slash+'C000'})

    def test_unknown_source_escape_cannot_be_dropped(self):
        with self.assertRaisesRegex(ValueError, 'source control'):
            validate_text({'source': chr(92)+'Qabc', 'translation': 'abc'})

    def test_shop_pages_have_separate_width_and_line_limits(self):
        slash = chr(92)
        entry = {'source': 'abc'+slash+'Ldef',
                 'translation': 'Welcome!'+slash+'NSeed Shop'+slash+'LCan I help?',
                 'max_lines': 3}
        validate_text(entry)
        with self.assertRaisesRegex(ValueError, '16-cell'):
            validate_text(dict(entry, translation='Welcome!'+slash+'L'+'x'*17))
        with self.assertRaisesRegex(ValueError, '3 lines'):
            validate_text(dict(entry, translation=('x'+slash+'N')*3+'x'+slash+'LNext'))

    def test_shop_page_controls_cannot_be_added_or_removed(self):
        slash = chr(92)
        for source, target in [('a'+slash+'Lb', 'ab'), ('ab', 'a'+slash+'Lb')]:
            with self.subTest(source=source), self.assertRaisesRegex(ValueError, 'Page controls'):
                validate_text({'source': source, 'translation': target})

    def test_shop_page_cannot_move_outside_color_span(self):
        slash = chr(92)
        with self.assertRaisesRegex(ValueError, 'color context'):
            validate_text({'source': slash+'C004a'+slash+'Lb'+slash+'C000',
                           'translation': slash+'C004ab'+slash+'C000'+slash+'LNext'})

    def test_composed_shop_prices_fit_full_item_name_and_six_digits(self):
        root = Path(__file__).resolve().parents[1]
        rows = json.loads((root/'translation/shop-menu.json').read_text())['entries']
        by_offset = {int(row['offset'], 0): row for row in rows}
        for prefix, suffix in [(0x121da8, 0x121dbc), (0x121f50, 0x121f60)]:
            with self.subTest(prefix=hex(prefix)):
                before, after = by_offset[prefix], by_offset[suffix]
                validate_text({'source': '%s'+before['source']+'%d'+after['source'],
                               'translation': '%s'+before['translation']+'%d'+after['translation'],
                               'format_cells': [16, 6], 'max_lines': 3})

    def test_printf_minimum_width_cannot_be_underreserved(self):
        with self.assertRaisesRegex(ValueError, '4-cell'):
            validate_text({'source': '%6d', 'translation': '%6d',
                           'format_cells': [1], 'max_cells': 4})

    def test_unsupported_printf_cannot_be_dropped(self):
        with self.assertRaisesRegex(ValueError, 'printf'):
            validate_text({'source': '%u', 'translation': 'Number'})

    def test_reservation_count_must_match_arguments(self):
        with self.assertRaisesRegex(ValueError, 'reservations'):
            validate_text({'source': '%d %s', 'translation': '%d %s', 'format_cells': [3]})

    def test_catalog_respects_budgets_and_reserved_cells(self):
        root = Path(__file__).resolve().parents[1]
        rows = json.loads((root/'translation/ship-menu.json').read_text())['entries']
        self.assertEqual(len(rows), 91)
        for row in rows:
            with self.subTest(offset=row['offset']):
                validate_text(row)
                self.assertLessEqual(len(row['translation'].encode('ascii')),
                                     len(row['source'].encode('shift_jis')))
        categories = [r for r in rows if 0x21e4ec <= int(r['offset'],0) <= 0x21e528]
        self.assertEqual(len(categories), 7)
        self.assertTrue(all(len(r['translation']) <= 4 for r in categories))

    def test_starter_names_fit_native_glyph_allocations(self):
        root = Path(__file__).resolve().parents[1]
        rows = json.loads((root/'translation/ship-text.json').read_text())['records']
        labels = [r for r in rows if r.get('kind') == 'ui_label']
        self.assertEqual({r['id'] for r in labels}, {3604, 3891, 3985})
        for row in labels:
            self.assertLessEqual(len(row['translation'])*2, row['byte_length'])
            self.assertTrue(all(32 <= ord(c) <= 126 for c in row['translation']))
