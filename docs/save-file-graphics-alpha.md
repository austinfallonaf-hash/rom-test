# Save-file graphics alpha

The save-selection plates now read **FILE A** and **FILE B**, matching the existing
Select a save file prompt. The five-by-seven bitmap font is drawn at **2× scale**,
with black ink and a white offset outline inside the original orange/purple plates.
No file operations, selection logic, names or saved data change.

Cumulative coverage is **4,049 native records, 873 UI strings, 299 choice blocks
and ten bitmap captions in three resources**. Other UI/graphics and gameplay
branches remain incomplete. Saved Japanese player/bot names remain save data.

## Source and pixels

The 320×256 RGBA16 background is resource **0x5B5 (1461)**. Its original HVQ2 blob
is **17,556 bytes at 0x1B4DF94**, SHA-256
`84ae7a8cad9ba99bcef849564e26844a4b4e278fca9a9733792b5e4f3bcf19a3`.
The exact predecessor's native cache provided its complete decoded image, untiled
from 64×32 blocks. `translation/assets/save-file-base.rgba16.zlib` retains those
pixels, SHA-256 `ccd2b49252034f42ef6628acd780860c3d38b7c5d09721c37bfc282d47e764a0`.

| Original | English | Rectangle (x0,y0,x1,y1) | Background sample x |
| --- | --- | --- | --- |
| セーブデータ A | FILE A | [52,28,126,45] | 50 |
| セーブデータ B | FILE B | [196,28,270,45] | 194 |

Each row uses its adjacent original plate color. Only the two bounded rectangles
change. Scale defaults to one, retaining all previous raster output; only integer
one/two are accepted. Both glyph and offset outline expand to uniform square
blocks and must fit their declared rectangle. Updated pixel SHA-256:
`d1b1b71970e4c346cfb1d027696dc18ccf6c8ed38cc534dba9cd29223c76d633`.

## Reclaimed allocation and unchanged programs

Resource 1450, the status background, was relocated in status-graphics-alpha and
already embeds its untouched original HVQ2 source in its replacement program.
Its former **21,872-byte allocation at 0x1B22138** is no longer directory-owned.
The new file payload uses **19,352 bytes**, ending at **0x1B26CD0**. It contains a
100-byte metadata header, the existing **220-byte MIPS program**, 17,556 embedded
original HVQ2 bytes and **1,476 caption-run bytes**. The remaining **2,520 original
bytes** are unchanged. The original file blob at 0x1B4DF94 also stays untouched.

The builder now permits a reclaimed owner relocated through an HVQ patch as well
as a native copy. It requires the exact original owner's hash, its single included
program entry, relocation out of that allocation, sufficient capacity and alignment.
All 457 original descriptors are checked for aliases across the **entire reclaimed
source allocation**, including its unused suffix. Every owner's own replacement
is also validated, and the builder rejects overlapping final edits. Embedded
source bytes are read from the immutable original ROM, not earlier edits.

The two earlier resource programs and descriptors remain byte-exact: status uses
24,552 bytes at 0x1B477D8 in the reclaimed original equipment allocation; equipment
uses 163,952 bytes at 0x1FD5360, ending exactly at 0x1FFD3D0. Both owners must stay
included/relocated. The nine-word dispatcher and all **107 layout guards** are
unchanged. Program code executes through the uncached RDRAM input alias, calls
the original HVQ decoder, then writes only generated caption runs into its output.
No new decompressor, image buffer or rendering path is introduced.

**All 184 book allocations from 0x1FFD3D0, and final 64 FF bytes, remain exact.**
There is no new free ROM-tail space. Historical status ROM/BPS reproduce exactly
with current tools and their original graphics catalog.

## Runtime checks and limits

The exact release ROM cold-boots into the save-selection screen. FILE A and
FILE B appear inside their original plates; selecting B brightens its plate and
dims A, then selecting A restores the opposite state. B remains an empty New File
slot and is not activated. File A loads through its existing Load action, retaining
day 2, 500G, the entered player name and Merlin. The profile retains HUNGER,
STRESS, TRAITS, PARTS and APPS with unchanged stats, Charm and Fire v1. Equipment
retains EQUIPPED, SPARE APPS and MOVES. All three complete 163,840-byte native
background-cache outputs match their generated images exactly. Bot Book entry 38
retains Merlin, 64 No.038, GB No.161, Height 120 cm, Weight 130 kg and its four
English biography lines. The emulator closes normally. Reference, default working
and isolated runtime EEPROM hashes stay unchanged; no save or savestate is used.

All three complete native image-cache outputs must match generated images:
163,840 bytes each for the file, status and equipment backgrounds. Source/cache
identities, normal emulator log, selected-file screenshots, native EEPROM and a
portable actual-ROM proof are retained in private runtime evidence.

These are emulator display/load checks, not hardware validation or tests of file
creation/copy/delete/saving, hunger/stress/personality behavior, other species or
older native/UI branches. Their prior limits remain. An earlier milestone's
exploratory bed save is retained separately under status-graphics evidence; it
is historical and is not this milestone's validation save.

## Build and recovery

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/facility-captions-menu.json --story translation/late-dialogue-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/save-file-graphics.json --update-checksum --validate-moves \
  --output local/save-file-graphics-alpha.z64 --patch local/save-file-graphics-alpha.bps
```

Apply the cumulative BPS directly to the exact Japanese original. All **160 tests**
pass in source and clean restoration. The two new regressions check exact 2×
nearest-neighbor glyph/outline output and a reclaimed HVQ-owner chain, rejecting
an alias in the unused suffix. Existing MIPS execution coverage now also exercises
a scaled caption. Invalid scales and oversized scaled rectangles are rejected.

Floating IPS independently reproduces the ROM. Read-only chksum64 agrees with
CIC-6102 CRC1/CRC2 **603D64ED 4BB35E71**; these values remain unchanged because
the edits are outside the checksum-covered region. ROM size stays 32 MiB.
MD5: `F2D9DED6540F403F99834A95A046169C`.
SHA-256: `17f6f2434507e9ac29407c83f154db2abb22bf6ad904e8d2707ccf3590a0e995`.

Actual-ROM proof permits only resource 1461's descriptor and its 19,352-byte
payload to differ from status-graphics-alpha. Every other byte, including earlier
text/native/source slots, donors, grids, exclusions, code, CRCs, old programs and
book, remains exact. Pixels outside the two rectangles also remain identical.

The AES-256 archive verifies **1,077 payload files**, source revision,
hashes, modes, emulator library symlink, native saves, evidence and all six
regenerated exact-ROM profile files through a clean restore. The passphrase stays
outside Git. Current/preceding encrypted working copies and verified restores are
retained; older ciphertext stays in Git/GitHub. The older 996-file facility restore
was manifest/source/canonical/cipher verified with 36 extras preserved before its
generated tree is removed after the new restore passes. See RESTORE.md and
backups/README.md.

Next: remaining bitmap/UI headings, beginning with Parts/evolution frames.
Preserve all three program resources, both reclaimed owners and the book tail.
