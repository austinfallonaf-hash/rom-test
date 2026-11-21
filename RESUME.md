# Resume the Robopon 64 translation

Current milestone: **status-graphics-alpha**: 4,049 native records, 873 UI strings, 299 native choice blocks, plus eight bitmap captions. This is a partial English draft. See `docs/status-graphics-alpha.md` for precise runtime coverage.

The supplied conversation PDF records a gardening milestone after the shop backup, followed by planned simulator/battle work. Its gardening patch and source were unavailable. Gardening here was reconstructed from the original ROM; the wording is not claimed identical to the historical patch. Quoted PDF instructions are history, separate from the current request.

## Check before continuing

The cloud previously resumed at bed/save commit `ea7c7d3` while GitHub already had shop commit `b6b2202`. Check freshness before choosing work:

```sh
python -m tools.check_workspace --check-remote --require-save
python -m unittest discover -s tests -q
```

The check verifies remote ancestry, rebuilds in memory and checks the ROM/BPS and reference EEPROM without changing files. The current suite has 158 tests. Fetching does not update a stale checkout: compare `git log --oneline HEAD..origin/codex/verified-workspace-recovery` after fetching before merging or switching. Omit `--check-remote` for an offline archive and confirm freshness separately.

## Rebuild

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/facility-captions-menu.json --story translation/late-dialogue-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/status-graphics.json --update-checksum --validate-moves --output local/status-graphics-alpha.z64 --patch local/status-graphics-alpha.bps
```

Apply `releases/status-graphics-alpha.bps` only to the exact original Japanese ROM. Do not stack earlier patches. The release manifest records hashes; the current ROM MD5 prefix is `5DF41F0A`. All source-byte, control, width and budget guards remain enabled. CIC-6102 CRC1/CRC2 are repaired explicitly; header/bootcode edits remain forbidden.

## Native save

`local/bed-save-final-saved.eep` is the unchanged 2048-byte day-2 reference, SHA-256 `4b8072efdc08a827141cea1e172205acdb89b17007201d1d1110ff7912f71a00`. File A holds 500G, the entered player name and Merlin.

The current ROM's working copy is `local/native-saves/Robot Ponkottsu 64 - 7tsu no Umi-5DF41F0A.eep`. Keep the reference intact and use separate copies for testing. New ROM revisions need a save copy under their own MD5-based filename. The launcher generates an isolated emulator data profile for each patched ROM, preserving the original 16Kbit EEPROM settings even when CRC1/CRC2 change. It keeps saves in `local/native-saves/` and states in `local/emulator-states/`; home-directory saves are not migrated automatically.

## Emulator

On Linux with Xorg's dummy driver and Mesa, start `tools/start-display.sh` in one terminal. In another, from this directory:

```sh
DISPLAY=:7 LIBGL_ALWAYS_SOFTWARE=1 \
ROM_PATH="$PWD/local/status-graphics-alpha.z64" \
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

Continue remaining bitmap headings, starting with **save-file A/B plates and
Parts/evolution frames**. Other Japanese UI/graphics and gameplay branches remain.
The latest batch adds five profile captions: HUNGER, STRESS, TRAITS, PARTS, APPS.
Counts remain 4,049 native records, 873 UI strings and 299 choices; bitmap captions
reach eight in two resources. All 158 tests pass. See docs/status-graphics-alpha.md.

The exact release ROM cold-boots from a fresh reference EEPROM into file A,
day 2, 500G, the entered player name and Merlin. HUNGER, STRESS, TRAITS, PARTS
and APPS appear in their native profile plates, retaining Merlin's stats, Charm
and Fire v1. The Apps equipment screen retains EQUIPPED, SPARE APPS and MOVES.
Both complete 163,840-byte native image-cache outputs match their generated
images exactly. Native navigation reaches Bot Book; entry 38 retains Merlin,
64 No.038, GB No.161, Height 120 cm, Weight 130 kg and its four English biography
lines. The emulator then closes normally. Reference, default working and final
isolated EEPROMs retain the reference hash; no savestate is loaded or created.
This final run does not perform an in-game save.

The new resource-local programs use the original decoder and uncached RDRAM code
entry. Program-backed sprite headers begin with a branch past the 100-byte header.
Resource 1450 embeds original HVQ2 and caption runs; resource 1460 copies its exact
previous translated pixels. The original HVQ2 path retains arguments and return.
Use translation/status-graphics.json with its exact dispatcher. Legacy RAW2
builds need their historical dispatcher; the builder rejects mixed protocols.

Preserve the **24,552-byte status payload at 0x1B477D8–0x1B4D7C0**, within the
reclaimed **26,556-byte original resource-1460 source**. Its directory owner must
remain included and relocated. The original status blob at 0x1B22138 is untouched.
The equipment payload uses **163,952 bytes**, ending at **0x1FFD3D0**: its new
12-byte copy helper uses the old twelve-byte alignment gap. All 184 book
allocations begin there and remain exact; the final **64 bytes** stay FF.
There is no new free ROM-tail space. Guard ownership/aliases, bounds, pixel hashes,
protocol, code and overlaps before changing graphics. All 107 layout guards remain;
only six words inside the existing nine-word dispatcher changed this milestone.

The exploratory menu-return test reached the bed and wrote only to its isolated
EEPROM. That copy, metadata and log are retained separately in the evidence.
The immutable reference and default working save were untouched. Final validation
restarted from reference. Verify the screen before new menu input; B can return
farther than expected. Do not send Up/A near the bed during navigation tests.

Keep all native text/source slots, 256 donor labels/162 donors, fifteen grids,
66 exclusions and book allocations intact. Cold-boot exact ROMs and use separate
EEPROMs; no older-ROM states. Other species/branches and hardware are not established.
CIC-6102 header for this ROM: **603D64ED 4BB35E71**.

Non-cone sparse checkout retains current/preceding encrypted working copies;
older snapshots remain in Git/GitHub. Add the next slug before staging. Keep
current/preceding verified restores. The older 964-file restore was manifest,
historical-source, canonical-asset and encrypted-part verified; 36 extra files
were retained before its generated tree was removed. The preceding 996-file
facility restore remains alongside this checkpoint. Never remove unique assets.

Recovery uses both ciphertext parts, the JSON index and three checksum files.
Verify parts, join, verify ciphertext, decrypt and verify the ZIP. The existing
passphrase stays outside Git. Git configuration is not in the private archive;
backups/README.md gives current sparse patterns and retrieval commands.

Update this handoff, `PROJECT_STATE.json` and the recovery archive when the milestone changes. A running cloud process is not a persistent checkpoint.

The durable translation checkpoint is the Git tag `status-graphics-alpha`. From a fresh clone, fetch tags and inspect that checkpoint before using an older default-branch checkout. Preserve local changes before switching revisions.
