import struct
import unittest
from unittest.mock import patch
from tools.build_story import build_story


class NativeStorageTests(unittest.TestCase):
    def setUp(self):
        self.pool, self.start = 0x101020, 0x101020
        data = bytearray(0x101080)
        self.rows = []
        for index, offset, size in [(1, self.start, 64), (2, self.start+64, 4),
                                    (3, self.start+68, 4)]:
            descriptor = 0x101000+(index-1)*8
            raw = bytes.fromhex('00b7')*(size//2)
            data[offset:offset+size] = raw
            struct.pack_into('>II', data, descriptor, size, offset-self.pool)
            self.rows.append({'id': index, 'descriptor': hex(descriptor),
                              'offset': hex(offset), 'byte_length': size,
                              'source_hex': raw.hex(), 'source': 'あ'*(size//2),
                              'translation': 'Hi!'})
        self.original = bytes(data)
        self.donor = dict(self.rows[0])
        self.name = dict(self.rows[1], translation='Merlin', kind='label',
                         storage={'record_id': 1, 'byte_offset': 8})
        for guard in [patch('tools.build_story.records', return_value=self.rows),
                      patch('tools.build_story.build', return_value=(self.original, b'')),
                      patch('tools.build_story.POOL', self.pool)]:
            guard.start()
            self.addCleanup(guard.stop)

    def test_full_name_uses_tail_without_changing_donor_or_original_name(self):
        rom, bps = build_story(self.original, [], [self.donor, self.name])
        self.assertEqual(rom[self.start:self.start+6], bytes.fromhex('002800490001'))
        self.assertEqual(struct.unpack_from('>II', rom, 0x101000), (6, 0))
        self.assertEqual(struct.unpack_from('>II', rom, 0x101008), (12, 8))
        self.assertEqual(rom[self.start+8:self.start+20],
                         b''.join((ord(c)-32).to_bytes(2, 'big') for c in 'Merlin'))
        self.assertEqual(rom[self.start+64:self.start+68], self.original[self.start+64:self.start+68])
        self.assertEqual(len(rom), len(self.original))
        self.assertEqual(bps[:4], b'BPS1')

    def test_multiple_names_and_catalog_order_are_independent(self):
        second = dict(self.rows[2], translation='Micro', kind='label',
                      storage={'record_id': 1, 'byte_offset': 20})
        a = build_story(self.original, [], [self.donor, self.name, second])
        b = build_story(self.original, [], [second, self.name, self.donor])
        self.assertEqual(a, b)
        self.assertEqual(struct.unpack_from('>II', a[0], 0x101010), (10, 20))

    def test_rejects_live_text_odd_offsets_and_allocation_overflow(self):
        for offset in [-2, 4, 7, 54, 64]:
            name = dict(self.name, storage={'record_id': 1, 'byte_offset': offset})
            with self.subTest(offset=offset), self.assertRaisesRegex(ValueError, 'padding'):
                build_story(self.original, [], [self.donor, name])

    def test_donor_translation_growth_cannot_overwrite_a_name(self):
        with self.assertRaisesRegex(ValueError, 'padding'):
            build_story(self.original, [], [dict(self.donor, translation='Longer text'), self.name])

    def test_rejects_missing_untranslated_or_relocated_donor(self):
        with self.assertRaisesRegex(ValueError, 'donor'):
            build_story(self.original, [], [self.name])
        for donor in [2, 3, 999]:
            name = dict(self.name, storage={'record_id': donor, 'byte_offset': 8})
            with self.subTest(donor=donor), self.assertRaisesRegex(ValueError, 'donor'):
                build_story(self.original, [], [self.donor, name])

    def test_rejects_name_aliases_with_overlapping_storage(self):
        second = dict(self.rows[2], translation='Micro', kind='label',
                      storage={'record_id': 1, 'byte_offset': 10})
        with self.assertRaisesRegex(ValueError, 'overlaps'):
            build_story(self.original, [], [self.donor, self.name, second])

    def test_rejects_malformed_storage_and_noninteger_indices(self):
        for storage in [None, [], {}, {'record_id': 1, 'byte_offset': True},
                        {'record_id': '1', 'byte_offset': 8},
                        {'record_id': 1, 'byte_offset': 8, 'extra': 0}]:
            with self.subTest(storage=storage), self.assertRaisesRegex(ValueError, 'Storage'):
                build_story(self.original, [], [self.donor, dict(self.name, storage=storage)])

    def test_source_guards_ascii_and_sixteen_cell_limit_still_apply(self):
        for changes in [{'source': '違う'}, {'translation': 'x'*17}, {'translation': 'été'}]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                build_story(self.original, [], [self.donor, dict(self.name, **changes)])
        self.rows[1]['source_hex'] = '200a0001'
        with self.assertRaisesRegex(ValueError, 'Control-bearing'):
            build_story(self.original, [], [self.donor, dict(self.name, source_hex='200a0001')])
        with self.assertRaisesRegex(ValueError, 'plain native labels'):
            build_story(self.original, [], [self.donor, dict(self.name, source_hex='200a0001', kind='dialogue')])

    def test_layout_edits_cannot_overwrite_borrowed_tail(self):
        edit = {'offset': hex(self.start+8), 'source_hex': '00b700b7', 'target_hex': '00000000'}
        with self.assertRaisesRegex(ValueError, 'overlaps'):
            build_story(self.original, [], [self.donor, self.name], layout=[edit])
