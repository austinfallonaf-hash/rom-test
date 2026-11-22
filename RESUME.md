# Resume the Robopon 64 translation

Current milestone: **parts-graphics-alpha**: 4,049 native records, 873 UI strings, 299 native choice blocks, plus twelve bitmap captions. This is a partial English draft. See `docs/parts-graphics-alpha.md` for precise runtime coverage.

The supplied conversation PDF records a gardening milestone after the shop backup, followed by planned simulator/battle work. Its gardening patch and source were unavailable. Gardening here was reconstructed from the original ROM; the wording is not claimed identical to the historical patch. Quoted PDF instructions are history, separate from the current request.

## Check before continuing

The cloud previously resumed at bed/save commit `ea7c7d3` while GitHub already had shop commit `b6b2202`. Check freshness before choosing work:

```sh
python -m tools.check_workspace --check-remote --require-save
python -m unittest discover -s tests -q
```

The check verifies remote ancestry, rebuilds in memory and checks the ROM/BPS and reference EEPROM without changing files. The current suite has 164 tests. Fetching does not update a stale checkout: compare `git log --oneline HEAD..origin/codex/verified-workspace-recovery` after fetching before merging or switching. Omit `--check-remote` for an offline archive and confirm freshness separately.

## Rebuild

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/facility-captions-menu.json --story translation/late-dialogue-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/parts-graphics.json --update-checksum --validate-moves --output local/parts-graphics-alpha.z64 --patch local/parts-graphics-alpha.bps
```

Apply `releases/parts-graphics-alpha.bps` only to the exact original Japanese ROM. Do not stack earlier patches. The release manifest records hashes; the current ROM MD5 prefix is `3616DA43`. All source-byte, control, width and budget guards remain enabled. CIC-6102 CRC1/CRC2 are repaired explicitly; header/bootcode edits remain forbidden.

## Native save

`local/bed-save-final-saved.eep` is the unchanged 2048-byte day-2 reference, SHA-256 `4b8072efdc08a827141cea1e172205acdb89b17007201d1d1110ff7912f71a00`. File A holds 500G, the entered player name and Merlin.

The current ROM's working copy is `local/native-saves/Robot Ponkottsu 64 - 7tsu no Umi-3616DA43.eep`. Keep the reference intact and use separate copies for testing. New ROM revisions need a save copy under their own MD5-based filename. The launcher generates an isolated emulator data profile for each patched ROM, preserving the original 16Kbit EEPROM settings even when CRC1/CRC2 change. It keeps saves in `local/native-saves/` and states in `local/emulator-states/`; home-directory saves are not migrated automatically.

## Emulator

On Linux with Xorg's dummy driver and Mesa, start `tools/start-display.sh` in one terminal. In another, from this directory:

```sh
DISPLAY=:7 LIBGL_ALWAYS_SOFTWARE=1 \
ROM_PATH="$PWD/local/parts-graphics-alpha.z64" \
tools/emulator.sh --windowed --gfx mupen64plus-video-glide64mk2 --audio dummy \
  --input mupen64plus-input-sdl --rsp mupen64plus-rsp-hle
