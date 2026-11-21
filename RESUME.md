# Resume the Robopon 64 translation

Current milestone: **bot-book-alpha**: 3,965 native records, 832 UI strings, 299 native choice blocks, plus three bitmap captions. This is a partial English draft. See `docs/bot-book-alpha.md` for precise runtime coverage.

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
  --menu translation/battle-moves-menu.json --story translation/bot-book-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves --output local/bot-book-alpha.z64 --patch local/bot-book-alpha.bps
```

Apply `releases/bot-book-alpha.bps` only to the exact original Japanese ROM. Do not stack earlier patches. The release manifest records hashes; the current ROM MD5 prefix is `6AB9FC59`. All source-byte, control, width and budget guards remain enabled. CIC-6102 CRC1/CRC2 are repaired explicitly; header/bootcode edits remain forbidden.

## Native save

`local/bed-save-final-saved.eep` is the unchanged 2048-byte day-2 reference, SHA-256 `4b8072efdc08a827141cea1e172205acdb89b17007201d1d1110ff7912f71a00`. File A holds 500G, the entered player name and Merlin.

The current ROM's working copy is `local/native-saves/Robot Ponkottsu 64 - 7tsu no Umi-6AB9FC59.eep`. Keep the reference intact and use separate copies for testing. New ROM revisions need a save copy under their own MD5-based filename. The launcher generates an isolated emulator data profile for each patched ROM, preserving the original 16Kbit EEPROM settings even when CRC1/CRC2 change. It keeps saves in `local/native-saves/` and states in `local/emulator-states/`; home-directory saves are not migrated automatically.

## Emulator

On Linux with Xorg's dummy driver and Mesa, start `tools/start-display.sh` in one terminal. In another, from this directory:

```sh
DISPLAY=:7 LIBGL_ALWAYS_SOFTWARE=1 \
ROM_PATH="$PWD/local/bot-book-alpha.z64" \
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

Continue native dialogue from **3918**; 3878–3917 were translated earlier.
Inspect the source portraits, highlights, pages, arguments and speaker variants
before writing. The 48 cut placeholders and 18 portrait-only records remain
intact. Do not translate them merely to raise the count.

The book milestone adds 184 lines, four records per biography, at 3694–3877.
`book_line` is restricted to those IDs and 1–36 printable ASCII cells. It requires
the guarded 0x109C04 half-width reader; generic labels retain sixteen-cell rules
and all fifteen earlier fixed grids remain separate. See docs/story-format.md.

Preserve all **249 donor-stored labels in 155 donors** and every eight-byte-
aligned **book_storage_offset**. Book text occupies **0x1FFD3D0–0x1FFFFC0** after
the untouched RAW2 graphic, with only **64 bytes** left at the end of the ROM.
Do not consume that padding casually or grow a line into another allocation.
The original Japanese book slots and all earlier 3,781 entries, active bytes
and descriptors remain intact. Book lines are not available as donors. For
ordinary label storage, subtract every occupied range and the donor's live text
before choosing a gap. The current donor free space is fragmented; preserve
existing placements rather than assuming its total is one usable interval.

The exact final ROM cold-boots and loads native file A with day 2, 500G,
player name, saved Japanese Merlin nickname, original stats, Charm and Fire v1.
Book entry 38 displays Merlin and all four actual biography records 3842–3845.
The record order is separate from the general name roster. A descriptor-only
preview repeats the real 36-cell line 3757 in every book-line slot; its screenshot
shows the full text in all four native detail rows. The release retains each
actual biography. Both runs use separate native EEPROM copies, unchanged from
the reference. No in-game save or savestate load/create is used. Evidence and
exact identities are in local/bot-book-evidence. Other biographies remain
build-validated; the book introduction, graphical headings and data labels
remain Japanese.

Ship navigation: hold `c` (R), use the analog arrows to choose a floor, left
Shift (A) to open destinations, arrows to choose, then A to travel. Scripted
input uses one continuous XTest connection; separate refocusing input calls
while holding R interfered with navigation. Use a cold boot and native
EEPROM copies; never use an older ROM's savestate to validate a new build.

Other book entries and earlier equipment/fuel/chore/minigame/pest/reaction/
name/newline/donor/regional branches retain their gameplay limits. Graphical
labels, Parts frames, capacity warnings, five anchored pages and VS/Transfer
Pak remain unfinished. Reference/default/runtime/preview EEPROMs remain exact;
no in-game save or savestate load/create is used for this milestone.

Recovery uses .part001 and .part002. PROJECT_STATE's backup field points to the
JSON index. Verify parts, concatenate in order, verify the full ciphertext,
decrypt, then verify the ZIP. Exact commands are in backups/README.md; keep both
parts, index and checksum files together. The existing passphrase applies.

Update this handoff, `PROJECT_STATE.json` and the recovery archive when the milestone changes. A running cloud process is not a persistent checkpoint.

The durable translation checkpoint is the Git tag `bot-book-alpha`. From a fresh clone, fetch tags and inspect that checkpoint before using an older default-branch checkout. Preserve local changes before switching revisions.
