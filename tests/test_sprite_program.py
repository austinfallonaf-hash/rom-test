import hashlib
import json
import struct
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.graphics import caption_image, replacement, validate_loader
from tools.sprite_program import (EXEC_HEADER, EXEC_DISPATCHER, COPY_PROGRAM,
                                  apply_runs, caption_runs, patch_code, payload,
                                  caption_palette, apply_palette)


def run_mips(code_blocks, registers, memory, hooks, stop, limit=500000):
    """Execute generated MIPS words with real branch/jump delay-slot semantics."""
    regs=list(registers);pc=0x8000043c;next_pc=pc+4
    def get(addr,n):return bytes(memory.get((addr+i)&0x1fffffff,0) for i in range(n))
    def put(addr,data):
        for i,v in enumerate(data):memory[(addr+i)&0x1fffffff]=v
    for steps in range(limit):
        if pc==stop:return regs,steps
        if pc in hooks:
            hooks[pc](regs,memory);pc=regs[31];next_pc=pc+4;continue
        word=code_blocks.get(pc)
        if word is None:word=int.from_bytes(get(pc,4),'big')
        op,rs,rt,rd,sh,fn=word>>26,(word>>21)&31,(word>>16)&31,(word>>11)&31,(word>>6)&31,word&63
        imm=word&65535;signed=imm if imm<32768 else imm-65536;v=regs[rs];t=regs[rt];following=(next_pc+4)&0xffffffff;addr=(v+signed)&0xffffffff
        if op in (35,43):assert addr%4==0, f'Unaligned word at {addr:x}'
        if op in (37,41):assert addr%2==0, f'Unaligned halfword at {addr:x}'
        if op==0:
            if fn==0:regs[rd]=t<<sh
            elif fn==2:regs[rd]=t>>sh
            elif fn==8:following=v
            elif fn==9:regs[rd]=pc+8;following=v
            elif fn==33:regs[rd]=v+t
            elif fn==35:regs[rd]=v-t
            elif fn==36:regs[rd]=v&t
            elif fn==37:regs[rd]=v|t
            else:raise AssertionError(f'Unsupported R word {word:08x}')
        elif op in (4,5):
            if (v==t)==(op==4):following=(pc+4+signed*4)&0xffffffff
        elif op==2:following=((pc+4)&0xf0000000)|((word&0x3ffffff)<<2)
        elif op==9:regs[rt]=v+signed
        elif op==12:regs[rt]=v&imm
        elif op==13:regs[rt]=v|imm
        elif op==15:regs[rt]=imm<<16
        elif op==35:regs[rt]=int.from_bytes(get(addr,4),'big')
        elif op==36:regs[rt]=int.from_bytes(get(addr,1),'big')
        elif op==37:regs[rt]=int.from_bytes(get(addr,2),'big')
        elif op==41:put(addr,(t&65535).to_bytes(2,'big'))
        elif op==43:put(addr,(t&0xffffffff).to_bytes(4,'big'))
        else:raise AssertionError(f'Unsupported word {word:08x} at {pc:x}')
        regs=[r&0xffffffff for r in regs];regs[0]=0;pc,next_pc=next_pc,following
    raise AssertionError('Sprite program did not terminate')


