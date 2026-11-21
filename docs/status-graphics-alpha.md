# Bot status graphics alpha

Five baked profile headings now read **HUNGER, STRESS, TRAITS, PARTS and APPS**.
Cumulative coverage is **eight bitmap captions in two resources**, alongside the
unchanged **4,049 native records, 873 UI strings and 299 choice blocks**. Saved
Japanese names remain save data. Traits is a compact label for the overall
personality panel. Hunger remains green and Stress blue; the other headings use
dark text on their light plates. No stats, equipment, tasks or game events change.

## Original image and caption pixels

The profile background is resource **0x5AA (1450)**, 320×256 RGBA16, originally a
21,872-byte HVQ2 blob at **0x1B22138**. Its decoded pixels were recovered from the
exact predecessor’s native resource cache, then untiled from 64×32 blocks.
`translation/assets/status-base.rgba16.zlib` retains the verified baseline:
SHA-256 `cde14909a5fa959b67a18b929742a023bada87c16793156d7e6362b80e639943`.

The deterministic five-by-seven font changes only the five declared rectangles.
Each row takes its background from the specified adjacent plate sample. Ink and
shadow are explicit RGBA16 words. Everything outside those rectangles is identical
to the recovered original. The builder bounds and fingerprints decompression.

## Compact resource program

There is no room for another full raw background at the ROM tail. The earlier
translated equipment background, resource **0x5B4 (1460)**, already points to a
raw image at 0x1FD5360. Its **26,556-byte original compressed allocation at
0x1B477D8** therefore has no remaining directory owner once that replacement is
included. All 457 original directory records are checked for aliases/overlap.

The new status payload uses **24,552 bytes** of that reclaimed allocation:
a 100-byte metadata header, **220 bytes of MIPS**, the untouched original
21,872-byte HVQ2 status blob, and **2,360 bytes of caption runs**. It ends at
**0x1B4D7C0**; the remaining **2,004 original bytes** stay untouched. The status
source blob at 0x1B22138 also stays intact. Reclamation requires the equipment
owner’s exact original hash, its included relocated copy, sufficient capacity,
alignment and an unaliased directory range. It cannot silently borrow an asset
that is still in use.

The existing nine-word startup dispatcher at **0x103C–0x1060** now sends original
HVQ2 resources directly to the original decoder with arguments/return unchanged.
All **457 original resources** have that marker. Program-backed replacements run
from the **uncached KSEG1 alias** of their freshly DMA-loaded input buffer. Their
first two words are `beq zero,zero,+24; nop`, entering code after the 100-byte
header. Uncached instruction fetch avoids executing stale instruction-cache
contents when a temporary loading buffer is reused. This is a format for these
verified generated assets, not arbitrary user-supplied programs.

The status program saves/restores its stack, return address and s0–s4. It calls
the original cached HVQ decoder at **0x80069028** on the embedded source blob,
retaining output/work arguments. It then writes the bounded caption runs into
that same linear output buffer. The original allocation, tile conversion,
resource cache and rendering path continue unchanged. No full-image second
buffer or new decompressor is introduced.

The equipment asset uses a **12-byte copy program**, preserving the exact previous
translated pixels. Its uncached tail jump reaches the uncached alias of the
original copy routine, with the original caller return. Metadata/pixel input now
totals **163,952 bytes**, ending exactly at **0x1FFD3D0**. This deliberately uses
the former twelve-byte alignment gap before the book. **All 184 book allocations
starting there, and the final 64 bytes at 0x1FFFFC0, remain byte-identical.**

`translation/status-graphics.json` selects this protocol; the old graphics catalog
and RAW2 dispatcher remain supported together for historical builds. Mixed
program/legacy replacements are rejected. There are still **107 guarded layout
words**; only six words within the existing nine-word dispatcher change. All 98
other layout words and the loader call site remain exact. The preceding facility
ROM and BPS reproduce byte-for-byte with the historical dispatcher and graphics.

