# Simulator and reconstructed gardening alpha

This cumulative draft contains 279 native records, 261 Shift-JIS UI strings and
299 native choice blocks. It includes all shop-alpha entries unchanged, 50
reconstructed gardening/newborn dialogue records, nine additional seed labels,
twelve gardening UI strings and 64 simulator/battle-result UI strings.

Apply `releases/simulator-alpha.bps` only to the exact original Japanese ROM.
Do not stack earlier patches.

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/simulator-menu.json --story translation/garden-recovery-text.json \
  --choices translation/story-choices.json --layout translation/shop-layout.json \
  --output local/simulator-alpha.z64 --patch local/simulator-alpha.bps
```

## Conversation recovery

The user supplied a 16-page PDF of the previous conversation. Its last completed
milestone was gardening, after the shop backup on GitHub, and its next planned
section was battle menus and simulator text. The PDF contains a completion
summary but no gardening catalog, patch bytes or usable patch-download link.
The user has no additional artifacts. No gardening source or patch was found
in the workspace, available Git objects or repository branches.

The gardening coverage here is newly reconstructed from the original Japanese
ROM. It is not a byte-identical recovery of the unavailable patch, and its
English wording may differ. The prior conversation's claim of a five-night
growth/harvest test applies to that older build, not automatically to this one.
Quoted instructions in the PDF were treated as historical context; the current
user request is to continue the translation.

## Added coverage

- Planting menus and seed choice; viewing/clearing runners; harvesting, renaming
  and automatic storage; full-ship and full-app-inventory refusal/discard prompts.
- Native newborn remarks 2689–2718 and growth remarks 3898–3917, with the original
  portrait arguments, name insertion, line breaks and byte allocations retained.
- Dragon, Wrestlr, Shark, Marilyn, Human, Matango, Eagle, Belbara and Purin seed
  labels. These are compact provisional names; `Wrestlr` omits a letter to fit
  its seven-glyph allocation. Existing Ashura and color-seed labels are retained.
- Simulator entry confirmation, roster heading, Swap/Start and roster stats;
  VS types, bot sources, strength choices, stage names and transfer/read messages.
- Battle win/loss, CPU bits, total-power/reward messages, post-battle hunger and
  stress, consumed orbs and stat increases.

Some simulator selection strings are shared with other battle modes. Translating
their guarded source strings does not establish runtime coverage of every mode,
stage, Transfer Pak operation or empty-save branch. Stage names are provisional
romanizations. Graphical command icons, HUD headings, most bot/move names and
text inside the checksum-covered executable remain unfinished.

## Guarded player-name controls

The harvest UI uses the observed `\H000` player-name insertion. The validator
now reserves its five-character capacity and preserves the control's argument
and position relative to color/page controls. Other `\H` arguments remain
unsupported. Three tests cover its display width, removal/argument/context
changes and unknown arguments. Printf arguments remain in original order;
harvest name fields and battle-result parameters have explicit width reserves.

All 82 tests pass. The guarded build validates the exact original hash and every
source string/record, controls, widths and allocations. Floating IPS independently
reproduces the generated ROM from the release BPS. All 185 earlier UI strings
and 220 earlier native records compare equal, and the checksum-covered prefix
is unchanged. The final ROM's MD5 prefix is `20B19F3D`.

## Remaining work

Complete the runtime coverage recorded below before treating any unplayed
branch as verified. Continue with graphical battle command labels, later combat
names and warning branches. The earlier shop sell-category Parts label still
needs its separate frame refinement. Later story and most graphical labels
remain unfinished.
