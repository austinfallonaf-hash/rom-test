import hashlib
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.prepare_emulator import prepare


class EmulatorProfileTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.bundle = self.root/'bundle';self.bundle.mkdir()
        self.original = self.root/'original.z64';self.target = self.root/'target.z64'
        data = bytearray(0x101000);data[:4]=bytes.fromhex('80371240')
        self.original.write_bytes(data)
        data[0x10:0x18]=bytes.fromhex('123456789abcdef0');data[0xC7000]=1
        self.target.write_bytes(data)
        self.md5=hashlib.md5(self.original.read_bytes()).hexdigest().upper()
        self.database=f'[{self.md5}]\nGoodName=Original [!]\nCRC=00000000 00000000\nPlayers=2\nSaveType=Eeprom 16KB\nTransferpak=Yes\n\n[OTHER]\nGoodName=Other\n'
        (self.bundle/'mupen64plus.ini').write_text(self.database)
        (self.bundle/'font.ttf').write_bytes(b'font proof')
        guard=patch('tools.prepare_emulator.EXPECTED_SHA256',hashlib.sha256(self.original.read_bytes()).hexdigest())
        guard.start();self.addCleanup(guard.stop)

    def test_profile_preserves_game_identity_save_type_and_original_bundle(self):
        directory=prepare(self.target,self.original,self.bundle,self.root/'profiles')
        data=(directory/'mupen64plus.ini').read_text()
        header=data.split('[OTHER]')[0]
        self.assertIn('CRC=12345678 9ABCDEF0',header)
        self.assertIn('GoodName=Original [!]',header)
        self.assertIn('SaveType=Eeprom 16KB',header)
        self.assertIn('Transferpak=Yes',header)
        self.assertEqual((directory/'font.ttf').read_bytes(),b'font proof')
        self.assertEqual((self.bundle/'mupen64plus.ini').read_text(),self.database)

    def test_original_uses_unmodified_bundle(self):
        output=self.root/'profiles'
        self.assertEqual(prepare(self.original,self.original,self.bundle,output),self.bundle.resolve())
        self.assertFalse(output.exists())

    def test_foreign_bootcode_is_not_assigned_this_game_profile(self):
        data=bytearray(self.target.read_bytes());data[0x100]=1;self.target.write_bytes(data)
        with self.assertRaisesRegex(ValueError,'does not belong'):
            prepare(self.target,self.original,self.bundle,self.root/'profiles')

    def test_wrong_original_is_rejected(self):
        data=bytearray(self.original.read_bytes());data[0x100]=1;self.original.write_bytes(data)
        with self.assertRaisesRegex(ValueError,'exact original'):
            prepare(self.target,self.original,self.bundle,self.root/'profiles')

    def test_repeated_generation_does_not_duplicate_md5_records(self):
        path=prepare(self.target,self.original,self.bundle,self.root/'profiles')
        first=(path/'mupen64plus.ini').read_bytes()
        self.assertEqual(prepare(self.target,self.original,self.bundle,self.root/'profiles'),path)
        self.assertEqual((path/'mupen64plus.ini').read_bytes(),first)
