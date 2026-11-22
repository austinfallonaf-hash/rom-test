# Resume the Robopon 64 translation

Current milestone: **save-file-graphics-alpha**: 4,049 native records, 873 UI strings, 299 native choice blocks, plus ten bitmap captions. This is a partial English draft. See `docs/save-file-graphics-alpha.md` for precise runtime coverage.

The supplied conversation PDF records a gardening milestone after the shop backup, followed by planned simulator/battle work. Its gardening patch and source were unavailable. Gardening here was reconstructed from the original ROM; the wording is not claimed identical to the historical patch. Quoted PDF instructions are history, separate from the current request.

## Check before continuing

The cloud previously resumed at bed/save commit `ea7c7d3` while GitHub already had shop commit `b6b2202`. Check freshness before choosing work:

```sh
python -m tools.check_workspace --check-remote --require-save
python -m unittest discover -s tests -q
```

The check verifies remote ancestry, rebuilds in memory and checks the ROM/BPS and reference EEPROM without changing files. The current suite has 160 tests. Fetching does not update a stale checkout: compare `git log --oneline HEAD..origin/codex/verified-workspace-recovery` after fetching before merging or switching. Omit `--check-remote` for an offline archive and confirm freshness separately.

## Rebuild

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/facility-captions-menu.json --story translation/late-dialogue-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/save-file-graphics.json --update-checksum --validate-moves --output local/save-file-graphics-alpha.z64 --patch local/save-file-graphics-alpha.bps
```

Apply `releases/save-file-graphics-alpha.bps` only to the exact original Japanese ROM. Do not stack earlier patches. The release manifest records hashes; the current ROM MD5 prefix is `F2D9DED6`. All source-byte, control, width and budget guards remain enabled. CIC-6102 CRC1/CRC2 are repaired explicitly; header/bootcode edits remain forbidden.

## Native save

`local/bed-save-final-saved.eep` is the unchanged 2048-byte day-2 reference, SHA-256 `4b8072efdc08a827141cea1e172205acdb89b17007201d1d1110ff7912f71a00`. File A holds 500G, the entered player name and Merlin.

The current ROM's working copy is `local/native-saves/Robot Ponkottsu 64 - 7tsu no Umi-F2D9DED6.eep`. Keep the reference intact and use separate copies for testing. New ROM revisions need a save copy under their own MD5-based filename. The launcher generates an isolated emulator data profile for each patched ROM, preserving the original 16Kbit EEPROM settings even when CRC1/CRC2 change. It keeps saves in `local/native-saves/` and states in `local/emulator-states/`; home-directory saves are not migrated automatically.

## Emulator

On Linux with Xorg's dummy driver and Mesa, start `tools/start-display.sh` in one terminal. In another, from this directory:

```sh
DISPLAY=:7 LIBGL_ALWAYS_SOFTWARE=1 \
ROM_PATH="$PWD/local/save-file-graphics-alpha.z64" \
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

Continue remaining bitmap/UI headings, starting with **Parts/evolution frames**.
Both save-file plates now read FILE A and FILE B, with the original bitmap font
at twice its small size. Coverage is 4,049 native records, 873 UI strings,
299 choice blocks and ten bitmap captions in three resources. All 160 tests pass.
See docs/save-file-graphics-alpha.md.

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

Use translation/save-file-graphics.json with the existing uncached program
dispatcher. The new 19,352-byte resource-1461 file payload at 0x1B22138 ends at
0x1B26CD0. It reclaims the original 21,872-byte resource-1450 status allocation;
2,520 original suffix bytes remain unchanged. Status already embeds its exact
original HVQ2 source in its relocated program, so its pixels/code stay exact.
The original file blob at 0x1B4DF94 stays intact. Relocation requires both included
owners, original hashes, capacity, alignment and no aliases anywhere in the full
reclaimed allocation. A resource program cannot borrow another active asset.

Retain the 24,552-byte status payload at 0x1B477D8 within the reclaimed 26,556-byte
original equipment source. Equipment remains at 0x1FD5360, using 163,952 bytes and
ending exactly at 0x1FFD3D0. All 184 book allocations starting there, the final
64 FF bytes, all prior text/native pools/donors/grids/exclusions and 107 guarded
layout words remain byte-exact. No new ROM-tail space is available.

The reference day-2 EEPROM stays immutable. Use isolated reference copies and
exact-ROM profiles. Confirm the screen before dependent input; B can return
farther than expected. A prior milestone's exploratory bed save is preserved
separately under local/status-graphics-evidence; it is historical evidence, not
this milestone's save validation. Never load older-ROM savestates.
Other species/branches, file creation/copy/delete/saving and hardware behavior
retain documented limits. CRC1/CRC2 remain 603D64ED 4BB35E71 because the changed
graphic bytes lie outside the CIC checksum's covered region.

Non-cone sparse checkout keeps current/preceding encrypted copies; older
snapshots remain in Git/GitHub. Update slugs before staging the next backup.
The older 996-file facility restore was checked against its manifest, historical
source, canonical private assets and ciphertext; 36 extra files were preserved.
Remove that generated tree only after the new clean restore passes, retaining
this checkpoint and the preceding 1,036-file status restore. Never remove unique
assets. Git configuration is not archived; backups/README.md gives the patterns.

Recovery requires both ciphertext parts, JSON index and three checksum files.
Verify parts, join, verify ciphertext, decrypt and verify ZIP. The existing
passphrase stays outside Git. The clean restore must validate payload hashes,
source revision, executable modes, emulator library symlink, native saves,
evidence and all six regenerated exact-ROM profile files.

Update this handoff, `PROJECT_STATE.json` and the recovery archive when the milestone changes. A running cloud process is not a persistent checkpoint.

The durable translation checkpoint is the Git tag `save-file-graphics-alpha`. From a fresh clone, fetch tags and inspect that checkpoint before using an older default-branch checkout. Preserve local changes before switching revisions.
