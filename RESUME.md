# Resume the Robopon 64 translation

Current milestone: **equipment-labels-alpha**: 3,781 native records, 832 UI strings, 299 native choice blocks, plus three bitmap captions. This is a partial English draft. See `docs/equipment-labels-alpha.md` for precise runtime coverage.

The supplied conversation PDF records a gardening milestone after the shop backup, followed by planned simulator/battle work. Its gardening patch and source were unavailable. Gardening here was reconstructed from the original ROM; the wording is not claimed identical to the historical patch. Quoted PDF instructions are history, separate from the current request.

## Check before continuing

The cloud previously resumed at bed/save commit `ea7c7d3` while GitHub already had shop commit `b6b2202`. Check freshness before choosing work:

```sh
python -m tools.check_workspace --check-remote --require-save
python -m unittest discover -s tests -q
```

The check verifies remote ancestry, rebuilds in memory and checks the ROM/BPS and reference EEPROM without changing files. The current suite has 134 tests. Fetching does not update a stale checkout: compare `git log --oneline HEAD..origin/codex/verified-workspace-recovery` after fetching before merging or switching. Omit `--check-remote` for an offline archive and confirm freshness separately.

## Rebuild

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/equipment-labels-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves --output local/equipment-labels-alpha.z64 --patch local/equipment-labels-alpha.bps
```

Apply `releases/equipment-labels-alpha.bps` only to the exact original Japanese ROM. Do not stack earlier patches. The release manifest records hashes; the current ROM MD5 prefix is `89C91C55`. All source-byte, control, width and budget guards remain enabled. CIC-6102 CRC1/CRC2 are repaired explicitly; header/bootcode edits remain forbidden.

## Native save

`local/bed-save-final-saved.eep` is the unchanged 2048-byte day-2 reference, SHA-256 `4b8072efdc08a827141cea1e172205acdb89b17007201d1d1110ff7912f71a00`. File A holds 500G, the entered player name and Merlin.

The current ROM's working copy is `local/native-saves/Robot Ponkottsu 64 - 7tsu no Umi-89C91C55.eep`. Keep the reference intact and use separate copies for testing. New ROM revisions need a save copy under their own MD5-based filename. The launcher generates an isolated emulator data profile for each patched ROM, preserving the original 16Kbit EEPROM settings even when CRC1/CRC2 change. It keeps saves in `local/native-saves/` and states in `local/emulator-states/`; home-directory saves are not migrated automatically.

## Emulator

On Linux with Xorg's dummy driver and Mesa, start `tools/start-display.sh` in one terminal. In another, from this directory:

```sh
DISPLAY=:7 LIBGL_ALWAYS_SOFTWARE=1 \
ROM_PATH="$PWD/local/equipment-labels-alpha.z64" \
tools/emulator.sh --windowed --gfx mupen64plus-video-glide64mk2 --audio dummy \
  --input mupen64plus-input-sdl --rsp mupen64plus-rsp-hle
```

Return = Start; left Shift = A; left Control = B; arrows = stick; c = R; Escape = quit. R opens navigation: use 3F/Pots for gardening and 2F/Btl Sim for practice battles. Face the facility and walk toward it before pressing A. Wait for transitions and text to finish.

Cold-boot new builds and use native EEPROM for persistence checks. Historical
savestates belong to their exact ROMs and cannot validate this build. In particular,
`local/fire-blue-story-evidence/opening-502.st0` belongs only to the preceding
ROM MD5 `07EC747C6805124E327FC2A1872EED28`; never load it on this build. That earlier
checkpoint checked opening records 502–509. This build's new Sunny Blue variant branches,
and earlier Water/Fire Blue branches including 831's page, await playthrough. The
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

Continue bot-book text from native record **3694**; 3673–3693 were translated
earlier. These entries use four lines with varying native widths. Inspect their
reader before choosing encoding; do not force unverified records through the
existing fixed-grid path or truncate information to satisfy the label guard.

The equipment milestone adds 127 labels (3537–3664 except existing Charm 3604)
and eight Pearlton warnings (3665–3672). 119 labels use explicit donor tails and
eight fit inline. Preserve all **249 stored-label ranges in 155 donors**. The
prior 130 placements are unchanged. Subtract every occupied interval before
allocating; a donor may be any explicitly translated non-relocated record, but
its live encoded text is never free. All fifteen existing fixed grids retain
full counts and their exact guarded layouts. All earlier 3,646 entries, active
bytes and descriptors are unchanged. Charm, Berry and saved nicknames remain.

Four guarded horizontal-scale words at 0x21B3A8, 0x217540, 0x216604 and
0x2171C0 change 1.0 to 0.5 for the profile, Gear Set equipped caption and
right-column item rows. Positions, vertical scales, IDs
and draw calls stay exact. A descriptor-only preview displays the actual
sixteen-cell Hell Caterpillar text in Charm's fields. The release still uses
Charm. See the notes and local/equipment-labels-evidence for exact identities
and observed screens. The profile and Gear Set equipped caption were observed;
the empty right-hand inventory does not exercise item rows. Reference/default/isolated EEPROMs are unchanged; no
savestate or in-game save was used in this milestone.

Fuel warnings and other equipment contexts remain build-validated and need
gameplay checks, as do prior chore/minigame/pest/reaction/name/newline/donor/
regional scenes. Never load an older ROM's savestate to validate a new build.
Graphical labels, Parts frame, capacity warnings, five anchored pages and
VS/Transfer Pak remain unfinished.

The recovery archive uses .part001 and .part002. PROJECT_STATE's backup field
points to the JSON index. Verify part hashes, concatenate in order, verify the
whole ciphertext, decrypt, then verify the ZIP. Exact commands are in
backups/README.md. Keep both parts, index and checksum files together; the
existing passphrase applies.

Update this handoff, `PROJECT_STATE.json` and the recovery archive when the milestone changes. A running cloud process is not a persistent checkpoint.

The durable translation checkpoint is the Git tag `equipment-labels-alpha`. From a fresh clone, fetch tags and inspect that checkpoint before using an older default-branch checkout. Preserve local changes before switching revisions.
