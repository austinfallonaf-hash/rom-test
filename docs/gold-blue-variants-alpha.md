# Gold Blue variants alpha

This cumulative partial English draft adds **180 native records**, reaching
**2,252 native records, 832 UI strings, 299 choice blocks and three bitmap
captions**. The preceding 2,072 entries are identical. Both Gold Blue routes,
regional hints and arrival/collision variants now have a draft. Land Blue begins
at native record 1972.

| Records | Added coverage |
| --- | --- |
| 1784–1906 except 1898–1900 | Alternate training/fighter encounters, Mighty/Linlin confrontation, reward and thaw/departure: 120 records |
| 1907–1923 | Regional hints and cleared-area reactions: 17 records |
| 1924–1971 except five portrait-only records | Alternate history/referral, collision, frozen arrival and repeated departure: 43 records |

Of the additions, 132 exactly match Japanese source in the preceding catalog
and reuse its English. The other 48 records contain 46 distinct source variants
or new hints; two repeat within this bank. There are no new inventory labels.
Records 1898, 1899, 1900, 1926, 1928, 1937, 1938 and 1945 contain only portrait
commands. Their complete payloads and eight-byte descriptors remain identical to
the original; they are excluded from translated-text counts. Earlier cut-message
and portrait-only exclusions remain unchanged.

## Wording and source details

Fu/Pao Tai's trial and rematches retain the mind, skill and body triad. The
shortened reactions to the hopping vampire, muscular fighter and drunken elder
fit their distinct source allocations. Mighty replaces Dandy in the Linlin
confrontation and has a separate paragraph urging the player to reclaim Gold
Caramela through his own strength. Linlin's rejection of balance, revenge vow,
the four-versus-one fragment count, Gold reward and thaw remain.

The new hints explain ice preventing ship steering and the pinball device
flinging ships around Jeekun Island. Other hints praise Linlin's kung-fu army,
celebrate its defeat, or contrast power bringing misery with power bringing joy.
The Gold Caramela rejects unworthy owners; Linlin's ownership froze the sea,
while the restored sea shows the player's worth. Caramel's revival remains a
possibility. Another speaker's "anything goes if you win" joke remains distinct.

Record 1913 retains the water and one-inch-punch references. Its Japanese film
puns refer to The Way of the Dragon, Enter the Dragon and The Big Boss; compact
English uses **Way of Robopon**, **Enter Robopon** and **The Big Robopon**. The
glossary documents this adaptation. The combat narrator keeps kung-fu cries,
blood, flying fists, clashing moves and the return-from-danger reaction.

Existing provisional names and compact Gold, Mt. Despera, Nikuniku, Musketeers
and Black Trio forms remain. Main farewell 1724 uses character-name color for
Caramela, while alternate 1896 uses treasure color; both source choices remain.
Records 1902/1903 retain their unusual source page ending before the final
portrait reset. Native roster/speaker labels remain Japanese.

Every new portrait, expression, color, page, line and player-name command preserves
its exact arguments and order. English fits the original allocations, 16 cells
per line and three nonempty lines per page. Player-name substitutions reserve
five cells. No new layout exception, codec change or record relocation was needed.
Record 831's inherited page exception is unchanged. Story events, battle
conditions, rewards and character transfers are unchanged.

## Build and verification

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/gold-blue-variants-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/gold-blue-variants-alpha.z64 --patch local/gold-blue-variants-alpha.bps
```

Apply `releases/gold-blue-variants-alpha.bps` directly to the exact Japanese
original; do not stack patches. The target remains 32 MiB, MD5
`905379262613E6AE8386FBB8AA821D1B`. The manifest records source, target and patch
hashes. CIC-6102 CRC1/CRC2 remain `FFA89600 C278C65F`.

All 115 existing tests pass. The builder checks exact source bytes, descriptors,
controls, widths, allocations and overlapping edits. Floating IPS independently
reproduces the final ROM from the BPS. Read-only chksum64 agrees with its header.
All preceding entries compare equal, and the eight portrait-only records'
complete descriptors and payloads match the original. Original ROM and reference
EEPROM remain intact.

## Runtime and recovery

The exact final ROM cold-boots from an isolated native EEPROM copy. File A retains
day 2, 500G, the entered player name and Merlin. The English file-menu prompt,
ship wake and pause rendering were inspected with the supplied Mupen64Plus and
Glide64mk2. No savestate was loaded or created; no in-game save was attempted.
Original ROM and reference/default/isolated EEPROM hashes are unchanged. The
exact-ROM profile retains 16Kbit EEPROM, two players and Transfer Pak metadata.
Screenshots, completed log and file hashes are in `local/gold-blue-variants-evidence/`.

The new alternate Gold Blue scenes, regional hints and arrival/collision variants
were not reached in playthrough. Their text has build validation only. Both Gold
Blue routes, Roulette and earlier Water/Fire Blue scenes still await gameplay
checks. Historical states retain their original ROM identities and were not used
for current validation.

The AES-256 recovery archive decrypts byte-for-byte to its ZIP. A clean restore
verifies all 636 payload files and passes all 115 tests, including ROM/BPS/save
checks, executable modes, the emulator library symlink and exact-ROM profile.
The manifest records the archived source revision. The passphrase stays outside
Git; earlier ROMs rebuild from their cumulative patches. See `backups/README.md`.

## Next work

Continue Land Blue at native record 1972. Play both Gold Blue routes, training,
fighters, Linlin, reward/thaw, regional hints, pinball/arrival/collision and
departure scenes. Both Roulette routes and earlier Water/Fire Blue branches
still need playthrough checks. Graphical/roster labels, the Parts frame, capacity
warnings and VS/Transfer Pak branches remain. Preserve the Dome three-versus-four
win discrepancy and check record 831's inherited page split.
