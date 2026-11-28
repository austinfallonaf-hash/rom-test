# Sunny Blue variants alpha

This cumulative partial English draft adds **140 native records**, reaching
**2,917 native records, 832 UI strings, 299 choice blocks and three bitmap
captions**. All preceding 2,777 entries are identical. The alternate Sunny Blue
bank now covers the returning bosses, united Musketeers, finale and approach
choices, plus closing narration. This is not a complete game translation.

| Records | Added coverage |
| --- | --- |
| 2502–2593 | Alternate five-boss rematches and united Musketeers: 92 records |
| 2594–2635 | Alternate finale, Sun acquisition, Caramel and escape: 35 records |
| 2636 | Closing narration: 1 record |
| 2637–2648 | Alternate mystery transmissions and crew responses: 12 records |

Six cut-message placeholders (2603–2607, 2617) and portrait-only record 2601
remain untouched, including their descriptors. Of the additions, 102 have
byte-identical Japanese source in the preceding catalog and reuse that English.
The remaining 38 source variants/new narration were reviewed separately. There
are no new inventory labels. Earlier provisional terms and names remain.

## Source differences

Several boss variants have the same words but different portrait commands and
reset positions. Their English follows those source controls: Johnny's return,
loss and rematch; Mura's pride dialogue; Don Oyaji's permission to advance; and
Captain Ladder's refusal and farewell. Don's jokes and sea-themed baby names,
Linlin's Sun hint and the Musketeers' one-best-Robopon team remain. Alternate
2574 says the Musketeers will **rest for a while**, unlike main 2428's leaving
the sea. Their piracy renunciation and other exact-source dialogue are retained.

The alternate elder asks the hero to trust themself, resolve to win and obtain
Caramela, and reconsider the journey's purpose. This differs from the main
route's fulfill-your-dream instruction. Short hero responses 2597/2615 retain
only the confidence paragraph; the omitted main-route paragraphs are not added.
The dialogue uses the source's different portrait layouts and familiar voice.
Zero 2611 adds a full perfect-world paragraph before his empire declaration.
The finite-life argument in 2608 has different portrait/page placement, and
2610 is shorter than the main response. Existing main translations are unchanged.

Alternate 2631 explicitly says the hero neither spoke a wish nor held one in
mind. The revived Caramel, eye-reading joke, Sun reward and Zero's tomorrow/future
explanation otherwise reuse exact source where available. The alternate elder
asks what was wished, the child urges escape more briefly, and the rubble warning
has its own wording. No additional wish, rescue or outcome was invented.

Closing narration 2636 credits the player's courage, strength and moral resolve
with restoring tomorrow and lasting peace, then urges hope and fulfilling dreams
with one's own hands. The English condenses these as brave, strong and just.
The narration's resource position alone does not establish which route invokes
it; gameplay must confirm that. It retains all source pages, colors and three
entered-name occurrences, with five cells reserved for each name.

Alternate approach 2637 threatens **Ram, Mighty and Mikachi**, replacing the main
Punch/Dandy/Mikachi crew. The elder's acceptance stresses the player's own
conclusion, and refusal recalls the earlier vow. The child admits fear and
imagines being eaten by a scary person when retreating. These reactions remain
distinct from the main route's confidence and death warning.

## Record 2637's declared page

Ram (3), Mighty (6) and Mikachi (7) take 16 cells before separators. Record 2637
uses `layout_pages_before: [36]`, the same explicit placement as main 2490. One
`2001` is added immediately before Mikachi's original name-color start
`2003:0001` at source-control index 36. Ram/Mighty stay on the previous page;
Mikachi/the threat continue on the next. Both pages use two lines.

No codec changes or additional newline opt-ins were needed. The existing guard
rejects undeclared pages, changed commands/arguments, invalid anchors, other
colors/resets, line/page overflow and allocation growth. All other new records
have exact original control streams. Earlier page records 831/2041/2226/2490
are identical, making five declared anchored-page records total. The actual
restored ROM is checked for 2637's sole extra page and rejection without its
declaration. All five page cases still need gameplay inspection.

## Build and validation

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/sunny-blue-variants-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/sunny-blue-variants-alpha.z64 --patch local/sunny-blue-variants-alpha.bps
```

Apply `releases/sunny-blue-variants-alpha.bps` directly to the exact Japanese
original; do not stack patches. The 32 MiB target MD5 is
`2E67F7510BFE5AB6800A9A57CD2B3E0C`. The release manifest records source, target
and patch sizes and SHA-256 hashes. CIC-6102 CRC1/CRC2 remain
`FFA89600 C278C65F`.

All 117 tests pass. The builder checks exact source bytes, descriptors, controls,
widths, allocations and overlapping edits. Every record fits its original budget,
three nonempty lines per page and 16 cells per line. Floating IPS independently
reproduces the ROM from the BPS; read-only chksum64 agrees with the header. The
previous catalog is identical. The exact new ID set is 2502–2648 minus the seven
excluded records. All 102 exact-source reuses compare equal. Verification checks
actual encoded ROM bytes and descriptors for all 140 additions and unchanged
bytes/descriptors for the exclusions.

## Runtime and recovery

The exact final ROM cold-boots and loads an isolated native EEPROM copy. File A
retains day 2, 500G, the entered player name and Merlin. The English file-menu,
ship-wake and pause displays were inspected with Mupen64Plus/Glide64mk2.
No savestate was loaded or created, and no in-game save was attempted. The
original ROM and reference/default/isolated EEPROM hashes remain unchanged.
The exact-ROM profile retains 16Kbit EEPROM, two players and Transfer Pak
metadata. Screenshots, the completed log and file hashes are in
`local/sunny-blue-variants-evidence/`.

New alternate rematches, finale, closing narration and approach scenes were not
reached in playthrough. They have build validation only. Earlier regional scenes
and anchored pages still need gameplay checks. Historical states remain tied
to their exact ROMs and were not loaded on this build.

The AES-256 recovery archive decrypts byte-for-byte to its ZIP. Clean restoration
verifies all 721 payload files and passes all 117 tests, including reproducible
ROM/BPS/save checks, archived source revision, evidence hashes, executable modes,
the emulator library symlink and exact-ROM profile. It also checks the new IDs,
reuses, excluded bytes and 2637's exact page in the restored ROM. The existing
recovery passphrase stays outside Git. See `backups/README.md` and `RESTORE.md`.

## Next work

Translate remaining Dome lower-rank refusal 2719; it is the only untranslated
record in 2649–2807. Audit remaining native text and roster names from 2808.
Play both Sunny Blue routes, closing narration and approach choices, especially
2637 and earlier pages 831/2041/2226/2490. Graphical labels, Parts frame, capacity
warnings and VS/Transfer Pak branches remain unfinished.
