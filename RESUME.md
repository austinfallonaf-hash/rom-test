# Resume the Robopon 64 translation

Current milestone: **facility-captions-alpha**: 4,049 native records, 873 UI strings, 299 native choice blocks, plus three bitmap captions. This is a partial English draft. See `docs/facility-captions-alpha.md` for precise runtime coverage.

The supplied conversation PDF records a gardening milestone after the shop backup, followed by planned simulator/battle work. Its gardening patch and source were unavailable. Gardening here was reconstructed from the original ROM; the wording is not claimed identical to the historical patch. Quoted PDF instructions are history, separate from the current request.

## Check before continuing

The cloud previously resumed at bed/save commit `ea7c7d3` while GitHub already had shop commit `b6b2202`. Check freshness before choosing work:

```sh
python -m tools.check_workspace --check-remote --require-save
python -m unittest discover -s tests -q
```

The check verifies remote ancestry, rebuilds in memory and checks the ROM/BPS and reference EEPROM without changing files. The current suite has 150 tests. Fetching does not update a stale checkout: compare `git log --oneline HEAD..origin/codex/verified-workspace-recovery` after fetching before merging or switching. Omit `--check-remote` for an offline archive and confirm freshness separately.

## Rebuild

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/facility-captions-menu.json --story translation/late-dialogue-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves --output local/facility-captions-alpha.z64 --patch local/facility-captions-alpha.bps
```

Apply `releases/facility-captions-alpha.bps` only to the exact original Japanese ROM. Do not stack earlier patches. The release manifest records hashes; the current ROM MD5 prefix is `AD3B8484`. All source-byte, control, width and budget guards remain enabled. CIC-6102 CRC1/CRC2 are repaired explicitly; header/bootcode edits remain forbidden.

## Native save

`local/bed-save-final-saved.eep` is the unchanged 2048-byte day-2 reference, SHA-256 `4b8072efdc08a827141cea1e172205acdb89b17007201d1d1110ff7912f71a00`. File A holds 500G, the entered player name and Merlin.

The current ROM's working copy is `local/native-saves/Robot Ponkottsu 64 - 7tsu no Umi-AD3B8484.eep`. Keep the reference intact and use separate copies for testing. New ROM revisions need a save copy under their own MD5-based filename. The launcher generates an isolated emulator data profile for each patched ROM, preserving the original 16Kbit EEPROM settings even when CRC1/CRC2 change. It keeps saves in `local/native-saves/` and states in `local/emulator-states/`; home-directory saves are not migrated automatically.

## Emulator

On Linux with Xorg's dummy driver and Mesa, start `tools/start-display.sh` in one terminal. In another, from this directory:

```sh
DISPLAY=:7 LIBGL_ALWAYS_SOFTWARE=1 \
ROM_PATH="$PWD/local/facility-captions-alpha.z64" \
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

Investigate the **bot-status hunger/stress/trait graphics** and a compact
replacement or overlay strategy. Current RAW2 artwork and book allocations leave
only **64 bytes** at the end of the ROM. Inspect source/cache/resource ownership
before choosing storage. Do not overwrite book text or assume more free tail space.
Other UI, graphics and native gameplay branches remain unfinished.

The current batch adds seven floating facility captions: Stars, Store, GB Link,
Btl Sim, Helm, Pots and Bed. These match the existing navigation labels. Store
means bot storage; its short source slot cannot hold the full Storage label.
All eight facility captions, including Bot Book, now have drafts. They use the
existing ASCII centering code; no font or game-code instruction changes occur.
A build guard now requires that exact reader for any facility-caption subset,
including subsets without Bot Book. All 150 tests pass.

The exact release ROM cold-boots into native file A with day 2, 500G,
the entered player name and Merlin’s original stats, Charm and Fire v1 intact.
R navigation visits all seven newly translated facilities: Bed, Pots, Helm,
GB Link, Btl Sim, Store and Stars. Each floating caption appears centered inside
its original plate. The unchanged Bot Book caption is also observed on this build.
No facility is activated for testing these captions. The immutable reference,
default working and isolated runtime EEPROMs retain their original hash. No
in-game save or savestate load/create is used.

Keep all **873 UI strings, 4,049 native records, 256 donor labels in 162 donors,
184 book allocations, fifteen grids, 66 native exclusions and 107 layout guards**.
Only seven original source slots and CRC1/CRC2 differ from book-interface-alpha.
The entire native table/pool, bitmap data and previous 866 UI strings stay exact.
Source captions lie within checksum coverage; the repaired CIC-6102 header is
**79430F32 1567A7B8**. Each new ROM MD5 needs its own EEPROM copy and profile.
The native day-2 reference is immutable. Saved Japanese names stay save data.

Non-cone sparse checkout retains current/preceding encrypted working copies;
older ciphertext remains in local Git and on GitHub. Add the next backup slug
before staging; backups/README.md gives the current patterns and retrieval
commands. Keep current/preceding verified restores. The older 933-file restore
was manifest/source/canonical/encrypted-archive checked and 34 extras preserved
before removing its generated tree. The preceding 964-file book-interface restore
remains beside this checkpoint’s new restore. Do not remove unique private assets.

Navigate with one XTest connection while R is held; refocusing between held keys
can interfere with menus. Return from a profile with B three times, waiting for
transitions before R. R opens floors, A opens destinations, arrows select, A
travels, then release R and wait. Capture facility captions without activating
the facility. Always cold-boot exact new ROMs and use isolated native EEPROMs;
never load older-ROM states. Earlier facility-operation/native-branch limits remain.

Recovery uses two ciphertext parts, the JSON index and three checksum files.
Verify parts, join in order, verify ciphertext, decrypt, then verify the ZIP.
The existing passphrase stays outside Git.

Update this handoff, `PROJECT_STATE.json` and the recovery archive when the milestone changes. A running cloud process is not a persistent checkpoint.

The durable translation checkpoint is the Git tag `facility-captions-alpha`. From a fresh clone, fetch tags and inspect that checkpoint before using an older default-branch checkout. Preserve local changes before switching revisions.
