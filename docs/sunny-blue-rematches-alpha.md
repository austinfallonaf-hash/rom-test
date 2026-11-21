# Sunny Blue rematches alpha

This cumulative partial English draft adds **93 native records**, reaching
**2,730 native records, 832 UI strings, 299 choice blocks and three bitmap
captions**. All preceding 2,637 entries are identical. The final confrontation
begins at record 2448 and remains untranslated.

| Records | Added coverage |
| --- | --- |
| 2356–2390 | Johnny, Mura, Don Oyaji, Captain Ladder and Linlin rematches: 35 records |
| 2391–2438 | United Black Musketeers battle, aftermath and farewell: 48 records |
| 2439–2447 | Repeat confrontation and battle prompt: 9 records |
| 3679 | Sun fragment inventory label: 1 record |

No cut-message or portrait-only exclusions occur in this bank. Six exact-source
Battle? prompts reuse the preceding catalog; repeated new dialogue also reuses
its English. No new anchored pages or codec changes were needed. Earlier page
exceptions in 831, 2041 and 2226 are unchanged and still await gameplay checks.

## Wording and source details

Johnny returns for a decisive rematch and repays his humiliation. Mura puts pride
at stake, retains the source's twice/no-third-time repetition and learns to
advance without fear. Captain Ladder tests whether the player deserves to revive
Caramel. Linlin questions the six fragments' loyalty, admits the importance of
mind, skill and body, and urges the player to obtain **Sun Caramela**, the seventh
fragment. This scene does not award it. Inventory record 3679 uses **Sun**.

Don Oyaji deliberately mangles words and digresses. Orange/fatten/revenge and
back/frog nonsense are compact English adaptations, not literal reproductions
of every Japanese pun. The do-it wordplay and absurd Joyland exclamation remain.
His baby names retain the Japanese sea-food jokes: Kanio, Sabazo, Uniko, Sazae
and Wakame. The thousand-days and ten-month asides, already-lost-twice admission,
anger at the plot, frightened bowel accident and warning about the boss remain.
These comic oddities are intentional; names and adaptations are provisional.

The Black Musketeers explain the player's hint: they have only fought separately.
Each now contributes **one best Robopon** to a single team. Losing stakes all six
Caramela; winning earns the seventh-fragment challenge. Black Trio is the compact
name used in crowded records. Their defeat leads to disbanding, leaving the sea
for a while and renouncing piracy for an honest life. It does not imply suicide.
Their gratitude and warning about the unknown summoner above lead into 2448.
Record 2425's divine wind means miraculous favorable luck. Ocean Blue in 2430
is retained as a farewell to the sea/world; it does not establish another region.

## Build validation

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/sunny-blue-rematches-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/sunny-blue-rematches-alpha.z64 --patch local/sunny-blue-rematches-alpha.bps
```

Apply `releases/sunny-blue-rematches-alpha.bps` directly to the exact Japanese
original; do not stack patches. Target MD5 is
`B38C0083DD0D17C041CE566669D7C9E3`. Source, target and patch sizes and SHA-256
hashes are recorded in the release manifest. CIC-6102 CRC1/CRC2 remain
`FFA89600 C278C65F`.

All 115 existing tests pass. The builder checks original/source bytes,
descriptors, controls, width, allocation and overlapping edits. All new original
control commands and arguments retain their order. Every record fits its
original allocation, three nonempty lines per page and 16 cells per line;
player names reserve five cells. Story events, rewards and record positions are
unchanged. Floating IPS independently reproduces the ROM from the BPS, and
read-only chksum64 agrees with the header. Original ROM and reference save hashes
remain intact. The exact new ID set is 2356–2447 plus 3679.

## Runtime and recovery

The exact final ROM cold-boots from an isolated native EEPROM copy. File A retains
day 2, 500G, the entered player name and Merlin. The English file-menu prompt,
ship wake and pause displays were inspected using Mupen64Plus/Glide64mk2.
No savestate was loaded or created; no in-game save was attempted. Reference,
default working and isolated EEPROM hashes remain unchanged. The exact-ROM
profile retains 16Kbit EEPROM, two players and Transfer Pak metadata. Screenshots,
completed emulator log and hashes are in `local/sunny-blue-rematches-evidence/`.

The new Sunny Blue rematches and Sun inventory display were not reached in
playthrough. They have build validation only. Earlier Land/Gold Blue, Roulette
and Water/Fire Blue scenes also await gameplay checks. Historical savestates
retain their exact ROM identities and were not used on this build.

The AES-256 recovery archive decrypts byte-for-byte to its ZIP. A clean restore
verifies all 687 payload files and passes all 115 tests, including reproducible
ROM/BPS/save checks, source revision, executable modes, the emulator library
symlink, exact-ROM profile and evidence hashes. The recovery passphrase stays
outside Git. See `backups/README.md` and `RESTORE.md`.

Continue the final confrontation at 2448. Play these rematches and inspect earlier
anchored pages 831/2041/2226. Graphical/roster labels, Parts frame, capacity
warnings and VS/Transfer Pak branches remain unfinished.
