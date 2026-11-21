"""Exercise the shipped MIPS alignment routine with ASCII and Shift-JIS names."""
import json
from collections import defaultdict
import unittest
from pathlib import Path


class BattleLayoutTests(unittest.TestCase):
    def test_opponent_alignment_counts_glyphs_instead_of_encoded_bytes(self):
        path = Path(__file__).resolve().parents[1]/'translation/battle-hud-layout.json'
        all_rows = json.loads(path.read_text())['entries']
        for kind, rows, base, end in [('move', all_rows[1:32], 0xB75F0, 0xB766C),
                                      ('name', all_rows[32:62], 0xB7278, 0xB72F0)]:
            self.check_counter(kind, rows, base, end)

    def check_counter(self, kind, rows, base, end):
        code = {int(row['offset'], 0): int(row['target_hex'], 16) for row in rows}
        self.assertEqual(sorted(code), list(range(base, end, 4)))
        for text in ['', 'Attack ', 'Fire Fara', 'アタック', 'ファイアファラ',
                     'Fireファラ', 'Thunder Knuckle', 'ｶﾅ', '海パンチ', 'Z']:
            with self.subTest(kind=kind, text=text):
                memory = defaultdict(int)
                def put(address, value):
                    memory.update({address+i:byte for i, byte in enumerate(value)})
                if kind == 'move':
                    put(0x1030, (0x2000).to_bytes(4, 'big'))
                    put(0x2122, text.encode('shift_jis')+b'\0')
                    memory[0x219F] = 2  # Third 20-byte move slot.
                else:
                    put(0x1038, (0x2000).to_bytes(4, 'big'))
                    put(0x2062, (3).to_bytes(2, 'big'))
                    put(0x800E8834, (0x2200).to_bytes(4, 'big'))
                    put(0x2200, text.encode('shift_jis')+b'\0')
                regs = [0]*32;regs[30] = 0x1000
                pc, next_pc, steps = base, base+4, 0
                while pc in code:
                    steps += 1
                    self.assertLess(steps, 1000)
                    word = code[pc];op=word>>26;rs=(word>>21)&31;rt=(word>>16)&31
                    rd=(word>>11)&31;shift=(word>>6)&31;imm=word&0xFFFF
                    signed=imm if imm<0x8000 else imm-0x10000
                    following = next_pc+4
                    address = (regs[rs]+signed)&0xFFFFFFFF
                    if op == 0:
                        if word&63 == 0: regs[rd] = regs[rt]<<shift
                        elif word&63 == 0x21: regs[rd] = regs[rs]+regs[rt]
                        else: self.fail(f'Unexpected instruction {word:08x}')
                    elif op == 0x23: regs[rt] = int.from_bytes(bytes(memory[address+i] for i in range(4)), 'big')
                    elif op == 0x20: regs[rt] = int.from_bytes(bytes([memory[address]]), 'big', signed=True)
                    elif op == 0x24: regs[rt] = memory[address]
                    elif op == 9: regs[rt] = regs[rs]+signed
                    elif op == 0x21: regs[rt] = int.from_bytes(bytes([memory[address], memory[address+1]]), 'big', signed=True)
                    elif op == 0xF: regs[rt] = imm<<16
                    elif op == 0xB: regs[rt] = int((regs[rs]&0xFFFFFFFF)<(signed&0xFFFFFFFF))
                    elif op in (4, 5):
                        if (regs[rs] == regs[rt]) == (op == 4): following = pc+4+signed*4
                    else: self.fail(f'Unexpected instruction {word:08x}')
                    regs[0] = 0
                    pc, next_pc = next_pc, following
                self.assertEqual(pc, end)
                self.assertEqual(regs[2], len(text))

    def test_composed_names_fit_the_battle_frames_and_prior_catalog_is_retained(self):
        root = Path(__file__).resolve().parents[1]
        old = json.loads((root/'translation/simulator-menu.json').read_text())['entries']
        new = json.loads((root/'translation/battle-hud-menu.json').read_text())['entries']
        self.assertEqual(new[:len(old)], old)
        prefixes = [r['translation'] for r in new if 0xC86B0 <= int(r['offset'],0) < 0xC8880]
        suffixes = [r['translation'] for r in new if 0xC8880 <= int(r['offset'],0) <= 0xC8990]
        self.assertTrue(prefixes and suffixes)
        for first in prefixes:
            for last in suffixes:
                self.assertLessEqual(len(first+last), 16, first+last)
        for row in new:
            if 0xC7010 <= int(row['offset'],0) <= 0xC70BC:
                self.assertLessEqual(len(row['translation']), 10)
