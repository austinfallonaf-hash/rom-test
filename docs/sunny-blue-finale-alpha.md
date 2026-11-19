# Sunny Blue finale alpha

This cumulative partial English draft adds **47 native records**, reaching
**2,777 native records, 832 UI strings, 299 choice blocks and three bitmap
captions**. All preceding 2,730 entries are identical. It covers the main finale,
escape and approach bank; alternate Sunny Blue starts at record 2502.

| Records | Added coverage |
| --- | --- |
| 2448–2489 | Final encouragement, Dr. Zero, battle outcomes, Sun reward, Caramel and escape: 35 records |
| 2490–2501 | Mystery transmissions and crew approach/retreat responses: 12 records |

Seven cut-message placeholders remain untouched: 2455, 2457–2461 and 2471.
There are no portrait-only exclusions or new inventory labels. Sun inventory
record 3679 was already translated; acquisition 2477 now uses the same compact
Sun form. All 47 new source strings differ from the preceding catalog; matching
new encouragement 2449/2467 shares its English.

## Story and wording

Dr. Zero claims the top battler rank Greatest 1, describes replacing his human
body with machinery and seeks eternal life and a Zero empire. The hero argues
that finite lives make each moment precious. Zero's loss, the plea to recover
his human heart and his gradual recognition of it remain distinct pages.
He yields Sun Caramela, bringing all seven together. The source's two outcomes
are preserved: his victory claims the fragments/empire, while his defeat leads
to the reward and revival.

Caramel is the first Robopon, fallen from space, who can finally return home.
His hesitant, folksy speech uses stutters and informal English rather than an
asserted real-world dialect. All repeated requests to open the player's eyes
and move closer remain, along with his joke that he cannot read the wish.
The hero never states a spoken wish. During the collapse, Zero recalls the
finite-life argument and chooses to die like a human. He identifies what is
in the player's eyes as tomorrow and the future beyond it. The ambiguity about
the wish is retained. No additional rescue, death scene or epilogue was invented.

Approach transmissions threaten the player and Punch, Dandy and Mikachi, demand
six fragments, promise familiar opponents and leave the decision to advance to
the player. Crew responses retain the earlier promise, mutual dependence and
fear of losing the player, as well as the different retreat reactions.

The English is condensed to the original allocations. Long ellipsis runs are
shortened, while all original page and portrait/color/name commands retain their
order. No events, rewards or script positions are changed. Dr. Zero, Greatest 1
and Caramel's voice remain provisional; the glossary records these decisions.

## Record 2490's declared page

The three names Punch (5), Dandy (5) and Mikachi (7) require 17 cells even before
separators. Their source puts all three colored names on one line. Record 2490
therefore declares `layout_pages_before: [36]`. It adds one `2001` immediately
before the original Mikachi name-color command `2003:0001` at source-control
index 36. The ship/Punch/Dandy text occupies two lines; Mikachi and the threat
continue on the next page, also using two lines.

The codec now accepts an explicit unpaged name-color start as an anchor, in
addition to the earlier portrait anchors. It still rejects resets, other colors,
already-paged anchors, changed commands/arguments, arbitrary extra pages,
record growth and overlong lines/pages. Two focused tests check a complete cast
list, exact control expansion, failure without the declaration, altered colors,
extra pages, overlong names, invalid anchors and allocation overflow.

All other new records have exact original control streams. Earlier exceptions
831/2041/2226 are identical, making four declared anchored-page records total.
The new page needs gameplay inspection; build verification alone cannot confirm
how the continuation renders in the late-game scene.

## Build and checks

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/sunny-blue-finale-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/sunny-blue-finale-alpha.z64 --patch local/sunny-blue-finale-alpha.bps
```

Apply `releases/sunny-blue-finale-alpha.bps` directly to the exact Japanese
original; do not stack patches. The 32 MiB target MD5 is
`4FFCDEDA9119415A1DDE2D5F2823316D`. The release manifest records source, target
and patch sizes and SHA-256 hashes. CIC-6102 CRC1/CRC2 remain
`FFA89600 C278C65F`.

All 117 tests pass. The builder checks exact source bytes, descriptors, controls,
widths, allocations and overlapping edits. Every record fits its original budget,
three nonempty lines per page and 16 cells per line; names reserve five cells.
Floating IPS independently reproduces the ROM from the BPS, and read-only
chksum64 agrees with the header. The previous catalog compares equal. The new
ID set is exactly 2448–2501 minus the seven cut placeholders. Verification
checks the actual encoded ROM bytes and descriptors for all 47 additions,
including 2490's sole extra page and rejection without its declaration.

## Runtime and recovery

The exact final ROM cold-boots using an isolated native EEPROM copy. File A
retains day 2, 500G, the entered player name and Merlin. The English file-menu,
ship-wake and pause displays were inspected with Mupen64Plus/Glide64mk2.
No savestate was loaded or created, and no in-game save was attempted. The
original ROM and reference/default/isolated EEPROM hashes remain unchanged.
The exact-ROM profile retains 16Kbit EEPROM, two players and Transfer Pak
metadata. Screenshots, the completed emulator log and file hashes are in
`local/sunny-blue-finale-evidence/`.

The new finale, acquisition, revival, escape and approach scenes were not reached
in playthrough. They have build validation only. Earlier regional scenes and
anchored pages still need gameplay checks. Historical states remain associated
with their exact ROMs and were not loaded on this build.

The AES-256 recovery archive decrypts byte-for-byte to its ZIP. Clean restoration
verifies all 704 payload files and passes all 117 tests, including reproducible
ROM/BPS/save checks, archived source revision, evidence hashes, executable modes,
the emulator library symlink and exact-ROM profile. It also checks all new
control streams and 2490's exact page in the restored ROM. The existing recovery
passphrase stays outside Git. See `backups/README.md` and `RESTORE.md`.

Continue alternate Sunny Blue at 2502. Play the main rematches, finale and
approach choices, especially 2490 and earlier pages 831/2041/2226. Graphical/roster
labels, Parts frame, capacity warnings and VS/Transfer Pak branches remain.
