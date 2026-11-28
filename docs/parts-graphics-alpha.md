# Parts graphics alpha

The Gear screen's two baked headings now read **EQUIPPED** and **SPARE PARTS**.
They use the same small white bitmap font as the Apps equipment screen, inside
the original red plates. Only those two caption rectangles change; equipment
names, stats, selection and game behavior stay intact. Saved Japanese names
remain save data. Evolution and other UI/graphics remain unfinished.

Cumulative coverage is **4,049 native records, 873 UI strings, 299 choice blocks
and twelve bitmap captions in four resources**.

## Source image and rectangles

The Parts background is resource **0x5B3 (1459)**, 320×256 RGBA16. Its original
20,412-byte HVQ2 source is at **0x1B4281C**, SHA-256
`25a9347a77b9a0b738450b0adaf7555fbd9a0771420d7c74b2cc92613099e8d0`.
The complete original decoded image was recovered from the exact predecessor's
native cache, untiled from 64×32 blocks and retained in
`translation/assets/parts-base.rgba16.zlib`. Pixel SHA-256:
`36f3d8edb3991e993fcee76e0e3fd9ff46ee53e1c8b7e4b30ab8b9f6b6d22da1`.

| Source | English | Rectangle (x0,y0,x1,y1) | Background sample x |
| --- | --- | --- | --- |
| そうびパーツ | EQUIPPED | [40,79,110,92] | 39 |
| もちものパーツ | SPARE PARTS | [178,20,255,32] | 255 |

Each row takes its adjacent original red-plate color. Ink is FFFE and shadow
0000; every pixel outside the two rectangles remains identical. New pixel hash:
`1f0268cc64d00c6e632c427136073061e49de4de0364b30ba680f6e454570153`.

## Palette runs and allocation

The previous full-color run format would require **22,300 bytes**, exceeding the
21,872-byte original status allocation. The new `hvq_palette` format preserves
the original HVQ decoder and changes only the generated caption-run encoding.
Each rectangle stores output offset, width/height, ink and shadow. Each row stores
its original background color, followed by one-byte runs: the upper two bits
select background/ink/shadow, and the lower six hold a length from 1 to 63. The
fourth color index and zero-length runs are invalid. Long runs split at 63 pixels.

The program calls the original decoder with its existing arguments, saves/restores
s0–s4, stack and return, then writes the generated rows into the original output.
It uses its own stack argument area for the three colors after the HVQ call has
returned. Row background words are loaded as two bytes because preceding packed
runs can leave them unaligned; metadata and halfword output remain aligned.
No new image buffer, decompressor, global code hook or rendering path is added.

The new payload is **21,384 bytes** at **0x1B22138**, ending **0x1B274C0**:
100-byte metadata header, **264-byte MIPS program**, four alignment bytes,
20,412 embedded original HVQ2 bytes and **604 palette-run bytes**. It fits the
21,872-byte original status allocation with **488 original suffix bytes** intact.

To free that allocation, the existing **19,352-byte file-selection program** moves
as a whole to the original Parts allocation at **0x1B4281C**, ending **0x1B473B4**.
Its complete payload, code and pixels are byte-identical to save-file-graphics-alpha;
**1,060 original suffix bytes** remain intact. Parts embeds its exact original
compressed source from the immutable ROM before any replacement writes occur.

The four-resource ownership chain is File → Parts → Status → Apps. Every owner
must remain included and relocated. Exact source hashes, full allocation alias
checks, capacity/alignment and final overlap guards stay enabled. New palette
entries may act as relocated owners; mixed legacy RAW2/program catalogs remain
rejected. Plain-run/copy payloads keep their exact historical format.

Status stays byte-exact at 0x1B477D8 (24,552 bytes), and Apps stays byte-exact at
0x1FD5360 (163,952 bytes), ending exactly at **0x1FFD3D0**. All **184 Book
allocations** from that address and the final **64 FF bytes** remain exact.
All **107 layout words**, including the uncached program dispatcher, are unchanged.
There is no additional ROM-tail space. The original file blob at 0x1B4DF94 is
unchanged; any future reclamation needs its included relocated-owner guards.
Original sources remain in the supplied immutable ROM; do not infer that
overwritten old allocations are still free.

## Native evidence and limits

The exact release ROM cold-boots into the file screen with FILE A and FILE B
intact. Native file A loads day 2, 500G, the entered player name and Merlin. Its
profile retains the five translated headings, stats, Charm and Fire v1. Gear
then displays EQUIPPED and SPARE PARTS in the original red plates, with Charm,
ATK 7, DEF 8, SPD 0 and RAM 10M intact. Apps retains EQUIPPED, SPARE APPS and
MOVES. All four complete 163,840-byte native background-cache outputs match
their generated images exactly. Native navigation also reaches Book entry 38,
retaining Merlin, 64 No.038, GB No.161, Height 120 cm, Weight 130 kg and its
four biography lines. The emulator closes normally. Reference, default working
and isolated runtime EEPROM hashes remain unchanged; no in-game save or
savestate is used. No equipment change/removal or evolution is confirmed.

The complete native image-cache outputs for Parts, file selection, status and
Apps are compared against their generated backgrounds, **163,840 bytes each**.
Source identities, screenshots, normal emulator logs, cache zlib/JSON, unchanged
native EEPROM and portable actual-ROM proof are retained in private evidence.

These are emulator display/load checks. Equipment setting/removal, evolution,
other species/branches and hardware retain their prior limits. The older
status milestone's exploratory bed-save copy remains historical evidence in its
own directory, separate from this milestone's validation.

## Build and recovery

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/facility-captions-menu.json --story translation/late-dialogue-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/parts-graphics.json --update-checksum --validate-moves \
  --output local/parts-graphics-alpha.z64 --patch local/parts-graphics-alpha.bps
```

Apply the cumulative BPS directly to the exact Japanese original. All **164 tests**
pass in source and clean restoration. Four new tests cover native palette execution
with scaled text, long runs, row gradients and duplicate colors; malformed stream,
color/geometry checks; and an exact allocation that fits palette runs but rejects
full-color runs. The instruction runner now checks word/halfword alignment as
well as delay slots, argument/register preservation, writes and return addresses.

Actual-ROM proof permits only two descriptors and two payloads to differ from
save-file-graphics-alpha. Previous status/Apps bytes, every native/UI/source slot,
donor/grid/exclusion, game instruction, checksum byte and Book allocation stays
exact. Pixels outside the Parts rectangles are also identical. The preceding
ROM and BPS reproduce byte-for-byte with current tools and their old catalog.

Floating IPS independently reproduces the ROM; read-only chksum64 agrees with
CIC-6102 CRC1/CRC2 **603D64ED 4BB35E71**. Edits are outside the covered checksum
region, so CRCs remain unchanged. ROM size remains 32 MiB.
MD5: `3616DA437AE5A473A761AE025B9DFCA3`.
SHA-256: `c673238c5714f9158ef5d7c3667b0572e80dcd7af2b8363ec552b4a660fdb1f4`.

The AES-256 archive verifies **1,120 payload files**, source revision,
hashes, modes, emulator library symlink, native saves/evidence and all six
regenerated exact-ROM profile files through a clean restore. The passphrase stays
outside Git. Current/preceding encrypted copies and verified restores are retained.
The older 1,036-file status restore was checked against its manifest, historical
source, canonical assets and ciphertext; **38 extras** were preserved before its
generated tree is removed after the new clean restore passes. Older ciphertext
remains in Git/GitHub. See RESTORE.md and backups/README.md.

Next: evolution frames, save-screen progress label and remaining UI/graphics.
