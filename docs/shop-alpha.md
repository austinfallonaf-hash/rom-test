# Shop alpha

This cumulative draft adds 42 shared shop UI strings and ten native color-seed
labels. Totals: **220 native records, 185 Shift-JIS UI strings and 299 native
choice blocks**. Earlier entries are retained unchanged.

Apply `releases/shop-alpha.bps` to the exact original Japanese ROM. Do not stack
patches.

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/shop-menu.json --story translation/shop-text.json \
  --choices translation/story-choices.json \
  --layout translation/shop-layout.json \
  --output local/shop-alpha.z64 --patch local/shop-alpha.bps
python -m unittest discover -s tests -q
```

## Added coverage

- Seed/parts shop greetings, the second greeting page, Cash, Buy/Sell/Exit and
  the Seed/Parts/Apps category labels.
- Buy/sell item questions, price confirmations, Yes/No, thanks, cancellation,
  departure, insufficient money, inventory limits and empty sell categories.
- Shared ATK/DEF/SPD, RAM, equipment restriction and class labels.
- Native records 3878–3887: Red, Blue, White, Yellow, Green, Brown, Gray, Black,
  Pink and Sepia. The Seed suffix is omitted because the original six/seven-glyph
  allocations cannot hold full English names; the shop/category supplies type.

The price confirmation is assembled by the game from an item name, a translated
prefix, the integer price and a suffix. English uses three lines:
`Red / Buy for 100G? / Is that OK?`, or `Sell at` on the price line. The item
name has its own line; six-digit prices still fit sixteen cells. The original
printf format, arguments and references are retained.

The guarded UI validator now recognizes the observed `\L` page break. Page
controls must remain in the same order relative to color changes. Width checks
restart on each page, and shop dialogue opts into a three-line page limit.
Unknown escapes remain rejected. Four new tests cover page widths/line counts,
added/removed page breaks, page movement across a color span and the assembled
price prompts with a full-width item name and six-digit price.

The Buy/Sell/Exit frame has a fixed width, independent of label padding. The
layout catalog changes one guarded MIPS instruction at `0x119cdc` from
`addiu a3,zero,48` to `addiu a3,zero,64`, widening this frame from 48 to 64
logical pixels. Position, height, text coordinates, call target and branches
stay the same. Compact headings `Seeds` and `Parts` use trailing spaces to fit
the existing Shift-JIS centering routine.

Three additional tests cover exact instruction replacement, source/alignment/
size/checksum guards, and rejection of overlap with other edits. Independent
patch application verifies that the BPS includes the instruction change.

## Verification

All 71 tests pass. The guarded builder checks source hash/bytes, controls,
format arguments, widths and allocations. Floating IPS independently applies
the BPS and produces a byte-identical ROM. The original ROM and checksum-covered
prefix are unchanged. The manifest records hashes of all release artifacts.

The final ROM has MD5 prefix `EE13E958`. Runtime testing starts with a cold boot
and the verified day-2 EEPROM copied under this ROM's save filename. Earlier
ROM savestates are not used to verify the new text.

The final build reached the northern seed shop through normal sea navigation.
Both greeting pages, the centered `Seeds` heading, the widened Buy/Sell/Exit
frame, Cash, all ten color labels and their 100G prices were checked on screen.
The assembled Red price prompt fits three lines with Yes/No choices. Buying
one Red changed the balance from 500G to 400G. Declining a subsequent Blue
purchase showed `All right. / Anything else?` and kept the balance at 400G.
The Sell path displayed the Parts/Apps/Seed categories and the seed inventory.
Declining an Ashura sale kept that item and the balance unchanged. Selling the
purchased Red for 50G showed `Sell at 50G?`, removed Red from the list and raised
the balance from 400G to 450G. The thanks/return prompt remained in English.

After the runtime processes stopped between chat turns, testing resumed from
the checkpoint saved by this exact final ROM at the shop greeting. Its full
MD5 matches the current ROM. The original native day-2 EEPROM remains
byte-identical to the verified copy; test purchases are not saved over it.

Evidence includes `shop-release-greeting-full.png`, `shop-release-main.png`,
`shop-release-list.png`, `shop-release-stock-bottom.png`,
`shop-release-price.png`, `shop-release-bought.png` and
`shop-release-declined.png`, plus `shop-release-sell-red-price.png` and
`shop-release-sold-red.png`. `local/shop-alpha-seed-shop.st0` is a same-build
navigation checkpoint for resuming this section, not a state for later patches.

## Remaining work

The parts-shop greeting and stock, warning branches not reached during normal
testing, later shop stock names, later story and combat commands need additional
work or runtime coverage. The sell-category panel's `Parts` label extends past
its original frame and needs a layout refinement; the text remains readable.
Names of later special seeds remain unfinished. This is a partial translation.