## Runtime evidence and limits

The exact release ROM cold-boots from a fresh reference EEPROM into file A,
day 2, 500G, the entered player name and Merlin. HUNGER, STRESS, TRAITS, PARTS
and APPS appear in their native profile plates, retaining Merlin's stats, Charm
and Fire v1. The Apps equipment screen retains EQUIPPED, SPARE APPS and MOVES.
Both complete 163,840-byte native image-cache outputs match their generated
images exactly. Native navigation reaches Bot Book; entry 38 retains Merlin,
64 No.038, GB No.161, Height 120 cm, Weight 130 kg and its four English biography
lines. The emulator then closes normally. Reference, default working and final
isolated EEPROMs retain the reference hash; no savestate is loaded or created.
This final run does not perform an in-game save.

An exploratory menu-return sequence reached the bed and saved only to its
isolated test EEPROM. That copy, identity and log were preserved separately.
The immutable reference and default working copy were unchanged. Final validation
was restarted from a fresh reference copy; exploratory screenshots are not used
as evidence for unchanged-save validation.

The complete runtime image-cache pixels are compared against generated images:
all 163,840 bytes of each background must match, including pixels outside the
new captions and the previous equipment image. MIPS execution tests exercise
both dispatch branches, uncached entry/header/copy paths, HVQ arguments, output
writes, caller clobbers, delayed branches, saved registers and return addresses.

These are emulator checks, not hardware validation. Other species/menus and
older native/UI branches retain their documented limits. The new headings do
not establish hunger/stress behavior, personality mechanics or equipment effects.
Other Japanese UI/graphics remain, including save-file A/B plates and other frames.

## Build, checks and recovery

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/facility-captions-menu.json --story translation/late-dialogue-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/status-graphics.json --update-checksum --validate-moves \
  --output local/status-graphics-alpha.z64 --patch local/status-graphics-alpha.bps
```

Apply the cumulative BPS directly to the exact Japanese original. All **158 tests**
pass in source and clean restoration. Eight new tests cover native program
execution, argument/register/return preservation, rectangle/run bounds, malformed
streams, exact ownership/capacity, changed sources, aliases and loader guards.
Floating IPS independently reproduces the ROM; read-only chksum64 agrees with
CIC-6102 CRC1/CRC2 **603D64ED 4BB35E71**. ROM size remains 32 MiB.
MD5: `5DF41F0A0726DF0E04C499F6D350A246`.
SHA-256: `c2ae60742bd1c98101d35931a56c5d9a1bb36c20e82d4c075d9ca074fa272ddc`.

Actual-ROM proof permits only the two graphic descriptors/payloads, startup
dispatcher and checksum bytes to differ from facility-captions-alpha. All preceding
text, native pools/source slots, donors, grids, exclusions and book bytes stay exact.
The AES-256 archive verifies **1,036 payload files**, source revision,
ROM/BPS/save/evidence hashes, modes, emulator library symlink and all six regenerated
exact-ROM profile files through a clean restore. Existing passphrase stays outside
Git. Current/preceding encrypted working copies and verified restores are kept;
older historical ciphertext remains in Git/GitHub. See RESTORE.md and backups/README.md.

Next: remaining bitmap headings, starting with save-file A/B plates and Parts/
evolution frames. Preserve both program resource allocations, their reclaimed
owner, all book placements and the final 64 bytes. No free tail space has appeared.

## Caption rectangles

| Source | English | Rectangle (x0,y0,x1,y1) | Ink |
| --- | --- | --- | --- |
| くうふく | HUNGER | [204, 21, 257, 33] | 0441 |
| ストレス | STRESS | [204, 53, 257, 65] | 0031 |
| そうごうせいかく | TRAITS | [64, 53, 118, 63] | 084f |
| パーツ | PARTS | [174, 92, 211, 104] | 084f |
| ソフト | APPS | [174, 134, 211, 146] | 084f |
