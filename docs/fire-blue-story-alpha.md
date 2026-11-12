# Fire Blue story alpha

This cumulative draft adds **165 native records**: Dr. Mighty and Ram's alternate
opening, the main Fire Blue theft/encounter/reward sequence, and the compact Fire
treasure label. Totals are **985 native records, 832 UI strings, 299 choice blocks
and three bitmap captions**. The preceding 820 records are unchanged. This is
a partial translation; the later interlude, coaster/alternate story banks and
many graphical and roster labels remain unfinished.

| Records | Added coverage |
| --- | --- |
| 502–559 | Mighty/Ram opening, password, refusals, Micro and Shark Seed gifts, and transition hints |
| 560–642 | Henpei, Mark, Komura, Dongo and Mura encounters, rewards and rematches |
| 643–679, excluding 14 cut-message placeholders | Gariman's stolen treasure, the party's intervention, return and Water Blue route |
| 3674 | Native Fire Caramela inventory label: Fire |

The new control-bearing messages contain 284 pages and 718 lines, counting
repeated branches separately. The Shark inventory label was already translated
at record 3890 and remains unchanged. Native record IDs 0–646 now have entries.
The 14 source records labeled カットメッセージ are left untouched: 647, 648,
650, 651, 658–665, 667 and 669.

## Language and layout

The alternate opening retains its distinct professor, ship, companion and gifts:
Dr. Mighty, Doluppi, Ram, Micro, Shark Seed and ten medals. Provisional names are
recorded with their Japanese spellings in the glossary. Micro's native roster
name remains Japanese. The computer's password/launch messages retain their
uppercase style.

Fire Caramela is the compact dialogue term for ほのおのカラメラ. The eight-glyph
native inventory field uses Fire, matching the earlier Full Moon label's omission
of Caramela. A few crowded dialogue lines also use Fire. Fixed transfer messages
use ASCII direction marks between the giver and recipient; the compact initial
reward reads Fire Caramela +1. No reward amounts or event logic are changed.

Komura's baby babble and Dongo's repeated chants are rendered phonetically,
without inventing decoded meanings. Mark's flexing/song wordplay is condensed.
In record 590, the original middle page contains four line slots. Its three
English chant lines leave the last cursor line empty; all original portrait and
line commands remain in order. No layout exception or extra page was added.

Every new portrait, expression, color, page, line and player-name command retains
its exact arguments and order. English stays within the original allocations,
16 cells per line and three nonempty lines per page. Player-name substitution
reserves five cells. No record relocation, expansion or codec change was needed.

## Build and verification

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/fire-blue-story-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/fire-blue-story-alpha.z64 --patch local/fire-blue-story-alpha.bps
```

Apply `releases/fire-blue-story-alpha.bps` directly to the exact original Japanese
ROM without stacking patches. The target remains 32 MiB; its MD5 is
`07EC747C6805124E327FC2A1872EED28`. The release manifest records source,
target and patch hashes. CRC1/CRC2 remain `FFA89600 C278C65F`.

All 111 tests pass. The builder checks source bytes, descriptors, control streams,
widths, allocations and edit overlap. Floating IPS independently reproduces the
target from the BPS, and chksum64 agrees with its header CRCs. All 820 preceding
catalog entries compare equal. The original ROM and reference EEPROM remain
unchanged.

## Runtime coverage

The exact final ROM cold-booted with an isolated copy of the preserved native
EEPROM. File A retained day 2, 500G, the entered player name and Merlin. The file
menu, ship wake-up dialogue and pause menu rendered correctly. No older-build
state was loaded. Evidence is under `local/fire-blue-story-evidence/` in the
encrypted recovery archive. The reference and default working EEPROM remain
unchanged.

A separate cold start selected the empty file B and skipped the inherited
opening movie with Start. The new Mighty/Ram opening was reached naturally.
Records 502–509 were traversed through twelve dialogue pages, including the
Doluppi/Dr. Mighty name page and both uppercase password-request pages. English,
colors and portraits fit their boxes. The run stopped before name entry.

`local/fire-blue-story-evidence/opening-502.st0` is an exploration checkpoint
saved after that cold start, on record 502's first page. Its M64+SAVE header
contains the exact final ROM MD5. It belongs only to this ROM and was not loaded
for validation. Never use it to validate a later build. All reference, default
working and isolated native EEPROM copies remain byte-identical.

The rest of the new opening (510 onward), Micro/Shark gifts, and the new Fire
Blue encounter, theft, reward and return branches have build validation only;
they have not been reached in a playthrough of this ROM. Checks use the supplied
Mupen64Plus/Glide64mk2 environment, not hardware.

## Remaining work

Continue the musketeers interlude beginning at record 680 and the remaining
coaster/alternate story banks before the next sea's main story. Exercise the new
Fire Blue theft, battle, reward and return branches in play. Other graphical
headings, roster names, the shop Parts frame, capacity warnings and VS/Transfer
Pak branches remain unfinished. The earlier Dome three-versus-four-win source
discrepancy remains documented in [Dome notes](battler-dome-alpha.md).
