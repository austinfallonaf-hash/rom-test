# Resume the Robopon 64 translation

Current milestone: **book-interface-alpha**: 4,049 native records, 866 UI strings, 299 native choice blocks, plus three bitmap captions. This is a partial English draft. See `docs/book-interface-alpha.md` for precise runtime coverage.

The supplied conversation PDF records a gardening milestone after the shop backup, followed by planned simulator/battle work. Its gardening patch and source were unavailable. Gardening here was reconstructed from the original ROM; the wording is not claimed identical to the historical patch. Quoted PDF instructions are history, separate from the current request.

## Check before continuing

The cloud previously resumed at bed/save commit `ea7c7d3` while GitHub already had shop commit `b6b2202`. Check freshness before choosing work:

```sh
python -m tools.check_workspace --check-remote --require-save
python -m unittest discover -s tests -q
```

The check verifies remote ancestry, rebuilds in memory and checks the ROM/BPS and reference EEPROM without changing files. The current suite has 149 tests. Fetching does not update a stale checkout: compare `git log --oneline HEAD..origin/codex/verified-workspace-recovery` after fetching before merging or switching. Omit `--check-remote` for an offline archive and confirm freshness separately.

## Rebuild

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/book-interface-menu.json --story translation/late-dialogue-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves --output local/book-interface-alpha.z64 --patch local/book-interface-alpha.bps
```

Apply `releases/book-interface-alpha.bps` only to the exact original Japanese ROM. Do not stack earlier patches. The release manifest records hashes; the current ROM MD5 prefix is `D85FAF7B`. All source-byte, control, width and budget guards remain enabled. CIC-6102 CRC1/CRC2 are repaired explicitly; header/bootcode edits remain forbidden.

## Native save

`local/bed-save-final-saved.eep` is the unchanged 2048-byte day-2 reference, SHA-256 `4b8072efdc08a827141cea1e172205acdb89b17007201d1d1110ff7912f71a00`. File A holds 500G, the entered player name and Merlin.

The current ROM's working copy is `local/native-saves/Robot Ponkottsu 64 - 7tsu no Umi-D85FAF7B.eep`. Keep the reference intact and use separate copies for testing. New ROM revisions need a save copy under their own MD5-based filename. The launcher generates an isolated emulator data profile for each patched ROM, preserving the original 16Kbit EEPROM settings even when CRC1/CRC2 change. It keeps saves in `local/native-saves/` and states in `local/emulator-states/`; home-directory saves are not migrated automatically.

## Emulator

On Linux with Xorg's dummy driver and Mesa, start `tools/start-display.sh` in one terminal. In another, from this directory:

```sh
DISPLAY=:7 LIBGL_ALWAYS_SOFTWARE=1 \
ROM_PATH="$PWD/local/book-interface-alpha.z64" \
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

Continue the **separate UI and bitmap text**, beginning with the seven remaining
facility captions near **0xFB78E–0xFB8DE**: Stars, Storage, GB Link, Battle Sim,
Helm, Pots and Bed. Bot-status hunger/stress and trait plates need graphical
investigation. The game remains partly Japanese. Native coverage is unchanged:
4,049 drafts, 48 cut placeholders and 18 portrait-only entries; keep the exclusions.

The current batch adds 34 UI strings for the Bot Book. Console/title now read
Bot Book; classes/types follow existing terminology. Both `%03d` arguments retain
three-cell reservations. The introduction keeps three lines. Height/Weight use
six guarded horizontal-scale words at 0.75 in the three native data states;
vertical scale, positions, numeric fields and units stay exact. The console/title now use 13 additional guarded ASCII-aware centering words.
Layout now has 107 guards. All previous 832 UI strings and the entire native table/pool are exact.

The exact final ROM cold-boots into native file A, retaining day 2, 500G,
the entered player name and Merlin’s original stats, Charm and Fire v1. The Book
console caption and gold page heading display Bot Book, correctly centered inside
their plates. The three-line introduction fits. The initial undiscovered entry
displays the translated dash number/type states, Height, Weight and Logged count.
Entry 38 displays Merlin with 64 No./038, GB No./161, Caster, T:Water,
Height 120cm, Weight 130kg and the unchanged four-line biography.
The isolated runtime, default working and immutable reference EEPROMs retain the
same hash. No in-game save or savestate load/create is used.

Preserve all **256 donor labels in 162 donors**, **184 book allocations**,
fifteen fixed grids, 66 native exclusions and 107 layout guards. Book storage ends
at 0x1FFFFC0, leaving **64 bytes**. Derive donor gaps by subtracting active text
and every occupied interval; never repurpose an allocation or tail padding.
The console caption at 0xFB84E changes checksum-covered bytes; the explicit
CIC-6102 repair gives **FF5EDDAC 400FB7B6**. Each new MD5 needs its own save/profile.

Non-cone sparse checkout keeps only current/preceding encrypted working copies.
Older ciphertext remains in local Git and on GitHub. Add the next backup slug
before staging; see backups/README.md for current patterns and recovery commands.
Git configuration is not archived. Keep latest/preceding verified restore trees;
verify manifests, canonical assets, source revisions and encrypted archives and
preserve extra files before removing superseded generated copies. Do not remove
unique private assets. The older 896-file bot-book restore was verified and its
34 extras retained before cleanup; the preceding 933-file late-dialogue restore
remains alongside this checkpoint’s new restore.

For ship navigation use one XTest connection without refocusing while R is held:
hold c, Down to 2F, A, Down three times to Book, A and release R. Face/walk toward
the console with Up, then A. Wait for the introduction and use A for View. Scroll
to native entry 38 for Merlin and A for its four biography lines. Return from a
profile with B three times before navigation. Cold-boot every exact new ROM;
never use an older ROM’s state. Earlier gameplay/branch limits remain.

Recovery uses two ciphertext parts, the JSON index and three checksum files.
Verify parts, join in order, verify ciphertext, decrypt, then verify the ZIP.
The existing passphrase stays outside Git.

Update this handoff, `PROJECT_STATE.json` and the recovery archive when the milestone changes. A running cloud process is not a persistent checkpoint.

The durable translation checkpoint is the Git tag `book-interface-alpha`. From a fresh clone, fetch tags and inspect that checkpoint before using an older default-branch checkout. Preserve local changes before switching revisions.
