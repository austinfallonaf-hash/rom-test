import hashlib
import json
import struct
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.graphics import caption_image, replacement, validate_loader, DISPATCHER


class GraphicsTests(unittest.TestCase):
    def fixture(self):
        image=bytes([0x10,0x84])*(64*32)
        header=bytearray(100);header[:8]=b'HVQ2 1.0'
        header[0x14:0x16]=b'\x02\x02';struct.pack_into('>HH',header,0x16,64,32)
        original=bytearray(b'\xff'*0x120000)
        struct.pack_into('>II',original,0x100,1,16)
        struct.pack_into('>II',original,0x108,16,100)
        original[0x120:0x184]=header
        entry={'resource_id':0x3f0,'source_blob_sha256':hashlib.sha256(header).hexdigest(),
               'image_sha256':hashlib.sha256(image).hexdigest(),'dimensions':[64,32],
               'destination':'0x110000','captions':[{'rect':[2,2,62,13],
                   'sample_x':1,'translation':'APPS'}]}
        return original,entry,image

    def test_caption_changes_only_its_guarded_rectangle(self):
        original=bytes([0x10,0x84])*(64*32)
        captions=[{'rect':[2,2,62,13],'sample_x':1,'translation':'APPS'}]
        result=caption_image(original,64,32,captions)
        self.assertEqual(len(result),len(original))
        self.assertIn(b'\xff\xfe',result)
        self.assertNotEqual(result,original)
        for y in range(32):
            for x in range(64):
                if not (2<=x<62 and 2<=y<13):
                    pos=2*(y*64+x)
                    self.assertEqual(result[pos:pos+2],original[pos:pos+2])

    def test_rejects_bad_text_dimensions_and_overlapping_captions(self):
        image=bytes(64*32*2)
        row={'rect':[2,2,62,13],'sample_x':1,'translation':'APPS'}
        for change in [{'translation':'APPS!'}, {'translation':'A'*11},
                       {'rect':[0,0,65,10]}, {'sample_x':3}]:
            with self.subTest(change=change), self.assertRaises(ValueError):
                caption_image(image,64,32,[dict(row,**change)])
        with self.assertRaisesRegex(ValueError,'Overlapping'):
            caption_image(image,64,32,[row,row])
        with self.assertRaisesRegex(ValueError,'size'):
            caption_image(b'',64,32,[row])

    def test_resource_relocation_preserves_metadata_and_uses_raw_length(self):
        original,entry,image=self.fixture()
        with patch('tools.graphics.TABLE',0x100):
            records=replacement(original,entry,image)
        self.assertEqual(records[0],(0x108,struct.pack('>II',0x110000-0x110,4196)))
        offset,payload=records[1]
        self.assertEqual(offset,0x110000)
        self.assertEqual(payload[:8],b'RAW2 1.0')
        self.assertEqual(struct.unpack_from('>I',payload,0x10)[0],4096)
        self.assertEqual(payload[0x14:100],original[0x134:0x184])
        self.assertEqual(original[0x110000:0x110004],b'\xff'*4)

    def test_rejects_changed_inputs_directory_and_occupied_tail(self):
        original,entry,image=self.fixture()
        with patch('tools.graphics.TABLE',0x100):
            for change in [{'source_blob_sha256':'bad'},{'image_sha256':'bad'},
                           {'dimensions':[32,64]},{'destination':'0x110001'},
                           {'destination':'0x120000'},{'resource_id':0x3f1}]:
                with self.subTest(change=change), self.assertRaises(ValueError):
                    replacement(original,dict(entry,**change),image)
            original[0x110000]=0
            with self.assertRaisesRegex(ValueError,'unused ROM tail'):
                replacement(original,entry,image)

    def test_loader_guard_requires_both_dispatcher_and_call_site(self):
        output=bytearray(0x57000)
        with self.assertRaisesRegex(ValueError,'dispatcher'):validate_loader(output)
        output[0x103c:0x1060]=DISPATCHER
        with self.assertRaisesRegex(ValueError,'dispatcher'):validate_loader(output)
        output[0x56270:0x56274]=bytes.fromhex('0c00010f')
        validate_loader(output)

    def test_shipped_mips_dispatches_without_changing_hvq_arguments_or_return(self):
        root=Path(__file__).resolve().parents[1]
        rows=json.loads((root/'translation/interface-layout.json').read_text())['entries']
        code={0x8000043c+4*i:int.from_bytes(DISPATCHER[4*i:4*i+4],'big') for i in range(9)}
        actual={int(r['offset'],0)+0x7ffff400:int(r['target_hex'],16)
                for r in rows if 0x103c<=int(r['offset'],0)<0x1060}
        self.assertEqual(actual,code)
        for magic,expected in [(b'HVQ2',0x80069028),(b'RAW2',0x8007bec0)]:
            with self.subTest(magic=magic):
                memory=bytearray(512);memory[64:68]=magic
                struct.pack_into('>I',memory,80,12)
                regs=[0]*32;regs[4:8]=[64,256,320,384];regs[31]=0x80055678
                pc,next_pc=0x8000043c,0x80000440
                for _ in range(20):
                    if pc not in code:break
                    word=code[pc];op=word>>26;rs=(word>>21)&31;rt=(word>>16)&31
                    imm=word&0xffff;signed=imm if imm<0x8000 else imm-0x10000
                    following=next_pc+4
                    if word==0:pass
                    elif op==0x25:regs[rt]=int.from_bytes(memory[regs[rs]+signed:regs[rs]+signed+2],'big')
                    elif op==0x23:regs[rt]=int.from_bytes(memory[regs[rs]+signed:regs[rs]+signed+4],'big')
                    elif op==9:regs[rt]=regs[rs]+signed
                    elif op==5:
                        if regs[rs]!=regs[rt]:following=pc+4+signed*4
                    elif op==2:following=((pc+4)&0xf0000000)|((word&0x3ffffff)<<2)
                    else:self.fail(f'Unexpected instruction {word:08x}')
                    regs[0]=0;pc,next_pc=next_pc,following
                self.assertEqual(pc,expected)
                self.assertEqual(regs[31],0x80055678)
                self.assertEqual(regs[4:8],[64,256,320,384] if magic==b'HVQ2' else [164,256,12,384])

    def test_compressed_recovered_input_is_bounded_and_matches_raw(self):
        import zlib
        original,entry,image=self.fixture()
        with patch('tools.graphics.TABLE',0x100):
            expected=replacement(original,entry,image)
            packed=dict(entry,image_encoding='zlib')
            self.assertEqual(replacement(original,packed,zlib.compress(image)),expected)
            for data in [b'bad',zlib.compress(image)+b'trailing',zlib.compress(image+b'oversized')]:
                with self.subTest(size=len(data)),self.assertRaises(ValueError):
                    replacement(original,packed,data)
