# Blue Pass story alpha

Pusuke and E-yan's Moon Blue encounters now have an English draft through the
Blue Pass reward, including their alternate dialogue, repeat challenges,
refusals, victories, defeats and retreat. This adds 70 encounter records and
three compact pass labels to the previous cumulative catalog.

| Records | Added coverage |
| --- | --- |
| 14–48 | Pusuke/E-yan introduction, challenge, secret, Blue Pass and rematches |
| 265–299 | Second encounter-script variant, preserving its own control arguments |
| 3684–3686 | Native inventory labels: Red, Blue and Free |

The cumulative build contains **396 native records, 832 UI strings, 299 choice
blocks and three bitmap captions**. The earlier 323 native entries are retained
exactly. The 70 new encounter entries include 91 dialogue pages and 228 lines
in control-bearing messages; repeated branches count separately. They are a
condensed draft within the original allocations, not a complete game translation.

## Language and constraints

Pusuke is a provisional romanization of プーすけ. Some of his `pu` speech quirk
is retained. Existing E-yan, Johnny, Moon Blue and Moon Caramela terminology is
unchanged. E-yan reveals that Johnny already has the Moon Caramela, then tries
to stop the party after Pusuke points out the disclosure.

Each compact pass-name field allows five glyphs, so the native inventory uses
Red, Blue and Free. Dialogue retains the full Blue Pass name. Translating the
Free label does not translate its later acquisition sequence.

All original portrait, expression, color, line and page commands and their
arguments remain in the original order. No new layout commands, record
relocation, expanded allocations or relaxed codec checks were needed. Lines
remain at most 16 cells and pages at most three lines. These high native-text
edits leave the preceding build's CIC-6102 CRC1/CRC2 unchanged.

## Rebuild and validation

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/blue-pass-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/blue-pass-alpha.z64 --patch local/blue-pass-alpha.bps
```

Apply `releases/blue-pass-alpha.bps` directly to the exact original Japanese
ROM, without stacking patches. The target remains 32 MiB. The release manifest
records source, target and patch hashes. The target MD5 is
`A1FA9CE01A4875B11F32B0C6766F3863`.

The build verifies source bytes, descriptor locations, control streams, line
widths, original byte budgets and edit overlap. The 108-test source suite passes.
Independent Floating IPS patch application reproduces the target byte for byte,
and chksum64 agrees with CRC1/CRC2 `FFA89600 C278C65F`.

The final ROM cold-booted in the supplied Mupen64Plus bundle with Glide64mk2,
using an isolated copy of the preserved native EEPROM. File A retained day 2,
500G, the entered player name and Merlin. Ship/pause and equipment rendering
were checked, including the inherited English bitmap captions. No older-build
emulator state was loaded. Evidence is under `local/blue-pass-evidence/` in the
encrypted recovery archive; the immutable reference EEPROM remains unchanged.

**The new Pusuke/E-yan branches and pass inventory labels have build validation;
they have not yet been reached in a playthrough of this ROM.** The cold-boot and
menu checks establish a regression check, not encounter or hardware coverage.
Earlier runtime scope is documented in [interface heading notes](interface-headings-alpha.md)
and [Moon Blue notes](moon-blue-alpha.md).

## Next work

Continue the remaining Moon Blue story with Sharol, Dean, Godoshii and Johnny,
and play through the Pusuke/E-yan branches. Other graphical headings, the shop
Parts frame, rare status/software-capacity warnings and VS/Transfer Pak branches
also remain unfinished.
