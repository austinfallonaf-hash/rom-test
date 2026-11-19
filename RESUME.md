# Resume the Robopon 64 translation

Current milestone: **sunny-blue-finale-alpha**: 2,777 native records, 832 UI strings, 299 native choice blocks, plus three bitmap captions. This is a partial English draft. See `docs/sunny-blue-finale-alpha.md` for precise runtime coverage.

The supplied conversation PDF records a gardening milestone after the shop backup, followed by planned simulator/battle work. Its gardening patch and source were unavailable. Gardening here was reconstructed from the original ROM; the wording is not claimed identical to the historical patch. Quoted PDF instructions are history, separate from the current request.

## Check before continuing

The cloud previously resumed at bed/save commit `ea7c7d3` while GitHub already had shop commit `b6b2202`. Check freshness before choosing work:

```sh
python -m tools.check_workspace --check-remote --require-save
python -m unittest discover -s tests -q
```

The check verifies remote ancestry, rebuilds in memory and checks the ROM/BPS and reference EEPROM without changing files. The current suite has 117 tests. Fetching does not update a stale checkout: compare `git log --oneline HEAD..origin/codex/verified-workspace-recovery` after fetching before merging or switching. Omit `--check-remote` for an offline archive and confirm freshness separately.

## Rebuild

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/sunny-blue-finale-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves --output local/sunny-blue-finale-alpha.z64 --patch local/sunny-blue-finale-alpha.bps
```

Apply `releases/sunny-blue-finale-alpha.bps` only to the exact original Japanese ROM. Do not stack earlier patches. The release manifest records hashes; the current ROM MD5 prefix is `4FFCDEDA`. All source-byte, control, width and budget guards remain enabled. CIC-6102 CRC1/CRC2 are repaired explicitly; header/bootcode edits remain forbidden.

## Native save

`local/bed-save-final-saved.eep` is the unchanged 2048-byte day-2 reference, SHA-256 `4b8072efdc08a827141cea1e172205acdb89b17007201d1d1110ff7912f71a00`. File A holds 500G, the entered player name and Merlin.

The current ROM's working copy is `local/native-saves/Robot Ponkottsu 64 - 7tsu no Umi-4FFCDEDA.eep`. Keep the reference intact and use separate copies for testing. New ROM revisions need a save copy under their own MD5-based filename. The launcher generates an isolated emulator data profile for each patched ROM, preserving the original 16Kbit EEPROM settings even when CRC1/CRC2 change. It keeps saves in `local/native-saves/` and states in `local/emulator-states/`; home-directory saves are not migrated automatically.

## Emulator

On Linux with Xorg's dummy driver and Mesa, start `tools/start-display.sh` in one terminal. In another, from this directory:

```sh
DISPLAY=:7 LIBGL_ALWAYS_SOFTWARE=1 \
ROM_PATH="$PWD/local/sunny-blue-finale-alpha.z64" \
tools/emulator.sh --windowed --gfx mupen64plus-video-glide64mk2 --audio dummy \
  --input mupen64plus-input-sdl --rsp mupen64plus-rsp-hle
```

Return = Start; left Shift = A; left Control = B; arrows = stick; c = R; Escape = quit. R opens navigation: use 3F/Pots for gardening and 2F/Btl Sim for practice battles. Face the facility and walk toward it before pressing A. Wait for transitions and text to finish.

Cold-boot new builds and use native EEPROM for persistence checks. Historical
savestates belong to their exact ROMs and cannot validate this build. In particular,
`local/fire-blue-story-evidence/opening-502.st0` belongs only to the preceding
ROM MD5 `07EC747C6805124E327FC2A1872EED28`; never load it on this build. That earlier
checkpoint checked opening records 502–509. This build's new Sunny Blue finale branches,
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

Continue alternate Sunny Blue/rematch text at native record 2502. The main
finale/escape and approach bank 2448–2501 now has 47 English records, with seven
cut-message placeholders untouched (2455, 2457–2461, 2471). All preceding 2,730
entries are identical. No new inventory labels were needed; Sun was already
translated. The acquisition at 2477 now uses that same compact form.

Record 2490's cast list cannot fit Punch, Dandy and Mikachi on one 16-cell line.
Its layout_pages_before: [36] adds one page before the original Mikachi name
color 2003:0001, preserving all source commands and arguments. The codec now
allows an explicit unpaged name-color anchor as well as a portrait. Other
colors, resets, already-paged anchors, altered commands, arbitrary pages and
record growth are rejected. Tests cover these guards. No additional newline
opt-in was used. Inspect this page and earlier exceptions 831/2041/2226 in play.

The story retains Zero's mechanical immortality, the hero's finite-life argument,
Zero's restored humanity, the Sun reward, Caramel's first-Robopon origin and
repeated eye-reading joke, the unspoken wish/future reveal and escape. Pages and
portrait/color/name order stay intact; long ellipsis runs are condensed.

Play the main finale, approach choices and preceding rematches. Earlier
Land/Gold Blue, Roulette and Water/Fire Blue scenes await playthrough. Preserve
the Land/Gold source-location and Gria/entered-name discrepancies documented in
the Land Blue notes. Keep the Dome three-versus-four-win discrepancy and reserve
a full line for item variable 200B:0006. Graphical/roster labels, Parts frame,
capacity warnings and VS/Transfer Pak branches remain unfinished.

Update this handoff, `PROJECT_STATE.json` and the recovery archive when the milestone changes. A running cloud process is not a persistent checkpoint.

The durable translation checkpoint is the Git tag `sunny-blue-finale-alpha`. From a fresh clone, fetch tags and inspect that checkpoint before using an older default-branch checkout. Preserve local changes before switching revisions.
