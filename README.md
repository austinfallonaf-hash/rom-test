# Robopon 64 English translation

The current alpha adds the bed/save confirmation, wake-up message, ship navigation and doctor
greetings to the earlier opening, tutorial, ship-menu and help translation.
The cumulative catalogs contain **142 native records, 129 UI strings and 16
choice blocks**. This remains a partial English draft;
graphic headings, most names, the kana grid and later story are unfinished.

File A was saved in-game and loaded after a full emulator restart on the final
build, retaining day 2, 500G, the player name and Merlin. Emulator savestates were
not used for this save/load check.

Apply [the cumulative bed/save BPS](releases/bed-save-alpha.bps) to the exact
original ROM. Do not stack earlier patches. See [bed/save validation
notes](docs/bed-save-alpha.md), [ship-help coverage](docs/ship-help-alpha.md),
[ship-menu coverage](docs/ship-menu-alpha.md),
[Dandy/tutorial coverage](docs/dandy-alpha.md), and
[native text format](docs/story-format.md).

The [full project backup](backups/README.md) includes the original inputs,
emulator and verified save data in an encrypted archive. Its recovery passphrase
is supplied separately in the project chat.

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
  --menu translation/bed-save-menu.json --story translation/ship-help-text.json \
  --choices translation/dandy-choices.json \
  --output local/bed-save-alpha.z64 --patch local/bed-save-alpha.bps
python -m unittest discover -s tests -v
```

The builder checks the entire original hash, each source byte sequence, byte
budgets, and overlapping edits. It creates `local/bed-save-alpha.z64` and
`local/bed-save-alpha.bps`, preserving the original. Apply the BPS to the exact
original using a standard BPS patcher. All edits lie outside the N64 header
checksum coverage; no checksum change is necessary for this alpha.

Extraction yielded 4,941 **unverified candidates**, not a count of script lines.
Candidates can include binary prefixes or miss short/custom/compressed text.
Do not automatically patch them.

## Graphical verification

This host includes Xorg with its dummy driver and Mesa software OpenGL. In one
terminal, run `tools/start-display.sh` (display `:7`, no TCP listener). In another:

```sh
DISPLAY=:7 LIBGL_ALWAYS_SOFTWARE=1 \
ROM_PATH=/workspace/rom-test/local/bed-save-alpha.z64 \
tools/emulator.sh --windowed --gfx mupen64plus-video-glide64mk2 --audio dummy \
  --input mupen64plus-input-sdl --rsp mupen64plus-rsp-hle
```

The launcher initializes a keyboard controller config if missing or empty. It
preserves nonempty existing configuration. Return = Start, left Shift = A,
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
