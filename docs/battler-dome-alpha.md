# Battler Dome alpha

This cumulative draft adds 202 native records: Moon Blue regional hints, the
alternate coaster bank, Normal Fight and Select Fight events, and two S-rank
acknowledgements. Totals are **820 native records, 832 UI strings, 299 choice
blocks and three bitmap captions**. The preceding 618 entries are unchanged.
This remains a partial translation; later story and many graphical labels,
roster names and item names are unfinished.

| Records | Added content |
| --- | --- |
| 390–437 | Regional opponents, battle/orb tips, Dome rules, seven seas, fuel and bot-care hints |
| 438–501 | Alternate coaster attendants, pass checks, return routes and Fire Blue exit |
| 2720–2743 | Normal Fight entry, rounds, prizes, defeat and F–S rank variants |
| 2744–2807 | Select Fight entry, species restrictions, rounds, prizes and defeat |
| 4100, 4106 | S-rank acknowledgements in both speech variants |

The new control-bearing messages contain 436 pages and 1,097 lines, counting
repeated branches separately. Native IDs 0–501 now have catalog entries. This
does not establish full first-sea or tournament playthrough coverage.

## Source details

Normal Fight uses one chosen Robopon. Select Fight requires a particular species.
Their event scripts consistently ask for three consecutive wins. Regional hint
416 instead says four. Both source claims are translated as written; the actual
win requirement remains to be checked in play. Battle rules and event logic are
unchanged. The S-rank congratulation also retains the source's reference to
Robopon gardening skill.

Prof. Flower, Nose, Mescal, Merlias, Tanbi, Pipa and Nikuro are provisional names
recorded alongside their Japanese spellings in the glossary. Roster names are
still Japanese. Hint 436 explains that Blue means sea rather than the color.
The compact seven-sea list in 426 omits the shared Blue suffix for Tree/Gold and
Land/Sunny to fit the source's two paired lines; the glossary has the full names.

All new source portrait, expression, color, page, line and variable commands
retain their exact arguments and order. Text is condensed within the original
allocations and 16-cell/three-line limits. No record relocation, expansion or
additional layout commands were needed. Existing layout exceptions are retained.

## Dynamic rewards

The generic prize message uses variable `[200B:0006]`, rather than the entered
player name. The codec now reserves a whole line for that argument instead of
assuming a five-cell name. The reward variable stays alone on its original
line, between its unchanged color commands; Got it! occupies the next line.
This prevents added English from crowding an unbounded runtime item label.
No runtime variable lookup or reward choice is changed. Three new unit tests
reject prefixes/suffixes beside the reward variable and verify its argument and
following line are preserved. The previous cumulative patch still rebuilds
byte for byte with the stricter guard.

## Build and verification

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/battler-dome-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/battler-dome-alpha.z64 --patch local/battler-dome-alpha.bps
```

Apply `releases/battler-dome-alpha.bps` directly to the exact original Japanese
ROM without stacking patches. The target remains 32 MiB; MD5 is
`93E5FFD1B56C7270CF05EC6D2BBBA47E`. The release manifest records source,
target and patch hashes. CRC1/CRC2 remain `FFA89600 C278C65F`.

All 111 tests pass. The builder checks source bytes, descriptors, control
streams, widths, allocations and overlapping edits. Floating IPS independently
reproduces the target from the BPS, and chksum64 agrees with its header CRCs.
All 618 preceding catalog entries compare equal.

The final ROM cold-boots in the supplied Mupen64Plus/Glide64mk2 environment
with an isolated copy of the preserved native EEPROM. File A retains day 2,
500G, the entered player name and Merlin. File-menu, ship wake-up, pause and
equipment rendering are checked, including inherited English captions and
app/move names. No older-build emulator state is loaded. Evidence is under
`local/battler-dome-evidence/` in the encrypted recovery archive. The reference
EEPROM and original ROM remain unchanged.

**New hint, coaster and Dome branches, dynamic prize rendering and S-rank
acknowledgements have build validation only; they have not been reached in a
playthrough of this ROM.** The loading/menu checks establish regression coverage,
not new-branch or hardware coverage. See [previous story notes](moon-blue-story-alpha.md)
for inherited scope.

## Next work

Continue the alternate opening beginning at record 502, then the Fire Blue
encounters beginning at 560. Play through the Dome entry/reward paths and resolve
the source's three-versus-four-win discrepancy. Other graphical headings, the
shop Parts frame, capacity warnings and VS/Transfer Pak branches remain unfinished.
