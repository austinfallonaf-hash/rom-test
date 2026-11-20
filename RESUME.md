# Resume the Robopon 64 translation

Current milestone: **minigame-guide-alpha**: 3,451 native records, 832 UI strings, 299 native choice blocks, plus three bitmap captions. This is a partial English draft. See `docs/minigame-guide-alpha.md` for precise runtime coverage.

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
  --menu translation/battle-moves-menu.json --story translation/minigame-guide-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves --output local/minigame-guide-alpha.z64 --patch local/minigame-guide-alpha.bps
```

Apply `releases/minigame-guide-alpha.bps` only to the exact original Japanese ROM. Do not stack earlier patches. The release manifest records hashes; the current ROM MD5 prefix is `207D8DD0`. All source-byte, control, width and budget guards remain enabled. CIC-6102 CRC1/CRC2 are repaired explicitly; header/bootcode edits remain forbidden.

## Native save

`local/bed-save-final-saved.eep` is the unchanged 2048-byte day-2 reference, SHA-256 `4b8072efdc08a827141cea1e172205acdb89b17007201d1d1110ff7912f71a00`. File A holds 500G, the entered player name and Merlin.

The current ROM's working copy is `local/native-saves/Robot Ponkottsu 64 - 7tsu no Umi-207D8DD0.eep`. Keep the reference intact and use separate copies for testing. New ROM revisions need a save copy under their own MD5-based filename. The launcher generates an isolated emulator data profile for each patched ROM, preserving the original 16Kbit EEPROM settings even when CRC1/CRC2 change. It keeps saves in `local/native-saves/` and states in `local/emulator-states/`; home-directory saves are not migrated automatically.

## Emulator

On Linux with Xorg's dummy driver and Mesa, start `tools/start-display.sh` in one terminal. In another, from this directory:

```sh
DISPLAY=:7 LIBGL_ALWAYS_SOFTWARE=1 \
ROM_PATH="$PWD/local/minigame-guide-alpha.z64" \
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

Continue ongoing-chore bot dialogue from native record 3342. The 22 additions
3320–3341 now have drafts. All preceding 3,429 entries and active text/descriptors
are identical. Three labels use guarded free padding: Knuckle, Hammer and Punch.
The total is 130 stored labels in 36 donors. Subtract every occupied range when
allocating; never treat a donor's whole padded tail as free.

Native grids 3323–3337 use kind fixed_grid. tools/fixed_grid.py permits only the
verified IDs and dimensions: 3323–3327 are 7 rows x 10 cells, even 3328–3336 are
3 x 21, odd 3329–3337 are 3 x 15. Catalog translation uses actual newline-separated
rows. They become right-padded native glyph rows without inserting a 2000 control.
Full original sizes/counts/pointers remain unchanged. Reader disassembly and
evidence are documented in the milestone notes. Do not reuse this path for other
records without verifying their reader. Source metadata and controls are guarded.

Four pest-control messages retain success/failure, runner loss and cleaning
warnings, preserving all controls and original budgets. Six new tests bring the
suite to 134. There are no new dialogue pages or newline opt-ins. Saved nicknames,
Berry, item effects and game events remain intact.

See the milestone notes/evidence for exact native-A and minigame runtime coverage.
Remaining minigame and pest branches, earlier reactions, name/newline contexts,
donor/regional scenes and five anchored pages need gameplay checks. Never load an
older ROM's savestate to validate a new build. Graphical labels, Parts frame,
capacity warnings and VS/Transfer Pak remain unfinished.

The encrypted snapshot uses .part001 and .part002. PROJECT_STATE's backup field
points to the JSON index. Verify the parts, concatenate in order, verify the whole
ciphertext, decrypt, then verify the ZIP. Exact commands are in backups/README.md.
Keep both parts, index and checksum files together; the existing passphrase applies.

Update this handoff, `PROJECT_STATE.json` and the recovery archive when the milestone changes. A running cloud process is not a persistent checkpoint.

The durable translation checkpoint is the Git tag `minigame-guide-alpha`. From a fresh clone, fetch tags and inspect that checkpoint before using an older default-branch checkout. Preserve local changes before switching revisions.
