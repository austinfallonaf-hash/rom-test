# Ship pause-menu alpha

This cumulative patch adds 73 Shift-JIS UI entries and three native item-name records to the earlier translation.
The current catalogs contain 126 native text records, 91 UI entries and sixteen
length-prefixed Yes/No blocks. It is an incomplete English draft.

Build from the exact original Japanese ROM:

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/ship-menu.json --story translation/ship-text.json \
  --choices translation/dandy-choices.json \
  --output local/ship-menu-alpha.z64 --patch local/ship-menu-alpha.bps
```

## Compact menu labels

The root category box is only four glyph cells wide. The short English labels
preserve its layout rather than expanding into neighbouring panels:

| Japanese | English | Meaning |
| --- | --- | --- |
| ロボポン | Bots | Robopon party |
| パーツ | Gear | Parts/equipment |
| ソフト | Apps | Software |
| たべもの | Food | Food |
| アイテム | Item | Other items |
| カラメラ | Gems | Caramela collection |
| ならび | Sort | Party order |

Equipment actions use Set and Del to fit the smaller three-cell submenu. The
profile's elemental labels use `T:` for Type; `T:Elec` abbreviates lightning.
Arm class names omit the repeated Arm prefix (Caster, Knight, Healer, etc.).

The catalog also includes work/exercise labels, numeric stat lines, RAM/error
text, evolution indicators, days, CPU chips, and item-discard prompts. Not all
of these appear in the initial party's available screens.

## Color and formatting guards

The UI validator now recognizes the existing `\Cnnn` colors and requires their
arguments and order to remain unchanged. Unsupported source or target escapes
are rejected. Existing printf specifiers, including their order and widths,
must be preserved. Layout checks strip color bytes and reserve visible cells
for printf values; declared reservations cannot undercut printf's minimum width.
Discard prompts put a reserved item-name line above `Drop it?`, preserving the
original highlighted `%s` and reset-color commands.

The visible starter item names come from native glyph-index records rather than
Shift-JIS metadata. Record 3604 (チャームハンド) is shortened to Charm to fit seven
glyphs, record 3985 (ファイア) becomes Fire, and record 3891 (アシュラシード) becomes
Ashura in inventory. The full Ashura Seed name remains in the tutorial reward.
These are compiled through the existing BPS path. Earlier attempted metadata
edits that did not affect these screens were removed; no executable/checksum
region changes are required.

The checksum routine was checked during diagnosis: the original CIC-6102 boot
CRC32 is `90BB6CB5`, and the computed original header words were `272B690F` /
`AD0A7A77`. No checksum update was made or needed in this release.

## Limitations

Hunger, stress, and several pane headings are graphics; these remain Japanese.
The kana input grid, initial names, most item/move names, species names, and later
story also remain unfinished. This does not claim that every stat screen or
inventory message is English. Work assignment, rare classes/types, full-party
conditions and insufficient-RAM paths require further runtime coverage.

Pearlton is treated as a ship fuel/resource, not the G money counter. The earlier
glossary's currency interpretation has been corrected based on the stoking task.

## Final runtime checks

A cold boot of the final ROM traversed the existing opening/tutorial to ship
control. The following screens were checked on that build:

- Root menu: all seven compact categories fit, along with the day counter.
- Bot profile: Caster, T:Water, Attack/Defense/Speed, CPU, evolution and orb labels
  fit; the CPU label was shortened after the initial badge overflow was observed.
- Parts: Set/Del fit the submenu; Charm and ATK/DEF/SPD/RAM display correctly.
  The original starter values remain 7/8/0 and 10M.
- Software: Fire v1 and the 10M/10M RAM display are intact. Ability names and
  graphical headings on this screen remain Japanese.
- Items: the starting Ashura seed is visible with its compact English label.
- Gems and Sort: both screens open and cancel back to the root menu; no party
  reorder was committed.

Discard prompts were **not runtime-tested**. The initial party has no spare
parts/software to discard; the starting seed view did not expose a discard
operation, and the tested A/Z controls did not unequip Charm from the empty
parts-selection screen. No item was removed. Color/printf preservation and line
budgets for those prompt entries are unit-tested, but this does not establish
runtime coverage. Work/exercise assignment and rare error paths are also unrun.

All 64 automated tests pass. Floating IPS applied the final BPS successfully,
and its output is byte-identical to the generated ROM. The original ROM hash,
ROM size, and checksum-covered region remain unchanged. The release manifest
records file sizes and SHA-256 hashes.

Local evidence includes `ship-root-final.png`, `bot-profile-release.png`,
`gear-actions-release.png`, `gear-status-release.png`,
`software-status-release.png`, `item-actions-release.png`,
`gems-menu-release.png`, and `sort-menu-release.png` under `local/`.
The exploration checkpoint is `local/after-ship-menu-alpha.st0` for this exact
ROM build; use a cold boot to validate later ROM changes.
