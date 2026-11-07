import unittest

from tools.build_patch import validate_text


class GardenControlTests(unittest.TestCase):
    def test_player_name_counts_as_five_cells(self):
        validate_text({'source': r'\H000', 'translation': r'\H000 picked'})
        with self.assertRaisesRegex(ValueError, '16-cell'):
            validate_text({'source': r'\H000', 'translation': r'\H000 picked a seed'})

    def test_name_cannot_be_dropped_changed_or_moved_outside_color(self):
        source = r'\C005\H000\C000 picked'
        for target in [r'\C005\C000 picked', r'\C005\H001\C000 picked',
                       r'\H000\C005\C000 picked']:
            with self.subTest(target=target), self.assertRaisesRegex(ValueError, 'Player-name'):
                validate_text({'source': source, 'translation': target})

    def test_unobserved_name_control_remains_unsupported(self):
        with self.assertRaisesRegex(ValueError, 'source control'):
            validate_text({'source': r'\H001 text', 'translation': r'\H001 text'})
