# Resume the Robopon 64 translation

Current translation milestone: **shop-alpha**. The current catalogs contain
220 native records, 185 UI strings and 299 native choice blocks. This remains
a partial, condensed English draft. See `docs/shop-alpha.md` for coverage.

## Check freshness before choosing work

On November 5, 2026 (America/Los_Angeles), the recovered cloud checkout was at
`ea7c7d3` (bed/save), while GitHub main was already at `b6b2202` (shops).
Care, battle, Moon Blue and shop progress was missing from the local checkout.
Do not assume an available workspace is the latest project state.

From this directory, run:

```sh
python -m tools.check_workspace --check-remote --require-save
python -m unittest discover -s tests -q
```

The first command checks whether remote main is included in the current
checkout, then rebuilds in memory and verifies the original, current release,
shipped BPS and preserved native save. It does not change files. It fails if
remote freshness cannot be established. If upstream is newer, fetch and compare:

```sh
git fetch origin main
git log --oneline HEAD..origin/main
```

Review local changes before merging or switching. Fetching alone does not make
the checkout current. For an offline archive without Git metadata, omit
`--check-remote` and confirm freshness separately before starting new work.

`PROJECT_STATE.json` identifies the release manifest, catalogs, ROM, preserved
save, recovery source and next task. The suite currently contains 79 tests,
including checks for stale checkouts and recovery data preservation.

## Rebuild the current release

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/shop-menu.json --story translation/shop-text.json \
  --choices translation/story-choices.json --layout translation/shop-layout.json \
  --output local/shop-alpha.z64 --patch local/shop-alpha.bps
```

The cumulative patch is `releases/shop-alpha.bps`; apply it only to the exact
original. Do not stack earlier patches. Exact hashes are recorded in
`releases/shop-alpha-manifest.json`. Recovery reproduced the shipped ROM and BPS
byte-for-byte; no translation catalogs or release binaries changed in the
workspace-recovery iteration.

## Recover the private assets

The latest complete encrypted snapshot is:

```text
backups/robopon64-progress-2026-11-05_135201-PST.zip.gpg
```

It contains the original/current ROMs, supplied emulator, documented evidence,
historical checkpoints and native save. It uses the same recovery passphrase
as the earlier backup; the passphrase is not in Git. Follow `backups/README.md`
to verify and decrypt it. The decrypted ZIP and all 238 payload file hashes
were verified during recovery.

Use the current source checkout's tools to verify and restore a decrypted ZIP:

```sh
python tools/verify_backup.py /path/to/decrypted.zip
python -m tools.restore_backup /path/to/decrypted.zip /path/to/new-directory
```

The destination must not already exist. Restoration preserves executable modes
and the emulator library symlink, and creates `rom-test/` inside the destination.
It verifies the archive before creating the directory. An older archive's source
does not include newer recovery tools: retain this source checkout as well.
Never extract an old snapshot over current work without comparing versions.

## Native save and emulator

`local/bed-save-final-saved.eep` is the unchanged 2048-byte reference EEPROM:

```text
SHA-256 4b8072efdc08a827141cea1e172205acdb89b17007201d1d1110ff7912f71a00
```

File A holds day 2, 500G, the entered player name and Merlin. The shop build's
working save is:

```text
local/native-saves/Robot Ponkottsu 64 - 7tsu no Umi-EE13E958.eep
```

The launcher reads/writes native saves in `local/native-saves/` and emulator
states in `local/emulator-states/`, both ignored workspace directories. It does
not automatically migrate historical saves from the default home-directory
location. Keep the reference EEPROM separate from gameplay saves. New patched
ROMs need a save copy under their own MD5-based filename.

On a Linux host with Xorg's dummy driver and Mesa installed, run
`tools/start-display.sh` in one terminal. In another, from this directory:

```sh
DISPLAY=:7 LIBGL_ALWAYS_SOFTWARE=1 \
ROM_PATH="$PWD/local/shop-alpha.z64" \
tools/emulator.sh --windowed --gfx mupen64plus-video-glide64mk2 --audio dummy \
  --input mupen64plus-input-sdl --rsp mupen64plus-rsp-hle
```

Return = Start, left Shift = A, left Control = B, arrows = stick, c = R,
Escape = exit. Allow transitions to finish. Cold-boot new builds and use native
EEPROM for persistence checks; older savestates can contain old script data.

`local/shop-alpha-seed-shop.st0` is a navigation checkpoint for the exact
`EE13E958` shop build. It may be used to explore that unchanged build, not to
validate later patches.

## Next work

The shop sell-category panel's Parts label extends beyond its frame. Refine
that layout, then check the parts-shop greeting/stock and remaining warning
branches. Later stock names, combat commands, story, most names, graphical
headings and the kana grid remain unfinished.

Update this state file and `PROJECT_STATE.json` when the current milestone
changes. Keep source checkpoints on the repository and private assets in verified
recovery archives. Shared-chat and Codex thread links could not be read by the
available tools; continuation is based on checked source and artifacts.
