# Roulette variants alpha

This cumulative partial English draft adds **235 native records**, reaching
**1,906 native records, 832 UI strings, 299 choice blocks and three bitmap
captions**. The preceding 1,671 entries are identical. Both Roulette rescue
routes, Tree Blue's regional hints and the arrival/abduction variants now have
a draft. The next untranslated bank begins at 1609.

| Records | Added coverage |
| --- | --- |
| 1366–1552 except eight portrait-only records | Alternate Koron, Cam, Daicook, Maido, Akane, Kairi and Ladder encounters, Ram rescue, Tree reward and Gold Blue departure: 179 records |
| 1553–1569 | Tree Blue regional hints and cleared-area reactions: 17 records |
| 1570–1608 | Alternate arrival, roulette guide, false autograph request and Ram abduction: 39 records |

Of these 235 records, 177 have an exact Japanese-source match in the preceding
catalog and reuse its English. The other 58 source variants/new hints were
reviewed separately. There are no new inventory labels. Records 1379, 1407, 1408,
1426, 1427, 1453, 1454 and 1499 contain only portrait commands; their payload and
descriptor bytes remain identical to the original and are not counted as
translated text. Existing cut-message placeholders remain untouched.

## Wording and source differences

Ram replaces Punch in the alternate rescue and abduction scenes. The distinct
professor's reactions, Ram's complaint when briefly forgotten, his return and the
promise to finish the quest are retained. The departure still checks 80% energy,
and the ransom/reward dialogue retains three fragments demanded and the fourth
fragment obtained. The timing guide and island-clear requirements remain.

Ladder's farewell in record 1530 explicitly names **Caramel**, the legendary
Robopon, using the character-name color. Main-route record 1300 names **Caramela**,
the fragments, using the treasure color. Both source wordings and colors are
retained; the preceding main-route translation is unchanged. The glossary notes
this distinction. Record 1542 also retains its colored Roulette name in the
engine-start command, where the main source bank has plain text.

The regional hints cover the pirates' base, Roulette's ancient technology,
Ladder's reputation and battle skill, Kairi/Cam preferences and the suggestion that
Ladder sees the player as his successor. The admirer dialogue retains its
"is this love?" punchline, and the spinning joke retains its passive/active
self-correction. Existing provisional names and compact Tree/Ladder/Roulette
forms remain. Native speaker/roster labels remain Japanese.

Every new portrait, expression, color, page, line and player-name command preserves
its exact arguments and order. English fits the original allocations, 16 cells
per line and three nonempty lines per page. Player-name substitutions reserve
five cells. No new layout exception, codec change, event edit, reward change,
character transfer edit or record relocation was needed. Record 831's existing
anchored page exception is inherited unchanged.

## Build and verification

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/roulette-variants-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/roulette-variants-alpha.z64 --patch local/roulette-variants-alpha.bps
```

Apply `releases/roulette-variants-alpha.bps` directly to the exact Japanese
original; do not stack patches. The target remains 32 MiB. Its MD5 is
`C87382BA5CDF6A72416A1D0AE21D4F45`. The manifest records source, target and patch
hashes. CIC-6102 CRC1/CRC2 remain `FFA89600 C278C65F`.

All 115 existing tests pass. The builder checks exact source bytes, descriptors,
controls, widths, allocations and overlapping edits. Floating IPS independently
reproduces the final ROM from the BPS. Read-only chksum64 agrees with its header.
All preceding 1,671 entries compare equal, and the eight portrait-only records'
payloads and descriptors match the original byte-for-byte. The original ROM and
reference EEPROM remain intact.

## Runtime and recovery

The exact final ROM cold-boots from an isolated native EEPROM copy. File A retains
day 2, 500G, the entered player name and Merlin. The file-menu prompt, ship wake
text and pause rendering were inspected with the supplied Mupen64Plus/Glide64mk2.
No savestate was loaded or created; no in-game save was attempted. Original ROM
and reference/default/isolated EEPROM hashes remain unchanged. The exact-ROM
profile retains 16Kbit EEPROM, two players and Transfer Pak metadata. Screenshots,
completed emulator log and file hashes are in `local/roulette-variants-evidence/`.

The new alternate Roulette scenes, regional hints and arrival/abduction variants
were not reached in playthrough. Both Roulette routes and earlier Water/Fire Blue
scenes still await gameplay checks; their new text has build validation only.
Historical states retain their original ROM identities and were not used.

The AES-256 recovery archive decrypts byte-for-byte to its ZIP. A clean restore
verifies all 602 payload files and passes all 115 tests, including ROM/BPS/save
checks, executable modes, the emulator library symlink and exact-ROM profile.
The manifest records the archived source revision. The passphrase stays outside
Git; earlier ROMs rebuild from their cumulative patches. See `backups/README.md`.

## Next work

Continue the training/story bank at native record 1609. Play both Roulette routes,
regional hints, timing/gates, both disguise choices, rescue/reward and departures,
including the Caramel/Caramela farewell difference. Earlier Water/Fire Blue
branches and record 831's page split still await playthrough. Graphical/roster
labels, the Parts frame, capacity warnings and VS/Transfer Pak branches remain
unfinished. Preserve the Dome three-versus-four-win discrepancy until checked
in play.
