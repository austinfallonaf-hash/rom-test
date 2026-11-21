# Land Blue variants alpha

This cumulative partial English draft adds **199 native records**, reaching
**2,637 native records, 832 UI strings, 299 choice blocks and three bitmap
captions**. All preceding 2,438 entries are identical. Both Land Blue routes,
regional hints and alternate Kujiran/warning/departure scenes now have a draft.
The Sunny Blue/rematch bank begins at record 2356.

| Records | Added coverage |
| --- | --- |
| 2157–2301 | Alternate false/true Musketeers, shallow/deep encounters and rematches: 145 records |
| 2302–2317 | Regional hints and cleared-area reactions: 16 records |
| 2318–2355 | Alternate rising-island tutorial, Kujiran, warning, Earth reward and departure: 38 records |

Of the additions, 168 have byte-identical Japanese source in the preceding
catalog and reuse its English. The other 31 source variants/new hints were
reviewed separately. There are no new inventory labels, cut-message exclusions
or portrait-only exclusions. Earlier excluded records remain unchanged.

## Source differences and wording

The Musketeers retain the time-killing/crushing joke, impostor confessions,
"Go for block!" malapropism, serious deep-area battles and erasure threats.
The alternate short loss reactions have different portrait/line layouts and are
adapted to their own source controls. Records 2239 and 2244 say Gold Blue in their
shallow-area explanation; this matches their source, while main 2054 says Land
Blue. The earlier source-location discrepancy remains documented.

The hints explain islands rising/sinking and the inconvenience for residents,
suspected impostors, fear of Sunny Blue and Mt. Despera, and the search for Earth
Caramela. They distinguish clearing an island to reveal another, moving away to
make an island rise, and approaching one that sinks. The ship hint separates
shallows from depths and mentions modern technology behind the better Robopon
ship. Cleared-area reactions recognize the upgraded vessel and Earth reward.

The alternate discovery correctly identifies **Kujiran**; it has no Doluppi joke
like main record 2130. The boarding/decline/swap prompts retain their distinct
lengths. Warning **2346 uses the entered-name command**, unlike main warning 2145,
which literally says Gria. Both forms are retained. Ram's fearful reaction,
Mighty's one-fragment-remaining warning and the shorter launch sequence remain.
The glossary records the variable-name and island-suffix differences.

Earth remains the sixth fragment; it alone grants Mt. Despera entry without the
other five, as the source says. Existing provisional names and compact Earth,
Mt. Despera and Black Trio forms remain. Roster/speaker labels remain Japanese.

## Anchored page in 2226

Record 2226 has exactly the same source text and bytes as 2041, including its
unseparated paragraphs. It reuses the English and `layout_pages_before: [3]`.
This adds one `2001` command immediately before the original `200A:0001` portrait
at source-control index 3. No codec change was needed. Existing exceptions in
831 and 2041 are unchanged, making three declared anchored-page records in total.

Verification confirms the control stream differs only by that exact page addition
and rejects encoding without the declaration. All other original commands and
arguments retain their order. Other new control streams remain exact. Every
record fits its original allocation, three nonempty lines per page and 16 cells
per line; player names reserve five cells. Story events, rewards, ship transfers
and record positions are unchanged. All three page cases still need playthrough.

## Build and verification

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/land-blue-variants-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/land-blue-variants-alpha.z64 --patch local/land-blue-variants-alpha.bps
```

Apply `releases/land-blue-variants-alpha.bps` directly to the exact Japanese
original; do not stack patches. The target remains 32 MiB, MD5
`85BA29DDB5806AAF7EAC1A57D83D8B29`. The manifest records source, target and patch
hashes. CIC-6102 CRC1/CRC2 remain `FFA89600 C278C65F`.

All 115 existing tests pass. The builder checks exact source bytes, descriptors,
controls, widths, allocations and overlapping edits. Floating IPS independently
reproduces the final ROM from the BPS. Read-only chksum64 agrees with its header.
All preceding entries compare equal. The new ID set is exactly 2157–2355, and
all 168 reused source byte strings and translations compare equal. Original ROM
and reference EEPROM remain intact.

## Runtime and recovery

The exact final ROM cold-boots from an isolated native EEPROM copy. File A retains
day 2, 500G, the entered player name and Merlin. The English file-menu prompt,
ship wake and pause rendering were inspected with supplied Mupen64Plus/Glide64mk2.
No savestate was loaded or created; no in-game save was attempted. Original ROM
and reference/default/isolated EEPROM hashes are unchanged. The exact-ROM profile
retains 16Kbit EEPROM, two players and Transfer Pak metadata. Screenshots,
completed log and file hashes are in `local/land-blue-variants-evidence/`.

New alternate Land Blue scenes, regional hints and 2226's added page were not
reached in playthrough. They have build validation only. Both Land Blue routes,
Gold Blue, Roulette and earlier Water/Fire Blue scenes await gameplay checks.
Historical states retain their original ROM identities and were not used for
current validation.

The AES-256 recovery archive decrypts byte-for-byte to its ZIP. A clean restore
verifies all 670 payload files and passes all 115 tests, including ROM/BPS/save
checks, executable modes, the emulator library symlink and exact-ROM profile.
It also checks 2226's exact extra page in the actual restored ROM. The manifest
records the archived source revision. The passphrase stays outside Git. Verified
superseded staging ZIPs and duplicate older restore trees were cleared, retaining
their manifests and preserving unmatched files. See `backups/README.md` for
recovery and retention instructions.

## Next work

Continue Sunny Blue/rematch text at record 2356. Play both Land Blue routes,
regional rise/sink gates, Kujiran choices, Earth reward, warnings and departure.
Inspect 2226/2041's pages, the sea-name discrepancy and the literal/variable name
warnings. Both Gold Blue routes, Roulette and earlier Water/Fire Blue branches
still await playthrough. Graphical/roster labels, the Parts frame, capacity
warnings and VS/Transfer Pak branches remain. Preserve the Dome three-versus-four
win discrepancy and inspect record 831's inherited page split.
