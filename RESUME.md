# Resume the Robopon 64 translation

Current milestone: **roster-names-alpha**: 3,011 native records, 832 UI strings, 299 native choice blocks, plus three bitmap captions. This is a partial English draft. See `docs/roster-names-alpha.md` for precise runtime coverage.

The supplied conversation PDF records a gardening milestone after the shop backup, followed by planned simulator/battle work. Its gardening patch and source were unavailable. Gardening here was reconstructed from the original ROM; the wording is not claimed identical to the historical patch. Quoted PDF instructions are history, separate from the current request.

## Check before continuing

The cloud previously resumed at bed/save commit `ea7c7d3` while GitHub already had shop commit `b6b2202`. Check freshness before choosing work:

```sh
python -m tools.check_workspace --check-remote --require-save
python -m unittest discover -s tests -q
```

The check verifies remote ancestry, rebuilds in memory and checks the ROM/BPS and reference EEPROM without changing files. The current suite has 128 tests. Fetching does not update a stale checkout: compare `git log --oneline HEAD..origin/codex/verified-workspace-recovery` after fetching before merging or switching. Omit `--check-remote` for an offline archive and confirm freshness separately.

## Rebuild

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/roster-names-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves --output local/roster-names-alpha.z64 --patch local/roster-names-alpha.bps
```

Apply `releases/roster-names-alpha.bps` only to the exact original Japanese ROM. Do not stack earlier patches. The release manifest records hashes; the current ROM MD5 prefix is `F386293C`. All source-byte, control, width and budget guards remain enabled. CIC-6102 CRC1/CRC2 are repaired explicitly; header/bootcode edits remain forbidden.

## Native save

`local/bed-save-final-saved.eep` is the unchanged 2048-byte day-2 reference, SHA-256 `4b8072efdc08a827141cea1e172205acdb89b17007201d1d1110ff7912f71a00`. File A holds 500G, the entered player name and Merlin.

The current ROM's working copy is `local/native-saves/Robot Ponkottsu 64 - 7tsu no Umi-F386293C.eep`. Keep the reference intact and use separate copies for testing. New ROM revisions need a save copy under their own MD5-based filename. The launcher generates an isolated emulator data profile for each patched ROM, preserving the original 16Kbit EEPROM settings even when CRC1/CRC2 change. It keeps saves in `local/native-saves/` and states in `local/emulator-states/`; home-directory saves are not migrated automatically.

## Emulator

On Linux with Xorg's dummy driver and Mesa, start `tools/start-display.sh` in one terminal. In another, from this directory:

```sh
DISPLAY=:7 LIBGL_ALWAYS_SOFTWARE=1 \
ROM_PATH="$PWD/local/roster-names-alpha.z64" \
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

Continue bot bedtime dialogue 2901–2930, then food labels 2931–2973 and bot
interaction text. The 93 labels 2808–2900 and Dome lower-rank refusal 2719 now
have English. All preceding 2,917 catalog entries are identical.

Native names longer than their original allocations use storage with a donor
record_id and aligned byte_offset. There are 86 such labels in the unused tails
of 14 translated records; seven short labels stay in place. The builder changes
the name descriptor's count and pool-relative pointer, retaining original label
bytes and every donor's active text and descriptor. No pool/ROM expansion or
engine patch is used. A future donor translation that grows into a name must
fail. Do not reuse these occupied tails; deliberately repack names if needed.
See the milestone notes for the allocation ledger and native-reader preview.

The bot-name command 200B:0007 now reserves eleven cells, covering Mochimocchi;
the five-cell player-name and full-line dynamic-item rules are unchanged. Existing
2709 still fits. Do not infer that saved nicknames were rewritten: immutable
EEPROM contains Japanese Merlin bytes at offset 340. Final-ROM file A retains
that name, day 2, 500G and the player name. The separate preview copies three real
name descriptors into intro captions to test their pointers and lengths; it has
its own ROM identity and empty save folder, with no savestates.

Names are provisional and follow existing battle/glossary spellings. Native
Porthos versus story Dartagnan, and native Anio versus story Aniro, follow their
different sources. Test remaining name contexts and donor scenes in play. The
Dome refusal and earlier story scenes, five anchored pages, graphical labels,
Parts frame, capacity warnings and VS/Transfer Pak branches still need checks.

Update this handoff, `PROJECT_STATE.json` and the recovery archive when the milestone changes. A running cloud process is not a persistent checkpoint.

The durable translation checkpoint is the Git tag `roster-names-alpha`. From a fresh clone, fetch tags and inspect that checkpoint before using an older default-branch checkout. Preserve local changes before switching revisions.
