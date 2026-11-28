# Interface headings alpha

The three Japanese captions baked into the app-equipment background now read
EQUIPPED, SPARE APPS and MOVES. Previous text catalogs are retained unchanged:
323 native records, 832 UI strings and 299 choice blocks, plus three new bitmap
captions. Other graphic headings and later story remain unfinished.

## Rebuild

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/battle-moves-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/interface-headings-alpha.z64 --patch local/interface-headings-alpha.bps
```

Apply `releases/interface-headings-alpha.bps` to the exact Japanese original,
without stacking patches. The target remains 32 MiB. The build uses Python's
standard library and the tracked recovered bitmap; no emulator state, screenshot,
font installation or extra private graphic input is needed to rebuild it.

## Sprite replacement

Resource 0x5B4 is a 320-by-256 HVQ2 background. It contains all three caption
plates. Its decoded 16-bit pixels were recovered from the supplied emulator's
resource cache and untiled from 64-by-32 blocks. The original compressed blob's
SHA-256 and the recovered pixel SHA-256 are recorded in the graphics catalog.
The latter is `d9a3e0e89490c968b3d21a2851ee685010a5877078f93e30630d99da64e43274`.
The baseline is tracked as `translation/assets/equipment-base.rgba16.zlib`.
The build bounds decompression and verifies this fingerprint before rendering.

`tools.graphics` replaces only the declared caption rectangles with deterministic
five-by-seven capital letters and row-matched plate backgrounds. Pixels outside
these rectangles stay identical to the recovered baseline. The resource's
format, dimensions and other metadata are retained. The new RAW2 header carries
the payload byte count at offset 0x10, followed by the pixels after its 100-byte
header. The original resource-directory entry is redirected to the guarded
0xFF-filled tail at ROM offset 0x1FD5360. The replacement occupies 163,940 bytes
and ends at 0x1FFD3C4, within the original 32 MiB image.

## Loader dispatch

The HVQ2 decode call at ROM 0x56270 now calls a nine-word dispatcher in the
unreachable startup alignment gap at 0x103C..0x105F (RAM 0x8000043C).
The original startup jumps from 0x80000434, through its delay slot, to
0x80000460; neither that jump nor its destination is changed. The gap is
in the loaded text segment and precedes the startup BSS-clear range.

For the RAW2 marker, the dispatcher sends input+100, the output buffer and the
stored byte count to the original source/destination/length copy routine at
0x8007BEC0. All original HVQ2 inputs tail-call the original decoder at
0x80069028 with their arguments and caller return address preserved. The
existing tile conversion and resource cache still run. The raw input requires
about 134 KiB more temporary loading memory; the cached output size is unchanged.

The builder requires both exact dispatcher bytes and its guarded call site
before writing a RAW2 asset. It checks source blob/pixel fingerprints, dimensions,
caption bounds, non-overlap, directory metadata and unused destination bytes.
These ten instruction edits extend the existing layout catalog to 81 words.
CIC-6102 CRC1/CRC2 are repaired; bootcode and other header fields stay intact.

All 108 tests pass, including dispatcher instruction execution for raw and HVQ2
paths, return/argument preservation, bounded compressed input, caption boundaries,
metadata and source/padding/overlap guards. Independent chksum64 agrees with the
header CRCs, and Floating IPS reproduces the target from the BPS.

## Runtime coverage

The exact final ROM (MD5 `212AB2AA372C527D8D3451C6CCD2A317`) cold-booted
using an isolated copy of the preserved native EEPROM. File A retained day 2,
500G, the entered player name and Merlin. The equipment screen displayed all
three English caption plates with the existing Fire v1, Attack and Fire Charm
content and surrounding artwork. The run returned to ship control and entered
a simulator practice battle with the normal HUD visible. No older-build
emulator state was loaded.
Evidence is under `local/interface-headings-evidence/`; its equipment state
belongs only to this exact ROM. Checks use the supplied Mupen64Plus bundle and
Glide64mk2; they do not establish hardware validation or every image/menu branch.
Earlier coverage remains in [battle moves notes](battle-moves-alpha.md) and
[simulator/gardening notes](simulator-alpha.md).
