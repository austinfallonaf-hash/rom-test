# Resume the Robopon 64 translation

Current milestone: **roulette-story-alpha**: 1,671 native records, 832 UI strings, 299 native choice blocks, plus three bitmap captions. This is a partial English draft. See `docs/roulette-story-alpha.md` for precise runtime coverage.

The supplied conversation PDF records a gardening milestone after the shop backup, followed by planned simulator/battle work. Its gardening patch and source were unavailable. Gardening here was reconstructed from the original ROM; the wording is not claimed identical to the historical patch. Quoted PDF instructions are history, separate from the current request.

## Check before continuing

The cloud previously resumed at bed/save commit `ea7c7d3` while GitHub already had shop commit `b6b2202`. Check freshness before choosing work:

```sh
python -m tools.check_workspace --check-remote --require-save
python -m unittest discover -s tests -q
```

The check verifies remote ancestry, rebuilds in memory and checks the ROM/BPS and reference EEPROM without changing files. The current suite has 115 tests. Fetching does not update a stale checkout: compare `git log --oneline HEAD..origin/codex/verified-workspace-recovery` after fetching before merging or switching. Omit `--check-remote` for an offline archive and confirm freshness separately.

## Rebuild

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/roulette-story-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves --output local/roulette-story-alpha.z64 --patch local/roulette-story-alpha.bps
```

Apply `releases/roulette-story-alpha.bps` only to the exact original Japanese ROM. Do not stack earlier patches. The release manifest records hashes; the current ROM MD5 prefix is `353AEA96`. All source-byte, control, width and budget guards remain enabled. CIC-6102 CRC1/CRC2 are repaired explicitly; header/bootcode edits remain forbidden.

## Native save

`local/bed-save-final-saved.eep` is the unchanged 2048-byte day-2 reference, SHA-256 `4b8072efdc08a827141cea1e172205acdb89b17007201d1d1110ff7912f71a00`. File A holds 500G, the entered player name and Merlin.

The current ROM's working copy is `local/native-saves/Robot Ponkottsu 64 - 7tsu no Umi-353AEA96.eep`. Keep the reference intact and use separate copies for testing. New ROM revisions need a save copy under their own MD5-based filename. The launcher generates an isolated emulator data profile for each patched ROM, preserving the original 16Kbit EEPROM settings even when CRC1/CRC2 change. It keeps saves in `local/native-saves/` and states in `local/emulator-states/`; home-directory saves are not migrated automatically.

## Emulator

On Linux with Xorg's dummy driver and Mesa, start `tools/start-display.sh` in one terminal. In another, from this directory:

```sh
DISPLAY=:7 LIBGL_ALWAYS_SOFTWARE=1 \
ROM_PATH="$PWD/local/roulette-story-alpha.z64" \
tools/emulator.sh --windowed --gfx mupen64plus-video-glide64mk2 --audio dummy \
  --input mupen64plus-input-sdl --rsp mupen64plus-rsp-hle
```

Return = Start; left Shift = A; left Control = B; arrows = stick; c = R; Escape = quit. R opens navigation: use 3F/Pots for gardening and 2F/Btl Sim for practice battles. Face the facility and walk toward it before pressing A. Wait for transitions and text to finish.

Cold-boot new builds and use native EEPROM for persistence checks. Historical
savestates belong to their exact ROMs and cannot validate this build. In particular,
`local/fire-blue-story-evidence/opening-502.st0` belongs only to the preceding
ROM MD5 `07EC747C6805124E327FC2A1872EED28`; never load it on this build. That earlier
checkpoint checked opening records 502–509. This build's new Roulette branches,
and earlier Water/Fire Blue branches including 831's page, await playthrough. The
current native-A cold boot checks the file/ship/pause displays and save contents.

## Recovery

The latest encrypted archive is identified by `PROJECT_STATE.json` and `backups/README.md`. It uses the existing recovery passphrase, kept outside Git. Verify the encrypted and decrypted checksums, then:

```sh
python tools/verify_backup.py /path/to/decrypted.zip
python -m tools.restore_backup /path/to/decrypted.zip /path/to/new-directory
```

The destination must not exist. Verification precedes extraction; executable modes and safe relative symlinks are preserved. It creates `rom-test/` within the destination. Keep the latest source checkout and compare versions before moving restored private assets into it. See `RESTORE.md`.

## Next work

Continue the alternate Roulette bank at native record 1366, regional hints and
arrival/abduction variants through 1608, then the training bank at 1609. The main
Dandy/Punch Roulette route now has a draft: pirate encounters and rematches,
Maido/Akane traps, rescue and Tree reward, arrival/abduction and Gold Blue departure.
Captain Ladder shortens to Ladder and Roulette Island to Roulette when crowded.
Tree Caramela uses Tree in inventory. The ransom demands three fragments; the
reward is called the fourth, Punch is freed, and launch energy remains 80%.
Koron's all-other-islands requirement and timing a roulette button press are
retained. Ten new cut-message placeholders remain untouched. No new layout
exception was needed; record 831's earlier exception is inherited unchanged.
Play these branches and the preceding Water/Fire Blue material. Preserve the
Dome three-versus-four-win discrepancy until checked in play and reserve a full
line for item variable 200B:0006. Graphical/roster labels, Parts frame, capacity
warnings and VS/Transfer Pak branches remain unfinished.

Update this handoff, `PROJECT_STATE.json` and the recovery archive when the milestone changes. A running cloud process is not a persistent checkpoint.

The durable translation checkpoint is the Git tag `roulette-story-alpha`. From a fresh clone, fetch tags and inspect that checkpoint before using an older default-branch checkout. Preserve local changes before switching revisions.
