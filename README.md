# Robopon 64 English translation

For a resumed cloud workspace, start with [RESUME.md](RESUME.md). Run
`python -m tools.check_workspace --check-remote --require-save` before continuing
to detect a checkout that is behind GitHub and verify the current release/save.
`PROJECT_STATE.json` identifies the current catalogs and recovery checkpoint.

The current Fire Blue story alpha adds Dr. Mighty and Ram's alternate opening,
Micro and Shark Seed gifts, and the main Fire Blue theft, encounter and reward
sequence. It contains 985 native records, 832 UI strings, 299 choice blocks and
three bitmap captions. This remains a partial English draft; later interludes,
coaster/alternate story banks, graphical labels and roster names are unfinished.

The earlier bed/save build verified an in-game save and cold reload of file A,
retaining day 2, 500G, the player name and Merlin. Later builds load that native
save for testing, starting from a cold boot. Old-build emulator savestates are
not used for validation.

Apply [the cumulative Fire Blue story BPS](releases/fire-blue-story-alpha.bps) to the exact
original ROM. Do not stack earlier patches. See [Fire Blue story notes](docs/fire-blue-story-alpha.md) for the new coverage and
[simulator and gardening notes](docs/simulator-alpha.md)
for provenance, tested coverage and limitations, and [shop coverage and validation
notes](docs/shop-alpha.md), [Moon Blue coverage](docs/moon-blue-alpha.md),
[battle-guide coverage](docs/battle-guide-alpha.md),
[bot-care coverage](docs/care-guide-alpha.md),
[bed/save validation](docs/bed-save-alpha.md),
[ship-help coverage](docs/ship-help-alpha.md),
[ship-menu coverage](docs/ship-menu-alpha.md),
[Dandy/tutorial coverage](docs/dandy-alpha.md), and
[native text format](docs/story-format.md).

The [project backup](backups/README.md) includes original inputs, the emulator,
the current translation and verified native save data in an encrypted archive.
Its recovery passphrase was supplied separately in the project chat.

## Inputs

Keep user-supplied binaries in ignored `local/`:

- `local/original.z64`: unmodified big-endian ROM, SHA-256
  `02cda6221c10cba0705f351227e2d6c77e071bdb4f7aa8b5cd3c7c047a2b1881`
- `local/mupen64plus-bundle-linux64-2.6.0/`: supplied emulator bundle

## Extract, build, test

From `/workspace/rom-test`, Python 3.12, standard library only:

```sh
python tools/rom_text.py local/original.z64 --output local/text-candidates.json
python -m tools.story_text local/original.z64 --output local/story-records.json
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/fire-blue-story-text.json \
  --choices translation/story-choices.json \
  --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves --output local/fire-blue-story-alpha.z64 --patch local/fire-blue-story-alpha.bps
python -m unittest discover -s tests -v
```

The builder checks the entire original hash, each source byte sequence, byte
budgets, and overlapping edits. It creates `local/fire-blue-story-alpha.z64` and
`local/fire-blue-story-alpha.bps`, preserving the original. Apply the BPS to the exact
original using a standard BPS patcher. Battle HUD strings lie inside CIC-6102 checksum coverage. The explicit flag
repairs CRC1/CRC2, preserving bootcode and other header fields. The launcher
generates an isolated profile preserving the emulator's EEPROM/game settings.
See [checksum notes](docs/n64-checksums.md).

Extraction yielded 4,941 **unverified candidates**, not a count of script lines.
Candidates can include binary prefixes or miss short/custom/compressed text.
Do not automatically patch them.

## Graphical verification

This host includes Xorg with its dummy driver and Mesa software OpenGL. In one
terminal, run `tools/start-display.sh` (display `:7`, no TCP listener). In another:

```sh
DISPLAY=:7 LIBGL_ALWAYS_SOFTWARE=1 \
ROM_PATH=/workspace/rom-test/local/fire-blue-story-alpha.z64 \
tools/emulator.sh --windowed --gfx mupen64plus-video-glide64mk2 --audio dummy \
  --input mupen64plus-input-sdl --rsp mupen64plus-rsp-hle
```

The launcher initializes a keyboard controller config if missing or empty. It
preserves nonempty existing configuration. Native saves now live in
`local/native-saves/` and emulator states in `local/emulator-states/`, so they
travel with the workspace. Existing saves in the user's default Mupen directory
are not moved automatically. Return = Start, left Shift = A,
left Control = B, arrows = stick, Escape = exit. While walking aboard the ship,
Face the bed and press left Shift (A) to interact. `c` (R trigger) opens
the ship's floor/destination navigation. At the title, press Return to
open the scenario menu, then left Shift to select it and reach save selection.
Allow screen transitions to finish before pressing the next key.
Glide64mk2 is recommended for this alpha: Rice can draw foreground ship objects
over the help dialogue during facility camera views.

Optional screenshot/input helper dependencies (kept outside tracked files):

```sh
python -m pip install --target local/python python-xlib==0.33 Pillow
DISPLAY=:7 PYTHONPATH=local/python python tools/desktop.py --key Return
DISPLAY=:7 PYTHONPATH=local/python python tools/desktop.py --capture local/current.png
```

ROMs, extracted script, emulator binaries, saves, and screenshots stay local.
See [research notes](docs/research.md) for scope, evidence, and next milestones.
