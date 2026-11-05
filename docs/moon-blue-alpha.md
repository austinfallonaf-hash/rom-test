# Moon Blue alpha

This cumulative draft adds 44 native records: both versions of Koron's first
encounter and fourteen information keeper messages for the first sea. It also
translates the helm's departure confirmation. Totals: **210 native records,
143 Shift-JIS UI strings and 299 native choice blocks**. Every entry from the
battle-guide alpha is retained unchanged.

Apply `releases/moon-blue-alpha.bps` to the exact original Japanese ROM, rather
than stacking it on another patch.

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/moon-blue-menu.json --story translation/moon-blue-text.json \
  --choices translation/story-choices.json \
  --output local/moon-blue-alpha.z64 --patch local/moon-blue-alpha.bps
python -m unittest discover -s tests -q
```

## Added coverage

| Records | Translation |
| --- | --- |
| 0–13, 249–264 | Koron's introduction, Moon Caramela question, battle challenge, refusal, defeat/victory, Red Pass reward, coaster instructions and repeat conversations |
| 376–389 | Moon Blue warning and former theme park, Caramela legend, coaster passes, Koron's northbound route toward Pukapon Island, Johnny and other regional battlers, short follow-up greetings |
| UI `0x103fc8`, `0x103fe4` | `Head to sea?` and the `No` option beside the original `GO!` |

Dialogue is condensed to the original allocations and sixteen cells per line.
Portraits, colors, page breaks and event references remain in order. Record 388
adds one layout newline inside a color span to fit the four battler names on
three lines; all existing controls remain in order. No text is relocated.

The glossary records provisional names. `Moon Caramela` is the compact dialogue
form of Full Moon Caramela. `Screw Coaster` is a literal working translation.
Later dialogue may provide better evidence for names and terminology.

## Native choices

The event bank contains 359 exact copies of the count-prefixed Japanese Yes/No
pair. Of these, 285 have the verified `0006 0002 ffff` two-choice header.
Those 285 blocks and the previously verified sixteen blocks form a union of
299; two occur in both sets. The other sixty matches are left untouched because
their preceding format has not been established.

Each replacement keeps the address and total fourteen-byte allocation: two
glyphs for Japanese Yes and three for No become three for `Yes` and two for `No`.
The menu's count prefixes are updated. Branch commands retain their addresses.
The new catalog records the original header bytes for further review. The
builder guards the entire original ROM hash and each choice's exact bytes.
This static format validation does not establish runtime coverage of all menus.

## Verification

All 64 existing tests pass. The guarded builder validates source bytes, metadata,
control streams, widths and allocations. Floating IPS independently applies the
BPS and produces a byte-identical ROM. All earlier catalog entries compare
equal. The original ROM and its checksum-covered prefix remain unchanged.
The release manifest records source, target and patch hashes.

The final ROM (`5A5FDA2C` MD5 prefix) cold-boots and loads the verified day-2
native EEPROM via file A. No old-build emulator savestate is used. The helm
shows `Head to sea?` with `GO!` and `No`, with the popup width intact. Runtime
evidence remains in ignored `local/`, including `moon-departure.png`.

Both pages of the first island's opening message were traversed. The warning
`Beware Moon Blue / Sea pirates, / bad foes ashore!` and the former theme-park
page fit the box with the source color and portrait changes. Captures:
`moon-port-intro.png` and `moon-port-history.png`. The event returns to sea.

For continued route testing, `i` (C Up) selects an overhead sea view and `k`
(C Down) cycles the map display. Left/right steer the ship; holding a turn for
several seconds makes it circle. A brief turn followed by Up holds a straight
course. This differs from movement aboard the ship. The native day-2 EEPROM
remains byte-identical to the trusted saved copy after sea exploration.

## Remaining work

Koron's encounter scripts, including the victory/reward path and alternate
variant, and the other information keeper messages need runtime coverage.
Route exploration reached the northern seed shop; its Japanese dialogue and
menus are a separate pending section. Later story, combat command menus, most
proper names, graphical headings and the kana grid remain unfinished. This is
a partial translation, not a complete first-sea playthrough or hardware test.
