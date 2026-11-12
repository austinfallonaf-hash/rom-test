# Water Blue story alpha

This cumulative partial English draft adds **261 native records**, reaching
**1,450 native records, 832 UI strings, 299 choice blocks and three bitmap
captions**. The preceding 1,189 catalog entries are identical. Both Water Blue
story routes now have text for the family encounters, ID cards, ship-parts quest,
prize game and radio warning. Later story banks and many graphical/roster labels
remain unfinished.

| Records | Added coverage |
| --- | --- |
| 883–957, 1001–1075 | R-3K, Kurumi, Mekao, J.D. and Don Oyaji encounters, rewards and rematches |
| 958–983 except 964, 1093–1118 except 1099 | Aniro's four-part quest, colored barriers, U-Manbo assembly and ship exchange |
| 984–997, 1119–1132 | Oban's two-box prize game, parts/Pearlton rewards and exhausted prizes |
| 998–1000, 1133–1135 | Unknown caller's warning about reviving Caramel |
| 1076–1092 | Regional hints, family order, barrier restrictions and cleared-area variants |
| 3675, 3680–3683, 3687, 3690–3693 | Ripple, four ship parts and five colored ID inventory labels |

There are 251 added story records and ten inventory labels. Source record 964
is a cut-message placeholder and remains untouched. Record 1099 contains only a
portrait command; it too remains untouched and is not counted as translated text.
The fourteen preceding Fire Blue cut placeholders also remain untouched.
Exact source duplicates reuse wording; differing control streams were adapted
separately. No new layout exception or codec change was needed.

## Wording and behavior

Provisional names are recorded beside their Japanese in `translation/glossary.json`:
R-3K, Don Oyaji, Kurumi, Mekao, J.D., Aniro, U-Manbo, Princess Oban and Nukinuki
Island. R-3K's mechanical katakana speech becomes uppercase. Mekao's deliberately
odd sentence endings retain short comic syllables. The Don's long list of
memories, streak/technique boasts and the assembly/cooking/hand-clapping jokes
are condensed to fit. The anonymous caller remains unidentified.

Ripple Caramela is the full treasure term; crowded dialogue, acquisition text
and the native inventory use Ripple. The four quest parts consistently use the
compact labels Helm, Engine, Screw and Oar in instructions, prize messages and
inventory. Their source U/Man/Bo/Go wordplay is noted in the glossary. Aniro
explicitly discards Oar during assembly in the original; the draft retains this.

The Pink ID from Aniro passes only pink barriers. R-3K gives Yellow ID, Kurumi
Blue ID, Mekao Green ID and J.D. Orange ID. Don Oyaji first gives just **one
Pearlton**, then insists on a second battle before yielding Ripple. Oban's fuel
prize remains **50 Pearlton**. Pearlton is fuel, distinct from G money. Kurumi's
five-times/ten-times strength claims are retained as dialogue, not verified stats.
The ship exchange retains Gyojin on the Dandy/Punch route and Doluppi on the
Mighty/Ram route; players can return to Aniro and swap again. Oban lets the player
choose one of two boxes, and her out-of-prizes message remains a separate branch.
No events, reward quantities, choices or record locations were changed.

All new messages preserve their original portrait, expression, color, page, line
and player-name commands with exact arguments and order. English fits the
original allocations, 16 cells per line and three nonempty lines per page.
Player-name substitutions reserve five cells. Record 831's existing anchored
page exception is inherited unchanged from the preceding milestone.

## Build and verification

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/water-blue-story-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/water-blue-story-alpha.z64 --patch local/water-blue-story-alpha.bps
```

Apply `releases/water-blue-story-alpha.bps` directly to the exact Japanese original;
do not stack patches. The target remains 32 MiB. Its MD5 is
`2B41A32E86413020B1F421456CDAD781`. The manifest records source, target and patch
hashes. CIC-6102 CRC1/CRC2 remain `FFA89600 C278C65F`.

The existing 115-test suite passes. The builder checks exact source bytes,
descriptors, control streams, widths, allocations and overlapping edits. Floating
IPS independently reproduces the final ROM from the BPS. chksum64 agrees with
its header in read-only mode. All preceding 1,189 catalog entries compare equal.
The original ROM and reference EEPROM remain intact.

## Runtime and recovery

The exact final ROM cold-booted with an isolated copy of the preserved native
EEPROM. File A retained day 2, 500G, the entered player name and Merlin. The file
menu, ship wake-up and pause menu rendered correctly. No savestate was loaded.
The reference, default working and isolated test EEPROM copies remain identical.
Evidence is under `local/water-blue-story-evidence/` in the encrypted archive.

Water Blue records 883–1135 and the ten inventory labels were not reached in this
run. Their battle, colored-barrier, parts/prize, ship-swap and warning branches
have build/control/width/allocation checks only. Prior evidence and states retain
their original ROM identities and cannot validate this ROM. Checks use the
supplied emulator environment, not hardware.

The encrypted archive is decrypted and compared byte-for-byte with its ZIP, then
restored into a separate empty directory, verifying all 568 payload files. The restored suite, reproducible build,
asset/evidence hashes, executable modes, library symlink and exact-ROM 16Kbit
EEPROM profile are checked. `BACKUP_MANIFEST.json` records the archived source
revision and each payload's size and hash.

## Next work

Continue the story bank at record 1136: Koron's island entry and Roulette Island,
leading toward Captain Ladder and the kidnapping plot. Play the new Water Blue
battles, colored barriers, parts/prize choices, ship exchanges and warning in both
routes. Earlier Fire Blue branches, including record 831's page split, still need
playthrough coverage. Graphical headings, roster names, the Parts frame, capacity
warnings and VS/Transfer Pak branches remain unfinished. Preserve the earlier
Dome three-versus-four-win source discrepancy until checked in play.
