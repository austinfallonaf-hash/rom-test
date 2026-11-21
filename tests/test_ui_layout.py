import struct
import unittest
from tools.ui_layout import (FACILITY_SOURCE, FACILITY_START, FACILITY_TARGET,
                             HEIGHT_WEIGHT, TITLE_WORDS, require_layout, required_words)
from tools.build_story import build_story


def execute(code, start, regs, memory, calls=None):
    """Execute the straight-line MIPS integer words used by the two readers."""
    regs = dict(regs)
    calls = calls or {}
    for off in range(0, len(code), 4):
        ins = int.from_bytes(code[off:off+4], 'big')
        op, rs, rt, rd, shift, fn = ins >> 26, (ins >> 21) & 31, (ins >> 16) & 31, (ins >> 11) & 31, (ins >> 6) & 31, ins & 63
        imm = ins & 65535
        signed = imm if imm < 32768 else imm-65536
        v, t = regs.get(rs, 0), regs.get(rt, 0)
        addr = (v+signed) & 0xffffffff
        if op == 0:
            if fn == 0: regs[rd] = t << shift
            elif fn == 2: regs[rd] = t >> shift
            elif fn == 3: regs[rd] = (t if t < 0x80000000 else t-0x100000000) >> shift
            elif fn == 4: regs[rd] = t << (v & 31)
            elif fn == 6: regs[rd] = t >> (v & 31)
            elif fn == 33: regs[rd] = v+t
            elif fn == 35: regs[rd] = v-t
            else: raise AssertionError(hex(ins))
        elif op == 9: regs[rt] = v+signed
        elif op == 11: regs[rt] = int(v < (signed & 0xffffffff))
        elif op == 35: regs[rt] = int.from_bytes(bytes(memory.get(addr+i, 0) for i in range(4)), 'big')
        elif op == 36: regs[rt] = memory.get(addr, 0)
        elif op == 41:
            for i, value in enumerate((t & 65535).to_bytes(2, 'big')): memory[addr+i] = value
        else: raise AssertionError(hex(ins))
        regs = {r: val & 0xffffffff for r, val in regs.items()}; regs[0] = 0
        if start+off in calls: calls[start+off](regs, memory)
    return regs


class BookUiLayoutTests(unittest.TestCase):
    def caption(self, raw, target):
        fp, pointer = 0x2000, 0x3000
        memory = {pointer+i: b for i, b in enumerate(raw+b'\0')}
        for i,b in enumerate(pointer.to_bytes(4,'big')): memory[fp+0x30+i]=b
        regs=execute(FACILITY_TARGET if target else FACILITY_SOURCE,FACILITY_START,{2:len(raw),30:fp,29:0x1800,31:0x1234},memory)
        self.assertEqual(regs[29],0x1800);self.assertEqual(regs[30],fp);self.assertEqual(regs[31],0x1234)
        self.assertEqual(regs[2]&65535,int.from_bytes(bytes(memory[fp+0x34+i] for i in range(2)),'big'))
        return regs[2]

    def title(self, raw, target):
        # Include strlen's real delay slot and model its verified v0/v1-only
        # implementation before the straight-line width/centering block.
        source=bytes.fromhex('2462000c0c01bf080040202100402021000418400062182100601021240300a00062102300021c0000031403')
        code=bytearray(source)
        if target:
            for p,(_,hexword) in TITLE_WORDS.items():code[p-0x10ce3c:p-0x10ce3c+4]=bytes.fromhex(hexword)
        fp,ctx=0x2000,0x3000;memory={ctx+12+i:b for i,b in enumerate(raw+b'\0')}
        # Execute around jal: the delay slot executes before strlen. strlen
        # leaves a0 and t0 untouched and returns the length in v0.
        regs=execute(code[:4],0x10ce3c,{3:ctx,30:fp,29:0x1800,31:0x1234},memory)
        regs=execute(code[8:12],0x10ce44,regs,memory)
        self.assertEqual(regs[4],ctx+12)
        regs[2]=len(raw);regs[3]=ctx+12+len(raw)
        regs=execute(code[12:],0x10ce48,regs,memory)
        self.assertEqual(regs[29],0x1800);self.assertEqual(regs[30],fp)
        return regs[2]

    def test_ascii_caption_is_centered(self):
        self.assertEqual(self.caption(b'Bot Book',True),112)
        self.assertEqual(self.caption(b'Bot Book',False),136)
        for n in range(1,17):self.assertEqual(self.caption(b'X'*n,True),160-6*n)

    def test_all_original_facility_captions_retain_positions(self):
        for s in ['スターコレクション','そうこ','ＧＢコンバート','バトシム','ロボポンずかん','そうじゅうせき','うえきばち','ベッド']:
            with self.subTest(s=s):self.assertEqual(self.caption(s.encode('shift_jis'),True),self.caption(s.encode('shift_jis'),False))

    def test_title_counts_ascii_cells(self):
        self.assertEqual(self.title(b'Bot Book',True),112)
        self.assertEqual(self.title(b'Bot Book',False),136)
        for n in range(17):self.assertEqual(self.title(b'X'*n,True),160-6*n)

    def test_japanese_title_position_stays_exact(self):
        for s in ['ロボポンファイル','ロボポンずかん','スターコレクション','ＧＢコンバート','バトルシミュレーション']:
            raw=s.encode('shift_jis');self.assertEqual(self.title(raw,True),self.title(raw,False))
        self.assertEqual(self.caption(b'',True),160)

    def test_exact_layout_required_for_each_ui_path(self):
        layout=[{'offset':hex(p),'source_hex':a,'target_hex':b} for p,(a,b) in required_words().items()]
        menu=[{'offset':hex(p)} for p in [0xfb84e,0x10d9f8,0x10da7c,0x10da8c]]
        require_layout(menu,layout)
        for omitted in range(len(layout)):
            with self.assertRaisesRegex(ValueError,'exact caption'):require_layout(menu,layout[:omitted]+layout[omitted+1:])
        bad=[dict(x) for x in layout];bad[0]['target_hex']='3c013f80'
        with self.assertRaises(ValueError):require_layout(menu,bad)

    def test_each_facility_caption_requires_centering_without_book_entry(self):
        from tools.ui_layout import FACILITY_CAPTIONS
        layout = [{'offset':hex(p),'source_hex':a,'target_hex':b}
                  for p,(a,b) in required_words().items()
                  if FACILITY_START <= p < FACILITY_START+40]
        for offset in FACILITY_CAPTIONS:
            menu = [{'offset':hex(offset)}]
            with self.subTest(offset=hex(offset)):
                require_layout(menu, layout)
                with self.assertRaisesRegex(ValueError, 'exact caption'):
                    require_layout(menu, [])
                for missing in range(len(layout)):
                    with self.assertRaises(ValueError):
                        require_layout(menu, layout[:missing]+layout[missing+1:])

    def test_older_ui_does_not_require_new_layout(self):
        require_layout([{'offset':'0x221324'}],[])
        # The UI guard runs before the source ROM check, including iterators.
        with self.assertRaisesRegex(ValueError,'exact caption'):
            build_story(b'',iter([{'offset':'0xfb84e'}]),[],layout=iter([]))

if __name__=='__main__':unittest.main()
