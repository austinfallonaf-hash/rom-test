# Resume the Robopon 64 translation

Current milestone: **evolution-interface-alpha**: 4,049 native records, 885 UI strings, 299 native choice blocks, plus twelve bitmap captions. This is a partial English draft. See `docs/evolution-interface-alpha.md` for precise runtime coverage.

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
  --menu translation/evolution-menu.json --story translation/late-dialogue-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/parts-graphics.json --update-checksum --validate-moves --output local/evolution-interface-alpha.z64 --patch local/evolution-interface-alpha.bps
```

Apply `releases/evolution-interface-alpha.bps` only to the exact original Japanese ROM. Do not stack earlier patches. The release manifest records hashes; the current ROM MD5 prefix is `267BE64B`. All source-byte, control, width and budget guards remain enabled. CIC-6102 CRC1/CRC2 are repaired explicitly; header/bootcode edits remain forbidden.

## Native save

`local/bed-save-final-saved.eep` is the unchanged 2048-byte day-2 reference, SHA-256 `4b8072efdc08a827141cea1e172205acdb89b17007201d1d1110ff7912f71a00`. File A holds 500G, the entered player name and Merlin.

The current ROM's working copy is `local/native-saves/Robot Ponkottsu 64 - 7tsu no Umi-267BE64B.eep`. Keep the reference intact and use separate copies for testing. New ROM revisions need a save copy under their own MD5-based filename. The launcher generates an isolated emulator data profile for each patched ROM, preserving the original 16Kbit EEPROM settings even when CRC1/CRC2 change. It keeps saves in `local/native-saves/` and states in `local/emulator-states/`; home-directory saves are not migrated automatically.

## Emulator

On Linux with Xorg's dummy driver and Mesa, start `tools/start-display.sh` in one terminal. In another, from this directory:

```sh
DISPLAY=:7 LIBGL_ALWAYS_SOFTWARE=1 \
ROM_PATH="$PWD/local/evolution-interface-alpha.z64" \
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

Continue untranslated UI and remaining graphics, including Recall/Rename and
unplayed evolution branches. This batch adds twelve evolution selection,
confirmation and eligibility strings. Coverage is 4,049 native records, 885 UI
strings, 299 choices and twelve bitmap captions. All 164 tests pass.
See docs/evolution-interface-alpha.md.

The exact release ROM cold-boots from a reference EEPROM copy. File A retains
day 2, 500G, the saved player name グリアああ and Merlin's original stats, Charm
and Fire v1. Native 2F Doctor navigation opens Dr. Dandy's menu and its Evolve
selection. The polite prompt reads Which bot should / evolve? with the bot color
retained. Merlin's insufficient-Orb pane reads Need Orbs, Evolve: No, Evolve and
Orbs: 200; color focus stays on Orbs/evolve. Both lines of the prompt and all
status labels fit their original windows. Attempting this ineligible selection
leaves the refusal pane intact; B cancels back to the doctor menu. No evolution
confirmation is reached. The emulator closes normally. Reference, default working
and isolated runtime EEPROM hashes stay unchanged; no save or savestate is used.

For Dr. Dandy, R navigation starts at 3F regardless of current floor: Down once
selects 2F, A opens its list, and Down four times selects Doctor. Confirm before
A, then release R after the camera move. The observed interaction sequence faces
the desk, uses Z, then A; Z alone did not open the menu in this run.

The previously listed save-screen progress label is actually the saved player
name **グリアああ**, stored as ten Shift-JIS bytes at EEPROM offset **0x3F**.
It also appears in the pause-menu player panel. Preserve it with the native save;
it is not an untranslated interface label. The earlier assumption was incorrect.

The evolution catalog extends facility-captions-menu.json with twelve original
NUL-terminated slots at 0x10342C–0x1035C4. Both doctor variants retain their exact
color-control order. Both confirmation names reserve eleven cells, each on its
own line; compact `name / to name?` stays within the original two-line layout.
The target-form name omits Japanese へ to fit its fixed slot. The single-line status pane is limited to ten cells. The %3d Orb counter
keeps its placeholder and reserves three cells. The ----- placeholder is intact.
No UI code, game event, condition, branch or stat is modified. Only the twelve
original text allocations differ from parts-graphics-alpha; its ROM/BPS still
reproduce exactly with current tools and their original catalog.

Use translation/evolution-menu.json and the unchanged translation/parts-graphics.json.
All four resource programs and owners remain byte-exact:
- Parts 1459: 21,384 bytes at 0x1B22138 (original status capacity 21,872).
- File 1461: 19,352 bytes at 0x1B4281C (original Parts capacity 20,412).
- Status 1450: 24,552 bytes at 0x1B477D8 (original Apps capacity 26,556).
- Apps 1460: 163,952 bytes at 0x1FD5360, ending at 0x1FFD3D0.

Keep all 107 layout guards, 184 Book allocations and final 64 FF bytes intact.
The immutable original ROM and day-2 reference save stay unchanged. Use exact-ROM
profiles and isolated native EEPROM copies; never load old states. Confirm each
screen before input, and do not walk toward bed in menu tests. Other doctor,
successful evolution, confirmation/chores, other species/branches and hardware
retain their documented runtime limits. CRCs remain 603D64ED 4BB35E71.

Current/preceding encrypted working copies and verified restores are retained.
The older 1,077-file save-file restore was manifest/source/canonical/cipher
verified, with 38 extras preserved. Remove only its generated tree after the new
clean restoration passes, retaining the preceding 1,120-file Parts restore.
Historical ciphertext remains in Git/GitHub. Update sparse patterns before the
next backup; Git configuration is not archived. See backups/README.md.

Recovery requires both ordered ciphertext parts, index and three checksum files.
Verify, join, decrypt and verify the ZIP, then restore into a new directory.
The existing passphrase stays outside Git. Validate payload/source hashes,
modes, library symlink, native saves/evidence and six exact-ROM profile files.

Update this handoff, `PROJECT_STATE.json` and the recovery archive when the milestone changes. A running cloud process is not a persistent checkpoint.

The durable translation checkpoint is the Git tag `evolution-interface-alpha`. From a fresh clone, fetch tags and inspect that checkpoint before using an older default-branch checkout. Preserve local changes before switching revisions.
