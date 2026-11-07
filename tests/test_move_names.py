import struct
import unittest
from unittest.mock import patch

from tools import move_names


class MoveNameTests(unittest.TestCase):
    def setUp(self):
        constants = dict(BIAS=0, RECIPE_TABLE=0, RECIPE_COUNT=2, PART_TABLE=16,
                         PART_COUNT=2, SUFFIX_TABLE=20, SUFFIX_COUNT=2,
                         TEXT_START=28, TEXT_END=128)
        guard = patch.multiple(move_names, **constants)
        guard.start();self.addCleanup(guard.stop)
        self.rom = bytearray(128)
        struct.pack_into('>4BI4BI', self.rom, 0, 0,1,0,0,28, 1,2,2,0,40)
        self.rom[16:20] = bytes([0,0,1,1])
        struct.pack_into('>II', self.rom, 20, 52,64)
        self.rows = []
        for offset, source, target in [(28,'ひ','Fire '),(40,'ほのお','Fire Breath'),
                                       (52,'つめ','Claw'),(64,'じゅう','Gun')]:
            data=source.encode('shift_jis')+b'\0'
            self.rom[offset:offset+len(data)] = data
            self.rows.append(dict(offset=hex(offset),source=source,translation=target))

    def test_prefix_suffix_order_and_standalone_move(self):
        names, components = move_names.compositions(self.rom, self.rows)
        self.assertEqual(names, ['Fire Claw','GunFire ','Fire Breath','Fire Breath'])
        self.assertEqual(components, 4)

    def test_long_combinations_rejected_even_when_each_component_fits(self):
        self.rows[0]['translation'] = 'Thunder '
        self.rows[2]['translation'] = 'Firestorm'
        with self.assertRaisesRegex(ValueError, 'sixteen'):
            move_names.validate(self.rom, self.rows)

    def test_missing_translation_and_changed_source_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Missing'):
            move_names.validate(self.rom, self.rows[:-1])
        self.rows[0]['source'] = 'ち'
        with self.assertRaisesRegex(ValueError, 'mismatched'):
            move_names.validate(self.rom, self.rows)

    def test_pointer_metadata_and_truncation_rejected(self):
        for offset, value in [(7,0),(17,2),(0,2),(1,46)]:
            with self.subTest(offset=offset):
                rom=bytearray(self.rom);rom[offset]=value
                with self.assertRaises(ValueError):move_names.validate(rom,self.rows)
        with self.assertRaisesRegex(ValueError, 'Truncated'):
            move_names.validate(self.rom[:64],self.rows)
