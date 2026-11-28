# Resume the Robopon 64 translation

Current milestone: **ship-actions-alpha**: 4,049 native records, 922 UI strings, 299 native choice blocks, plus twelve bitmap captions. This is a partial English draft. See `docs/ship-actions-alpha.md` for precise runtime coverage.

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
  --menu translation/ship-actions-menu.json --story translation/late-dialogue-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/parts-graphics.json --update-checksum --validate-moves --output local/ship-actions-alpha.z64 --patch local/ship-actions-alpha.bps
```

Apply `releases/ship-actions-alpha.bps` only to the exact original Japanese ROM. Do not stack earlier patches. The release manifest records hashes; the current ROM MD5 prefix is `A7CF0A90`. All source-byte, control, width and budget guards remain enabled. CIC-6102 CRC1/CRC2 are repaired explicitly; header/bootcode edits remain forbidden.

## Native save

`local/bed-save-final-saved.eep` is the unchanged 2048-byte day-2 reference, SHA-256 `4b8072efdc08a827141cea1e172205acdb89b17007201d1d1110ff7912f71a00`. File A holds 500G, the entered player name and Merlin.

The current ROM's working copy is `local/native-saves/Robot Ponkottsu 64 - 7tsu no Umi-A7CF0A90.eep`. Keep the reference intact and use separate copies for testing. New ROM revisions need a save copy under their own MD5-based filename. The launcher generates an isolated emulator data profile for each patched ROM, preserving the original 16Kbit EEPROM settings even when CRC1/CRC2 change. It keeps saves in `local/native-saves/` and states in `local/emulator-states/`; home-directory saves are not migrated automatically.

## Emulator

On Linux with Xorg's dummy driver and Mesa, start `tools/start-display.sh` in one terminal. In another, from this directory:

```sh
DISPLAY=:7 LIBGL_ALWAYS_SOFTWARE=1 \
ROM_PATH="$PWD/local/ship-actions-alpha.z64" \
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

Continue untranslated training/chore results at 0x103C18-0x103F58, then remaining
name-entry/interaction UI. The overall-power result at 0x103EF8 contains the
unsupported control \O333; understand it before editing. Do not discard controls.
Use translation/ship-actions-menu.json and the unchanged graphics catalog.
This batch adds 31 original slots; no relocation or code changes. The 891 earlier
UI entries and every byte outside the new text allocations remain identical to
recall-rename-alpha. All 164 tests pass; see docs/ship-actions-alpha.md.

The exact release ROM cold-boots from an isolated reference EEPROM copy.
File A retains day 2, 500G, player name グリアああ and Merlin's original stats,
Charm and Fire v1. Game Boy Link displays Link with a GB? on one line. Star
Collection displays View your Star / Collection? on two lines. Bot storage
shows Deposit or / withdraw bots? on two lines. All three prompts fit the
original windows and keep existing Yes/No choices. Selecting No returns to
the corresponding ship facility each time. The pause Bots check returns to
the bot profile; assignment/training setup and the other 28 new slots remain
build-only. No task is assigned, training started, transfer performed or bot
stored. Normal exit leaves reference/default/runtime EEPROM hashes unchanged;
no in-game save or savestate is used.

Private local/ship-actions-evidence holds screenshots, completed emulator log,
source/target text allocations, save identity and portable verify_actual.py. Its
coverage.json distinguishes observed offsets from build-only entries. No successful
training/chore result, sailing, transfer, ghost battle, deposit/withdrawal or other
unplayed gameplay branch is implied by a prompt check. Saved player name グリアああ
and Merlin nickname remain existing save data.

Keep all four resource programs/owners, 107 layout guards, 184 Book allocations
and final 64 FF bytes exact. No new ROM-tail space is available. CRC1/CRC2 remain
603D64ED 4BB35E71. Historical generated ROMs were removed only after manifest/hash
and independent BPS reproduction; recreate an older one with its shipped BPS and
original when needed. Original/current/preceding and unmatched prototypes remain.

Recreate an older generated ROM from the exact original and its cumulative patch:

```sh
local/flips-src/Flips-master/flips --apply releases/OLD-MILESTONE.bps \
  local/original.z64 local/restored-historical.z64
```

Check its target hash against the corresponding release manifest before use.

Use separate reference EEPROM copies and exact-ROM profiles. Confirm each screen
before dependent input. R ship navigation always starts at 3F: Down once opens
2F, whose list is Helm, GB Link, Btl Sim, Book, Doctor. 1F has Store and Stars.
Never send unverified Up/A near the bed. Other doctor, Collector service,
committed rename/name entry and successful evolution remain unplayed.

The private ZIP includes original/current ROMs, historical patches, emulator,
source and evidence. Its encrypted parts, index and all three checksum files
must verify before restoration into a new directory. The existing passphrase
stays outside Git. Check manifest/source hashes, modes, library symlink, saves,
evidence and all six regenerated exact-ROM profile files.

Current/preceding encrypted snapshots and verified restore trees are retained.
The older 1,156-file evolution restore is manifest/source/canonical/cipher checked;
38 generated extras are preserved before cleanup, which follows the new clean
restore. Historical ciphers remain in Git/GitHub. Sparse patterns keep Recall
and ship-actions snapshots; backups/README.md records the exact commands.

Update this handoff and PROJECT_STATE.json after each verified checkpoint.
