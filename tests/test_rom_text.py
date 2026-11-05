import unittest
from tools.rom_text import candidates, inspect


class TextTests(unittest.TestCase):
    def test_header_rejects_wrong_byte_order(self):
        with self.assertRaises(ValueError):
            inspect(bytes.fromhex('37804012') + bytes(60))

    def test_extracts_exact_bytes_offsets_and_control_codes(self):
        raw = 'ロボポン\\Nいいえ'.encode('shift_jis')
        rows = list(candidates(b'\0\0' + raw + b'\0'))
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['offset'], '0x00000002')
        self.assertEqual(bytes.fromhex(rows[0]['source_hex']), raw)
        self.assertEqual(rows[0]['source'], 'ロボポン\\Nいいえ')

    def test_unterminated_text_is_not_a_string(self):
        self.assertEqual(list(candidates('ロボポン'.encode('shift_jis'))), [])

    def test_ascii_and_binary_are_not_japanese(self):
        self.assertEqual(list(candidates(b'debug message\0\xff\xff\xff\0')), [])

    def test_scanner_is_read_only(self):
        data = bytearray('ロボポン\0'.encode('shift_jis'))
        original = bytes(data)
        list(candidates(data))
        self.assertEqual(bytes(data), original)


if __name__ == '__main__':
    unittest.main()
