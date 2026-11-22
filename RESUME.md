# Resume the Robopon 64 translation

Current milestone: **recall-rename-alpha**: 4,049 native records, 891 UI strings, 299 native choice blocks, plus twelve bitmap captions. This is a partial English draft. See `docs/recall-rename-alpha.md` for precise runtime coverage.

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
  --menu translation/recall-rename-menu.json --story translation/late-dialogue-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/parts-graphics.json --update-checksum --validate-moves --output local/recall-rename-alpha.z64 --patch local/recall-rename-alpha.bps
```

Apply `releases/recall-rename-alpha.bps` only to the exact original Japanese ROM. Do not stack earlier patches. The release manifest records hashes; the current ROM MD5 prefix is `220E75A3`. All source-byte, control, width and budget guards remain enabled. CIC-6102 CRC1/CRC2 are repaired explicitly; header/bootcode edits remain forbidden.

## Native save

`local/bed-save-final-saved.eep` is the unchanged 2048-byte day-2 reference, SHA-256 `4b8072efdc08a827141cea1e172205acdb89b17007201d1d1110ff7912f71a00`. File A holds 500G, the entered player name and Merlin.

The current ROM's working copy is `local/native-saves/Robot Ponkottsu 64 - 7tsu no Umi-220E75A3.eep`. Keep the reference intact and use separate copies for testing. New ROM revisions need a save copy under their own MD5-based filename. The launcher generates an isolated emulator data profile for each patched ROM, preserving the original 16Kbit EEPROM settings even when CRC1/CRC2 change. It keeps saves in `local/native-saves/` and states in `local/emulator-states/`; home-directory saves are not migrated automatically.

## Emulator

On Linux with Xorg's dummy driver and Mesa, start `tools/start-display.sh` in one terminal. In another, from this directory:

```sh
DISPLAY=:7 LIBGL_ALWAYS_SOFTWARE=1 \
ROM_PATH="$PWD/local/recall-rename-alpha.z64" \
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

Continue remaining untranslated interaction UI, including name-entry labels,
ship-facility and training prompts. This batch adds six Doctor Recall/Rename
strings. Coverage is 4,049 native records, 891 UI strings, 299 choices and twelve
bitmap captions. All 164 tests pass. See docs/recall-rename-alpha.md.

The exact release ROM cold-boots from an isolated reference EEPROM copy.
File A retains day 2, 500G, player name グリアああ and Merlin's original stats,
Charm and Fire v1. Doctor navigation opens the polite doctor's menu. Recall
shows Call Collector? with Collector green; No returns to the doctor menu.
Rename shows Which bot should / be renamed? with bot yellow. Selecting Merlin
shows the saved Japanese nickname above Rename this bot?, with the name yellow.
Both prompts fit their original two-line windows. No returns to bot selection;
B then cancels back to the doctor menu. The name editor is not opened and Collector
is not summoned. Normal exit leaves reference, default and isolated runtime
EEPROM hashes unchanged. No in-game save or savestate is used.

The cumulative recall-rename-menu.json preserves all 885 previous entries and
adds six original slots: 0x1033D8/0x103400 (Recall), 0x10380C/0x103844 (Rename
selection), 0x10387C/0x1038A8 (name confirmation). The native NPC label is already
Collector (record 2867), so Recall asks Call Collector? with its green name.
Both doctor variants preserve color controls and newline counts. Rename selection
and confirmation retain two lines; formatted names reserve eleven cells. The
harvest naming question at 0x1041B0 was already translated and remains untouched.
Only the six original text allocations differ from evolution-interface-alpha;
its ROM/BPS reproduce exactly with current tools and the prior menu catalog.

Saved player name グリアああ remains ten Shift-JIS bytes at EEPROM 0x3F. It is
not a progress heading. Existing bot nicknames are also preserved. No game event,
branch, item, stat, name-input code or save operation is changed. Other doctor,
Collector summon/service, committed rename/name entry, long-name cases and
successful evolution retain their documented runtime limits.

Doctor route: after profile, cancel back to ship and wait for the world screen.
R navigation always starts at 3F: Down once selects 2F, A opens the list, Down four
times selects Doctor, A moves the camera, then release R. Face the desk and use
Z then A as in the observed route. Confirm the actual menu before further input.
Do not walk toward bed or send unverified Up/A sequences during menu tests.

Use translation/recall-rename-menu.json and unchanged translation/parts-graphics.json.
Keep all four resource programs and relocated owners, 107 layout guards, all 184
Book allocations and final 64 FF bytes exact. Native-source slots/donors/grids/
exclusions, 299 choices, code/checksums and original ROM remain unchanged. There
is no new ROM-tail space. CRCs remain 603D64ED 4BB35E71. Use exact-ROM profiles
and separate reference EEPROM copies; never load earlier-ROM states.

Workspace retention independently reproduced 39 older generated ROMs from their
manifest-verified committed BPS files and the immutable original, then removed
only those exact working copies, freeing 1,308,622,848 bytes. Original, current/
preceding playable ROMs and unmatched prototypes remain. All shipped patches and
encrypted history remain in Git/GitHub. To recreate an older build, use Flips:

```sh
local/flips-src/Flips-master/flips --apply releases/OLD-MILESTONE.bps \
  local/original.z64 local/restored-historical.z64
```

Do not assume an old local filename still exists. The recovery archive includes
the original/current ROMs and cumulative historical patches; it intentionally
excludes duplicate historical ROM builds. local/recall-rename-evidence contains
the generated-ROM ledger with every source/target/patch hash and exact rebuild.

Current/preceding encrypted working copies and verified restores remain. The
older 1,120-file Parts restore was manifest/source/canonical/cipher verified,
with 38 generated extras preserved. Remove only its generated tree after the new
clean restore passes, retaining the preceding 1,156-file evolution restore.
Historical cipher working copies may be sparse-omitted only after Git/remote
verification. Update patterns before staging a new backup; Git configuration is
not archived. See backups/README.md.

Recovery needs both ordered ciphertext parts, JSON index and three checksum
files. Verify, join, decrypt, verify ZIP, then restore into a new directory. The
existing passphrase stays outside Git. Validate payload/source hashes, executable
modes, library symlink, native saves/evidence and six exact-ROM profile files.

Update this handoff, `PROJECT_STATE.json` and the recovery archive when the milestone changes. A running cloud process is not a persistent checkpoint.

The durable translation checkpoint is the Git tag `recall-rename-alpha`. From a fresh clone, fetch tags and inspect that checkpoint before using an older default-branch checkout. Preserve local changes before switching revisions.