class SpriteProgramTests(unittest.TestCase):
    def image(self):return bytes.fromhex('1085')*(64*32)
    def rows(self):return [{'rect':[2,2,62,13],'sample_x':1,'translation':'HUNGER'}]
    def header(self):
        b=bytearray(100);b[:8]=b'HVQ2 1.0';b[20:22]=b'\2\2';struct.pack_into('>HH',b,22,64,32);return bytes(b)
    def execute(self,blob,source,target,*,copy=False):
        src,out,work,ret=0x80100000,0x80200000,0x80300000,0x80012340
        memory={src+i-0x80000000:v for i,v in enumerate(blob)}
        memory.update({out-0x80000000+i:0x55 for i in range(len(source))})
        regs=[0x77770000+i for i in range(32)];regs[0]=0;regs[4:8]=[src,out,work,0x80400000];regs[29]=0x807ff000;regs[31]=ret;original=regs[:];calls=[]
        def write(addr,b):
            for i,v in enumerate(b):memory[(addr+i)&0x1fffffff]=v
        def hvq(r,m):
            calls.append('hvq');self.assertEqual(r[5:8],original[5:8]);self.assertGreater(r[4],src+100)
            self.assertEqual(bytes(m[(r[4]+i)&0x1fffffff] for i in range(8)),b'HVQ2 1.0');write(out,source)
            # Real O32 callees may clobber all these registers.
            for n in [2,3,4,5,6,7,8,9,10,11,12,13,14,15,24,25]:r[n]=0xdddd0000+n
        def memcpy(r,m):
            calls.append('copy');self.assertEqual(r[4:7],[src+112,out,len(target)])
            write(out,bytes(m[(r[4]+i)&0x1fffffff] for i in range(r[6])))
        code={0x8000043c+4*i:int.from_bytes(EXEC_DISPATCHER[i*4:i*4+4],'big') for i in range(9)}
        result,steps=run_mips(code,regs,memory,{0x80069028:hvq,0xa007bec0:memcpy},ret)
        self.assertEqual(calls,['copy'] if copy else ['hvq'])
        self.assertEqual(bytes(memory[(out+i)&0x1fffffff] for i in range(len(target))),target)
        self.assertEqual(result[16:24],original[16:24]);self.assertEqual(result[29:32],original[29:32])
        self.assertLess(steps,500000)
        return result

    def test_native_patch_program_decodes_then_changes_only_caption_pixels(self):
        source=self.image();rows=self.rows();expected=caption_image(source,64,32,rows)
        blob=payload(self.header(),expected,64,32,rows);self.execute(blob,source,expected)
        for y in range(32):
            for x in range(64):
                if not(2<=x<62 and 2<=y<13):self.assertEqual(expected[2*(y*64+x):2*(y*64+x)+2],source[2*(y*64+x):2*(y*64+x)+2])

    def test_native_patch_program_handles_multiple_aligned_rectangles_and_colors(self):
        rows=self.rows()+[{'rect':[4,16,58,32],'sample_x':1,'translation':'HI','ink_hex':'0031','shadow_hex':'fffe','scale':2}]
        source=self.image();expected=caption_image(source,64,32,rows);self.execute(payload(self.header(),expected,64,32,rows),source,expected)

    def test_copy_program_runs_uncached_and_preserves_equipment_pixels(self):
        source=self.image();pixels=caption_image(source,64,32,self.rows());blob=payload(self.header(),pixels,64,32,self.rows(),copy=True)
        self.assertEqual(blob[:8],EXEC_HEADER);self.assertEqual(blob[100:112],COPY_PROGRAM);self.execute(blob,source,pixels,copy=True)

    def test_original_hvq_path_retains_all_arguments_and_return(self):
        regs=[0]*32;regs[4:8]=[0x80100000,0x80200000,0x80300000,0x80400000];regs[31]=0x80012340;memory={0x100000+i:v for i,v in enumerate(b'HVQ2')};before=regs[:];seen=[]
        def hvq(r,m):seen.append(r[4:8])
        code={0x8000043c+4*i:int.from_bytes(EXEC_DISPATCHER[i*4:i*4+4],'big') for i in range(9)}
        result,_=run_mips(code,regs,memory,{0x80069028:hvq},regs[31]);self.assertEqual(seen,[before[4:8]]);self.assertEqual(result[31],before[31])

    def test_run_stream_round_trip_and_rejects_malformed_data(self):
        source=self.image();expected=caption_image(source,64,32,self.rows());stream=caption_runs(expected,64,32,self.rows());self.assertEqual(apply_runs(source,64,32,stream),expected)
        bad=bytearray(stream);bad[12]=0
        for data in [stream[:3],stream[:-5],bytes(bad),stream+b'bad',b'\0'*4]:
            with self.subTest(size=len(data)),self.assertRaises(ValueError):apply_runs(source,64,32,data)
        with self.assertRaises(ValueError):caption_runs(source,64,32,[])
        with self.assertRaises(ValueError):patch_code(32768,32769,320)

    def test_native_palette_handles_scaled_text_long_runs_and_row_gradients(self):
        source=b''.join((0x1085+y*64).to_bytes(2,'big')*128 for y in range(32))
        rows=[{'rect':[2,2,126,20],'sample_x':1,'translation':'EQUIPPED','scale':2},
              {'rect':[2,22,126,32],'sample_x':1,'translation':'SPARE PARTS','ink_hex':'0031','shadow_hex':'fffe'}]
        expected=caption_image(source,128,32,rows);head=bytearray(self.header());struct.pack_into('>H',head,22,128)
        blob=payload(bytes(head),expected,128,32,rows,palette_source=source)
        self.execute(blob,source,expected)
        self.assertEqual(apply_palette(source,128,32,caption_palette(source,expected,128,32,rows)),expected)

    def test_native_palette_allows_duplicate_background_and_ink_colors(self):
        source=self.image();rows=[dict(self.rows()[0],ink_hex='1085',shadow_hex='0031')]
        expected=caption_image(source,64,32,rows)
        self.execute(payload(self.header(),expected,64,32,rows,palette_source=source),source,expected)

    def test_palette_rejects_invalid_colors_geometry_truncation_and_run_codes(self):
        source=self.image();rows=self.rows();expected=caption_image(source,64,32,rows)
        stream=caption_palette(source,expected,64,32,rows)
        self.assertEqual(apply_palette(source,64,32,stream),expected)
        for code in [0,0xc1,63]:
            bad=bytearray(stream);bad[18]=code
            with self.subTest(code=code),self.assertRaises(ValueError):apply_palette(source,64,32,bytes(bad))
        for data in [stream[:3],stream[:-5],stream+b'bad',b'\0'*4]:
            with self.subTest(size=len(data)),self.assertRaises(ValueError):apply_palette(source,64,32,data)
        bad=bytearray(stream);struct.pack_into('>I',bad,4,len(source))
        with self.assertRaises(ValueError):apply_palette(source,64,32,bytes(bad))
        outside=bytearray(expected);outside[2*(2*64+2):2*(2*64+2)+2]=b'\x12\x34'
        with self.assertRaises(ValueError):caption_palette(source,bytes(outside),64,32,rows)
        with self.assertRaises(ValueError):caption_palette(source,expected,64,32,[])
        with self.assertRaises(ValueError):caption_palette(source,expected,64,32,[dict(rows[0],sample_x=3)])

    def test_palette_fits_exact_reclaimed_capacity_that_full_color_runs_exceed(self):
        original,entry,owner=self.fixture();pixels=caption_image(self.image(),64,32,self.rows())
        compact=payload(self.header(),pixels,64,32,self.rows(),palette_source=self.image())
        self.assertLess(len(compact),len(payload(self.header(),pixels,64,32,self.rows())))
        blob=self.header()+b'\0'*(len(compact)-100)
        original[0x320:0x320+len(blob)]=blob;struct.pack_into('>I',original,0x114,len(blob))
        owner=dict(owner,source_blob_sha256=hashlib.sha256(blob).hexdigest())
        packed=dict(entry,program='hvq_palette')
        with patch('tools.graphics.TABLE',0x100):
            self.assertEqual(replacement(original,packed,self.image(),[packed,owner])[1][1],compact)
            with self.assertRaisesRegex(ValueError,'allocation'):
                replacement(original,entry,self.image(),[entry,owner])
            struct.pack_into('>I',original,0x114,len(blob)-1)
            with self.assertRaisesRegex(ValueError,'allocation'):
                replacement(original,packed,self.image(),[packed,owner])

    def fixture(self):
        original=bytearray(b'\xff'*0x120000);head=self.header();owner=head+b'\0'*(4096-100)
        struct.pack_into('>II',original,0x100,2,32);struct.pack_into('>II',original,0x108,0,100);struct.pack_into('>II',original,0x110,0x200,4096)
        original[0x120:0x184]=head;original[0x320:0x1320]=owner
        common={'image_sha256':hashlib.sha256(self.image()).hexdigest(),'dimensions':[64,32],'captions':self.rows()}
        entry=dict(common,resource_id=0x3f0,source_blob_sha256=hashlib.sha256(head).hexdigest(),program='hvq_patch',reclaim_resource_id=0x3f1,destination='0x320')
        owner_entry=dict(common,resource_id=0x3f1,source_blob_sha256=hashlib.sha256(owner).hexdigest(),program='copy',destination='0x110000')
        return original,entry,owner_entry

    def test_reclaimed_storage_requires_unique_relocated_owner_and_exact_capacity(self):
        original,entry,owner=self.fixture()
        with patch('tools.graphics.TABLE',0x100):
            edits=replacement(original,entry,self.image(),[entry,owner]);self.assertEqual(edits[1][0],0x320);self.assertLess(len(edits[1][1]),4096)
            for change in [{'reclaim_resource_id':0x3f0},{'destination':'0x324'},{'source_blob_sha256':'bad'},{'program':'unknown'}]:
                with self.subTest(change=change),self.assertRaises(ValueError):replacement(original,dict(entry,**change),self.image(),[entry,owner])
            with self.assertRaises(ValueError):replacement(original,entry,self.image(),[entry])
            with self.assertRaises(ValueError):replacement(original,entry,self.image(),[entry,dict(owner,destination='0x320')])
            struct.pack_into('>I',original,0x114,100)
            with self.assertRaises(ValueError):replacement(original,entry,self.image(),[entry,owner])

    def test_aliases_and_changed_reclaimed_source_are_rejected(self):
        original,entry,owner=self.fixture()
        with patch('tools.graphics.TABLE',0x100):
            original[0x400]^=1
            with self.assertRaises(ValueError):replacement(original,entry,self.image(),[entry,owner])
            original[0x400]^=1
            struct.pack_into('>II',original,0x100,3,32);struct.pack_into('>II',original,0x118,0x200,4096)
            with self.assertRaisesRegex(ValueError,'alias'):replacement(original,entry,self.image(),[entry,owner])

    def test_reclaimed_hvq_owner_chain_and_alias_in_unused_suffix(self):
        original,entry,owner=self.fixture()
        third_blob=self.header()+b'\0'*(8192-100)
        struct.pack_into('>II',original,0x100,3,32)
        struct.pack_into('>II',original,0x118,0x2000-0x120,8192)
        original[0x2000:0x4000]=third_blob
        middle=dict(owner,program='hvq_patch',reclaim_resource_id=0x3f2,destination='0x2000')
        third=dict(owner,resource_id=0x3f2,source_blob_sha256=hashlib.sha256(third_blob).hexdigest())
        entries=[entry,middle,third]
        with patch('tools.graphics.TABLE',0x100):
            edits=[replacement(original,e,self.image(),entries) for e in entries]
            self.assertEqual([x[1][0] for x in edits],[0x320,0x2000,0x110000])
            spans=sorted((x[1][0],x[1][0]+len(x[1][1])) for x in edits)
            self.assertTrue(all(a[1]<=b[0] for a,b in zip(spans,spans[1:])))
            with self.assertRaisesRegex(ValueError,'owner'):
                replacement(original,entry,self.image(),[entry,dict(middle,program='RAW2'),third])
            # This alias falls after the short payload, but still owns reclaimed bytes.
            self.assertLess(edits[0][1][0]+len(edits[0][1][1]),0x1200)
            original[0x180:0x1e4]=self.header()
            struct.pack_into('>I',original,0x108,0x60)
            struct.pack_into('>II',original,0x100,4,32)
            struct.pack_into('>II',original,0x120,0x1200-0x120,16)
            with self.assertRaisesRegex(ValueError,'alias'):
                replacement(original,entry,self.image(),entries)

    def test_shipped_dispatcher_and_program_loader_guard(self):
        root=Path(__file__).resolve().parents[1];rows=json.loads((root/'translation/interface-layout.json').read_text())['entries'];code=b''.join(bytes.fromhex(e['target_hex']) for e in rows if 0x103c<=int(e['offset'],0)<0x1060);self.assertEqual(code,EXEC_DISPATCHER)
        output=bytearray(0x57000);output[0x103c:0x1060]=EXEC_DISPATCHER;output[0x56270:0x56274]=bytes.fromhex('0c00010f');entries=[{'program':'copy'},{'program':'hvq_patch'},{'program':'hvq_palette'}];validate_loader(output,entries)
        with self.assertRaises(ValueError):validate_loader(output,[{'program':'copy'},{}])
        output[0x103c]^=1
        with self.assertRaises(ValueError):validate_loader(output,entries)

if __name__=='__main__':unittest.main()
