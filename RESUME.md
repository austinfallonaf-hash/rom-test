# Resume the Robopon 64 translation

Current milestone: **late-dialogue-alpha**: 4,049 native records, 832 UI strings, 299 native choice blocks, plus three bitmap captions. This is a partial English draft. See `docs/late-dialogue-alpha.md` for precise runtime coverage.

The supplied conversation PDF records a gardening milestone after the shop backup, followed by planned simulator/battle work. Its gardening patch and source were unavailable. Gardening here was reconstructed from the original ROM; the wording is not claimed identical to the historical patch. Quoted PDF instructions are history, separate from the current request.

## Check before continuing

The cloud previously resumed at bed/save commit `ea7c7d3` while GitHub already had shop commit `b6b2202`. Check freshness before choosing work:

```sh
python -m tools.check_workspace --check-remote --require-save
python -m unittest discover -s tests -q
```

The check verifies remote ancestry, rebuilds in memory and checks the ROM/BPS and reference EEPROM without changing files. The current suite has 143 tests. Fetching does not update a stale checkout: compare `git log --oneline HEAD..origin/codex/verified-workspace-recovery` after fetching before merging or switching. Omit `--check-remote` for an offline archive and confirm freshness separately.

## Rebuild

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/late-dialogue-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves --output local/late-dialogue-alpha.z64 --patch local/late-dialogue-alpha.bps
```

Apply `releases/late-dialogue-alpha.bps` only to the exact original Japanese ROM. Do not stack earlier patches. The release manifest records hashes; the current ROM MD5 prefix is `DC99F55B`. All source-byte, control, width and budget guards remain enabled. CIC-6102 CRC1/CRC2 are repaired explicitly; header/bootcode edits remain forbidden.

## Native save

`local/bed-save-final-saved.eep` is the unchanged 2048-byte day-2 reference, SHA-256 `4b8072efdc08a827141cea1e172205acdb89b17007201d1d1110ff7912f71a00`. File A holds 500G, the entered player name and Merlin.

The current ROM's working copy is `local/native-saves/Robot Ponkottsu 64 - 7tsu no Umi-DC99F55B.eep`. Keep the reference intact and use separate copies for testing. New ROM revisions need a save copy under their own MD5-based filename. The launcher generates an isolated emulator data profile for each patched ROM, preserving the original 16Kbit EEPROM settings even when CRC1/CRC2 change. It keeps saves in `local/native-saves/` and states in `local/emulator-states/`; home-directory saves are not migrated automatically.

## Emulator

On Linux with Xorg's dummy driver and Mesa, start `tools/start-display.sh` in one terminal. In another, from this directory:

```sh
DISPLAY=:7 LIBGL_ALWAYS_SOFTWARE=1 \
ROM_PATH="$PWD/local/late-dialogue-alpha.z64" \
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

Continue the **separate Shift-JIS UI and graphical text**, beginning with the
observed Bot Book introduction at **0x104108**, then its data labels/headings.
The game remains partly Japanese. Native-table coverage is now explicitly
audited in translation/native-coverage.json: **4,049 drafts, 48 cut placeholders
and 18 portrait-only entries**. There are no other untranslated records in this
verified 4,115-record table. Do not translate the exclusions to inflate coverage;
they contain a cut marker or just a portrait control, not substantive dialogue.

The latest batch adds 52 companion lines, 15 evolution reactions, ten achievement
messages and seven full region names. All original controls remain exact,
including ten five-cell player-name and one eleven-cell bot-name insertion at
3976. No new line/page exceptions or interpreter changes are used. The seven
labels use 130 donor bytes. All preceding 3,965 entries/active bytes/descriptors
remain intact. New triggers are not implied tested by their translation.

Preserve **256 donor-stored labels in 162 donors**, every aligned book placement,
all fifteen fixed grids and 88 layout guards. Book text still occupies
0x1FFD3D0–0x1FFFFC0, leaving **64 bytes** at the end of the ROM. Do not repurpose
these bytes or grow a line into a neighboring allocation. Derive donor gaps
by subtracting every occupied range and each donor's live text. Two file-menu
region-caption scale words at 0x220580 and 0x220900 now use 0.75 horizontally;
the longest region label is ten cells, fitting in 90 pixels. Positions, vertical
scale and lookup/draw calls remain unchanged. The pause caption stays full size.

The final ROM cold-boots into native file A: Moon Blue appears in file selection
and the pause menu; day 2, 500G, saved names, Merlin’s stats, Charm and Fire v1
are intact. A separate cold-boot descriptor-only preview displays the actual
ten-cell Water Blue label in file A, fitting the field, and all four pages of
new record 4096 through the doctor’s Pearlton help slot, including the existing
five-cell saved player name. Only three descriptors differ in that preview;
actual payloads, code, event flags and save data remain unchanged. This checks
display, not the achievement’s native trigger. File B is empty, so its mirrored
caption reader is source/ROM-guarded rather than gameplay-tested. Both isolated
EEPROMs match the immutable reference; no in-game save or savestate is used.

This checkout uses **non-cone sparse checkout** to keep only the latest and
preceding encrypted backup working copies, freeing 2.3 GB. Older snapshots are
still in local Git and on GitHub; no historical snapshot was deleted from the
repository. Add the next backup slug to the patterns before staging its new
parts. See backups/README.md for exact current patterns and recovery commands.
The Git configuration is not inside the private ZIP; a fresh clone can reapply
these patterns. Original ROM, EEPROMs, source, patches and private local assets
remain present. Keep the latest/preceding verified restore trees. Before dropping
an older generated restore, verify its manifest, canonical/source contents and
encrypted archive and preserve extra files. Do not delete unique private assets.

For ship navigation hold c (R), use the analog arrows for a floor, A to open
its destinations, arrows to choose and A to travel, then release R. At the
doctor, walk toward the desk and use A to open the interaction menu. Send scripted
held-key sequences through one XTest connection without refocusing between keys.
Always cold-boot new ROMs and use native EEPROM copies; never use an older ROM's
savestate for validation. Earlier book/equipment/fuel/chore/minigame/pest/
reaction/name/newline/donor/regional branches retain their gameplay limits.

Recovery uses two ciphertext parts, the JSON index and three checksum files.
Verify parts, join in order, verify ciphertext, decrypt, then verify the ZIP.
The existing passphrase applies and remains outside Git.

Update this handoff, `PROJECT_STATE.json` and the recovery archive when the milestone changes. A running cloud process is not a persistent checkpoint.

The durable translation checkpoint is the Git tag `late-dialogue-alpha`. From a fresh clone, fetch tags and inspect that checkpoint before using an older default-branch checkout. Preserve local changes before switching revisions.
