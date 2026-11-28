# Roulette story alpha

This cumulative partial English draft adds **221 native records**, reaching
**1,671 native records, 832 UI strings, 299 choice blocks and three bitmap
captions**. The preceding 1,450 entries are identical. This milestone covers the
main Dandy/Punch route through Roulette Island; the alternate Mighty/Ram bank
beginning at 1366 and the later regional hints remain for the next milestone.

| Records | Added coverage |
| --- | --- |
| 1136–1163 except 1149 | Koron, pirate-base introductions, rematches and island-clear requirements |
| 1164–1191 except 1177–1178 | Cam, ransom dialogue and the brother's transfer to Ladder |
| 1192–1216 except 1196–1197 | Daicook's food-themed encounters and rematches |
| 1217–1231 except 1223–1224 | Maido's trap and the second pirate on his island |
| 1232–1252 | Akane posing as Kurumi, both rescue-choice outcomes and rematches |
| 1253–1281 except 1269 | Kairi's encounters and her relationship to Ladder |
| 1282–1323 | Captain Ladder, victory/defeat, Tree reward, Punch's return and Gold Blue departure |
| 1324–1341 except 1328–1329 | Arrival, giant-turtle island, entry warnings and roulette-button timing |
| 1342–1365 | Cam's false autograph request, abduction and three-fragment ransom |
| 3676 | Compact native Tree Caramela inventory label: Tree |

The story bank contributes 220 records and the inventory label one. Ten source
cut-message placeholders remain untouched: 1149, 1177, 1178, 1196, 1197, 1223,
1224, 1269, 1328 and 1329. Exact source duplicates reuse wording; different
command streams were adapted separately. No new layout exception or codec change
was needed. The source orders arrival and abduction text after the encounter
bank; record order is not a claim about the order in which players see it.

## Wording and behavior

Provisional names are recorded beside their Japanese in `translation/glossary.json`:
Cam, Captain Ladder, Daicook, Maido, Akane, Kairi, Roulette Island, Silver Island,
Mekkameka and Jeekun Island. Captain Ladder shortens to Ladder in crowded lines;
Roulette Island shortens to Roulette. The false Kurumi calls herself Mekkameka's
Kurumi in the source, and that place name is retained. Native speaker/roster labels
remain Japanese. Cam's cat-like speech keeps short meows and nya endings;
Daicook's cooking metaphors and Maido's snack joke are condensed to fit.

The guide explains timing a button press while the roulette spins. Koron states
that other islands must be cleared before roulette can stop at the Captain's
island. Maido states that beating him alone does not clear his area. Both of
Akane's rescue-choice outcomes expose her disguise. Kairi remains Ladder's sister,
and the Captain's childhood Caramel dream, pride, conditions and entrustment are
retained. The brother's bait/food misunderstanding and the party briefly forgetting
to free him remain separate messages.

Tree Caramela is the compact English term for たいじゅのカラメラ, the great-tree
fragment. The inventory and some crowded dialogue use Tree. Its two-line
acquisition text uses Tree Caramela / +1; the next line of dialogue still calls
it the fourth fragment. Punch's return is retained. The ransom still demands
three Caramela, and its crowded location pair uses Tree/Roulette, with Tree
meaning Tree Blue. Gold Blue remains the next sea, with a warning about Jeekun
Island. The departure's energy check remains 80%. No events, choices, reward
quantities, character transfers or record locations were changed.

All new portrait, expression, color, page, line and player-name commands preserve
their exact arguments and order. English fits the original allocations, 16 cells
per line and three nonempty lines per page. Player names reserve five cells.
Record 831's existing anchored page exception is inherited unchanged.

## Build and verification

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/roulette-story-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/roulette-story-alpha.z64 --patch local/roulette-story-alpha.bps
```

Apply `releases/roulette-story-alpha.bps` directly to the exact Japanese original;
do not stack patches. The target remains 32 MiB. Its MD5 is
`353AEA9646485C7781CD3186D47559C7`. The manifest records source, target and patch
hashes. CIC-6102 CRC1/CRC2 remain `FFA89600 C278C65F`.

The existing 115-test suite passes. The builder checks exact source bytes,
descriptors, controls, widths, allocations and overlapping edits. Floating IPS
independently reproduces the final ROM from the BPS. Read-only chksum64 agrees
with its header. All preceding 1,450 catalog entries compare equal. The original
ROM and reference EEPROM remain intact.

## Runtime and recovery

The exact final ROM cold-booted with an isolated copy of the preserved native
EEPROM. File A retained day 2, 500G, the entered player name and Merlin. File-menu,
ship wake and pause rendering were checked. No savestate was loaded. Reference,
default working and isolated test EEPROM copies remain identical. Evidence is
under `local/roulette-story-evidence/` in the encrypted archive.

The new main Roulette records 1136–1365 and Tree inventory label were not reached
in this run. Their timing/gates, battles, traps, rescue/reward and Gold Blue
departure have build/control/width/allocation checks only. The alternate bank
awaits translation. Earlier evidence/states retain their original ROM identities.
Checks use the supplied emulator environment.

The encrypted archive is decrypted and compared byte-for-byte with its ZIP, then
restored into a separate empty directory, verifying all 585 payload files. The restored suite and reproducible
build, asset/evidence hashes, executable modes, library symlink and exact-ROM
16Kbit EEPROM profile are checked. `BACKUP_MANIFEST.json` records its source
revision and every payload's size and hash.

## Next work

Continue the alternate Roulette bank at record 1366, followed by regional hints,
arrival/abduction variants through 1608, then the new training bank at 1609.
Play the new roulette timing, island-clear gates, both disguise choices, rescue,
reward and departure branches. Earlier Water Blue and Fire Blue branches still
need playthrough coverage. Graphical/roster labels, the Parts frame, capacity
warnings and VS/Transfer Pak branches remain unfinished. Preserve the Dome
three-versus-four-win source discrepancy until checked in play.
