# Land Blue story alpha

This cumulative partial English draft adds **186 native records**, reaching
**2,438 native records, 832 UI strings, 299 choice blocks and three bitmap
captions**. All preceding 2,252 entries are identical. The main Land Blue route
now has a draft; the alternate bank begins at record 2157.

| Records | Added coverage |
| --- | --- |
| 1972–2013 | False Musketeers, panicked challenges, wins/losses, confessions and rematches: 42 records |
| 2014–2066 | True Musketeers in the shallows, Earth search and deep-area warning: 53 records |
| 2067–2116 | Deep-area rematches and their stronger threats/reactions: 50 records |
| 2117–2135 | Rising-island tutorial, better-ship requirements, Kujiran discovery and boarding choices: 19 records |
| 2136–2156 | Sixth-fragment information, mysterious call, Earth reward and Sunny Blue departure: 21 records |
| 3678 | Eight-cell inventory label: Earth |

There are no cut-message or portrait-only exclusions in the new bank. Earlier
cut/portrait-only exclusions remain unchanged. English fits the original record
allocations; no text records or event logic were relocated.

## Wording and source details

The false Musketeers retain their fear, attempts at grand speech, accidental
celebration and confession. Their "Go for block!" misstatement is preserved
instead of silently correcting it to "Go for broke!" The real Musketeers' time-
killing/crushing joke, irritation, serious rematches and threats to erase the
player remain. Deep-area dialogue retains the life-or-death stakes.

The tutorial distinguishes islands that rise near ships from those unlocked by
defeating a battler. The present vessel can reach the shallows; the depths require
a better ship. **Kujiran** is the provisional whale-shaped Robopon/ship name.
Doluppi in record 2130 is a false identification followed by an explicit joke and
correction. Boarding, declining and later ship-change prompts remain distinct.
**Pukkapuka Island** preserves the rising islands' floating wordplay.

**Earth Caramela** is the sixth fragment, shortened to **Earth** in crowded
dialogue, acquisition text and inventory. Record 2141 explicitly says it alone
allows entry to Mt. Despera without the other five Caramela. The source's claims,
reward order and departure toward the final sea, Sunny Blue, are retained.
The mountain remains cursed with an enticing secret, and one final fragment
remains after Earth. Names remain provisional; roster/speaker labels are Japanese.

Record 2054 says Land Blue, while repeat record 2059 says Gold Blue. Both source
locations are retained pending gameplay review. Warning 2145 literally addresses
Gria, rather than invoking the player-name command; English retains that hardcoded
name. Actual player-name substitutions in the other records remain variables.

## Guarded page addition in 2041

Record 2041 has no explicit page separator between its two paragraphs. Keeping
its line breaks produces more than three nonempty lines under the existing text
validator. This entry declares `layout_pages_before: [3]`, adding one `2001` page
command immediately before the original `200A:0001` portrait at source-control
index 3. It uses the existing anchored-page mechanism; no codec change was needed.

The record fits its original allocation, and its original commands/arguments
retain their order. Verification confirms the control stream differs only by
this exact page addition and that encoding without the declaration is rejected.
Record 831's earlier exception is inherited unchanged. All other new page, line,
portrait, expression, color and name commands retain their exact source streams.
Each page fits three nonempty lines of 16 cells, reserving five for entered names.
Both page exceptions still need gameplay inspection.

## Build and verification

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/land-blue-story-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/land-blue-story-alpha.z64 --patch local/land-blue-story-alpha.bps
```

Apply `releases/land-blue-story-alpha.bps` directly to the exact Japanese original;
do not stack patches. The target remains 32 MiB, MD5
`0838AE41F1BFBFE9D5B45FADBC6B66A1`. The manifest records source, target and patch
hashes. CIC-6102 CRC1/CRC2 remain `FFA89600 C278C65F`.

All 115 existing tests pass. The builder checks exact source bytes, descriptors,
controls, widths, allocations and overlapping edits. Floating IPS independently
reproduces the final ROM from the BPS. Read-only chksum64 agrees with its header.
All preceding entries compare equal, and the new ID set is exactly 1972–2156
plus 3678. Original ROM and reference EEPROM remain intact.

## Runtime and recovery

The exact final ROM cold-boots from an isolated native EEPROM copy. File A retains
day 2, 500G, the entered player name and Merlin. The English file-menu prompt,
ship wake and pause rendering were inspected with supplied Mupen64Plus/Glide64mk2.
No savestate was loaded or created; no in-game save was attempted. Original ROM
and reference/default/isolated EEPROM hashes are unchanged. The exact-ROM profile
retains 16Kbit EEPROM, two players and Transfer Pak metadata. Screenshots,
completed log and file hashes are in `local/land-blue-story-evidence/`.

New Land Blue scenes, the Earth inventory label and 2041's added page were not
reached in playthrough. They have build validation only. New Land Blue, both Gold
Blue routes, Roulette and earlier Water/Fire Blue scenes still await gameplay
checks. Historical states retain their original ROM identities and were not used
for current validation.

The AES-256 recovery archive decrypts byte-for-byte to its ZIP. A clean restore
verifies all 653 payload files and passes all 115 tests, including ROM/BPS/save
checks, executable modes, the emulator library symlink and exact-ROM profile.
It also checks 2041's exact extra page in the actual restored ROM. The manifest
records the archived source revision. The passphrase stays outside Git. Verified
superseded staging ZIPs were cleared before packaging to preserve disk space.
See `backups/README.md` for recovery and retention instructions.

## Next work

Continue alternate Land Blue at record 2157. Play the impostors, true Musketeers,
shallows/depths, rising-island gates, Kujiran boarding/ship swaps, Earth reward,
warning and Sunny Blue departure. Inspect 2041's added page and the 2054/2059 sea
name discrepancy. Both Gold Blue routes, Roulette and earlier Water/Fire Blue
branches still await playthrough. Graphical/roster labels, the Parts frame,
capacity warnings and VS/Transfer Pak branches remain. Preserve the Dome
three-versus-four-win discrepancy and inspect record 831's inherited page split.