```

Return = Start; left Shift = A; left Control = B; arrows = stick; c = R; Escape = quit. R opens navigation: use 3F/Pots for gardening and 2F/Btl Sim for practice battles. Face the facility and walk toward it before pressing A. Wait for transitions and text to finish.

Cold-boot new builds and use native EEPROM for persistence checks. Historical
savestates belong to their exact ROMs and cannot validate this build. In particular,
`local/fire-blue-story-evidence/opening-502.st0` belongs only to the preceding
ROM MD5 `07EC747C6805124E327FC2A1872EED28`; never load it on this build. That earlier
checkpoint checked opening records 502–509. New late-dialogue event triggers and the earlier Sunny/Water/Fire Blue
branches, including 831's page, await playthrough. The
current native-A cold boot checks the file/ship/pause displays and save contents.

## Recovery

The latest encrypted archive is identified by `PROJECT_STATE.json` and `backups/README.md`. It uses the existing recovery passphrase, kept outside Git. Verify the encrypted and decrypted checksums, then:

```sh
python tools/verify_backup.py /path/to/decrypted.zip
python -m tools.restore_backup /path/to/decrypted.zip /path/to/new-directory
```

The destination must not exist. Verification precedes extraction; executable modes and safe relative symlinks are preserved. It creates `rom-test/` within the destination. Keep the latest source checkout and compare versions before moving restored private assets into it. See `RESTORE.md`.

Keep the latest verified restore tree. Superseded restore-test trees and decrypted
staging ZIPs under `/workspace/work/` can fill the workspace. Before removing a
test tree, preserve its manifest and confirm its files have no changes. Extra
files must match canonical copies; preserve unmatched files. Remove a
superseded staging ZIP only when its hash matches a recorded backup checksum.
Encrypted snapshots, source checkouts and canonical ROM/save assets are separate
from these generated test copies.

## Next work

Continue remaining UI/bitmap headings, beginning with **evolution frames and
the save-screen progress label**. The Gear screen now reads EQUIPPED and SPARE
PARTS. Coverage is 4,049 native records, 873 UI strings, 299 choices and twelve
bitmap captions in four resources. All 164 tests pass. See docs/parts-graphics-alpha.md.

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

Use translation/parts-graphics.json and the unchanged uncached program dispatcher.
Parts resource 1459 uses the new hvq_palette stream: each rectangle stores ink and
shadow; each row stores its original background color followed by one-byte runs
(two-bit color index, six-bit length 1..63). The 264-byte program calls original HVQ
then copies these bounded runs into its output. Row colors are loaded as bytes
because packed streams can leave them unaligned. The stack palette is populated
after the HVQ call, preserving caller registers/return and original work buffers.
Plain HVQ-run/copy programs and legacy RAW2 builds retain their matching protocols.

Preserve all four resource programs and their owners:
- Parts 1459: 21,384 bytes at 0x1B22138, using original status capacity 21,872; 488 suffix bytes stay original.
- File 1461: 19,352 bytes at 0x1B4281C, using original Parts capacity 20,412; 1,060 suffix bytes stay original. Its payload/pixels are unchanged, relocated as a whole.
- Status 1450: 24,552 bytes at 0x1B477D8, inside original Apps capacity 26,556; unchanged.
- Apps 1460: 163,952 bytes at 0x1FD5360, ending exactly 0x1FFD3D0; unchanged.

Original compressed sources are embedded from the immutable ROM before edits.
Every reclaimed owner must stay included/relocated. Full-range aliases, source
hashes, capacity, alignment and final edit overlaps remain guarded. All 184 Book
allocations from 0x1FFD3D0 and final 64 FF bytes remain exact. There is no new tail
space. All 107 layout guards and every previous text/native/donor/grid/exclusion
byte remain unchanged. Source/save identities and exact-ROM profile rules above
still apply. Never load older-ROM savestates or walk toward bed in menu tests.

Only Parts caption display is added. Equipment changes/removal, evolution, other
species/branches and hardware retain prior limits. The old exploratory bed-save
copy remains historical evidence under local/status-graphics-evidence, separate
from current native EEPROM validation. CRC1/CRC2 remain 603D64ED 4BB35E71.

Non-cone sparse checkout keeps current/preceding encrypted copies; older snapshots
remain in Git/GitHub. Add new slugs before staging. The older 1,036-file status
restore was checked against its manifest, source, canonical assets and ciphertext;
38 extra files were preserved. Remove only its generated tree after the new clean
restore passes, retaining this checkpoint and the preceding 1,077-file save-file
restore. Never remove unique assets. Git configuration is not archived; see
backups/README.md for sparse patterns and retrieval commands.

Recovery requires both ordered ciphertext parts, index and three checksum files.
Verify, join, decrypt, verify ZIP, then restore into a new directory. The existing
passphrase stays outside Git. Check payload/source hashes, modes, library symlink,
native saves/evidence and all six regenerated exact-ROM emulator-profile files.

Update this handoff, `PROJECT_STATE.json` and the recovery archive when the milestone changes. A running cloud process is not a persistent checkpoint.

The durable translation checkpoint is the Git tag `parts-graphics-alpha`. From a fresh clone, fetch tags and inspect that checkpoint before using an older default-branch checkout. Preserve local changes before switching revisions.
