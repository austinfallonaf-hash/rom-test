# Battle-help alpha

This cumulative draft adds native records 2649–2658 and five battle-help menu
labels. Totals: 166 native records, 141 Shift-JIS UI strings and sixteen native
choice blocks. All earlier translation entries are included unchanged.

Apply `releases/battle-guide-alpha.bps` to the exact original Japanese ROM.
Do not stack it on an older patch.

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-guide-menu.json --story translation/battle-guide-text.json \
  --choices translation/dandy-choices.json \
  --output local/battle-guide-alpha.z64 --patch local/battle-guide-alpha.bps
python -m unittest discover -s tests -q
```

## Added topics

| Menu | Details retained |
| --- | --- |
| Move | Equipping software unlocks special moves; moves can attack, immobilize foes or heal HP; stronger moves consume more EP |
| Orbs | Old Man Fairy drops Energy Orbs in battle; color determines effects; HP/stamina benefits and HP loss; some bots evolve by eating many |
| Status | Special moves alter status; Bug causes self-attacks, Stop prevents movement; some effects are beneficial |
| Swap | Switching requires at least two bots; swap an active bot for one on standby during the active bot's turn; choose a replacement when a bot falls |
| Level | Winning battles raises levels; trying attacks, taking damage and running improves different stats |

The two doctor versions retain their own source records and control streams.
The orb-color page uses two lines in one version and three in the other; both
layouts are preserved. English fits sixteen cells per line, the original pages
and each record's exact byte budget. No event branches, battle rules, stats or
checksum-covered bytes are changed. Proper names and status terms remain
provisional; the glossary records the chosen English.

## Verification

All 64 existing tests pass. The guarded builder verifies the original ROM hash,
each original string/record, controls, line lengths and allocations. Floating
IPS independently applies the new BPS and produces a byte-identical ROM.
Earlier catalog entries are retained unchanged.

A cold boot loaded the native day-2 EEPROM through file A, using a copy under
the new ROM's MD5-based save filename. Old-build emulator savestates were not
used. Glide64mk2 remains the recommended renderer.

All five Dr. Dandy topics were traversed to their return prompts: Move (4
pages), Orbs (5), Status (3), Swap (5) and Level (3). The upper and lower topic
menu sections fit. The stronger-move EP requirement, harmful-orb warning, Bug
and Stop definitions, and restriction to switching on the active bot's turn
were visible in English.

A final wording refinement changed only the two level-help records; all other
ROM bytes match the build used for the full twenty-page traversal. On the final
ROM (`0B9B5195` MD5 prefix), all three Level pages and the return prompt were
checked again after a cold boot. The last page reads `Different stats / can
grow a lot.` The native save remained byte-identical throughout guide testing.

Local evidence includes `battle-guide-topic-menu.png`,
`battle-final-level-selected.png`, `battle-moves-3.png`, `battle-orbs-4.png`,
`battle-status-2.png`, `battle-swap-4.png`, `battle-final-level-3.png` and
`battle-final-level-return.png`. The release manifest records the final file
sizes and SHA-256 hashes.

## Remaining work

These are help explanations. Combat command menus, move names, later story,
most names and graphical headings remain unfinished. Testing the guide does
not test the battle mechanics it describes. The alternate doctor version
requires separate runtime coverage.
