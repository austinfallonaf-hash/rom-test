# Fire Blue variants alpha

This cumulative partial English draft adds **204 native records**, reaching
**1,189 native records, 832 UI strings, 299 choice blocks and three bitmap
captions**. The preceding 985 catalog entries are identical. Both Fire Blue
story routes now have text, including their interludes and recruitment scenes;
this does not complete the game's graphical labels or later seas.

| Records | Added coverage |
| --- | --- |
| 680–699, 842–861 | Black Musketeers arrival, introductions and attempted treasure purchase |
| 700–704, 862–866 | Return route, refusal and overweight-ship messages |
| 705–720, 867–882 | Mikachi joins the Gyojin or Doluppi crew, refusals and gift |
| 721–803 | Alternate Henpei, Mark, Komura, Dongo and Mura encounter bank |
| 804–818 | Regional hints, four-island movement and quarter-opening gate puzzle |
| 819–841 | Alternate Gariman theft, return, reward and next-sea route bank |
| 2954 | Strawberry Mousse's compact native inventory label: Berry |

All 203 consecutive story records from 680 through 882 are included. Exact
source duplicates reuse previously checked wording; differing command streams
were adapted separately. The fourteen cut-message placeholders from the preceding
bank remain untouched (647, 648, 650, 651, 658–665, 667 and 669).

## Wording and layout

The provisional names Black Musketeers, Athos, Aramis, Dartagnan and Mikachi are
recorded alongside the Japanese in `translation/glossary.json`. Dartagnan is a
compact ASCII spelling that shares a 16-cell line with Aramis. The member named
ダルタニアン is retained. Two tiny reflection records use Black Trio.

Mikachi's Strawberry Mousse gift uses Berry in its six-glyph inventory allocation
and compact transfer messages. Fire Caramela still uses Fire in crowded lines.
Pearlton remains fuel, distinct from money. Gyojin/Punch/Dr. Dandy and
Doluppi/Ram/Dr. Mighty remain distinct route variants. The gate hints explain
that beating each of four islet battlers draws that islet inward and opens a
quarter of Mura's gate; all four are required. Muscle and fluke/frog wordplay is
condensed; baby speech and Dongo's chants remain phonetic.

Source record 831 lacks a page separator before its final paragraph, leaving six
lines on one page. Its catalog declares `layout_pages_before: [23]`: insert exactly
one page command immediately before original control index 23, a portrait command.
The codec expands the expected stream at that anchor. All original controls,
arguments and their order must still match, and undeclared extra pages fail.
The default remains strict. Tests cover malformed anchors, changed portraits,
extra or removed pages and allocation limits. The preceding release still
rebuilds byte-for-byte under this codec.

English remains within the original allocations, 16 cells per line and three
nonempty lines per page. Player names reserve five cells. No events, choices,
rewards or record locations were changed.

## Build and validation

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/fire-blue-variants-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/fire-blue-variants-alpha.z64 --patch local/fire-blue-variants-alpha.bps
```

Apply `releases/fire-blue-variants-alpha.bps` directly to the exact original
Japanese ROM; do not stack patches. The target remains 32 MiB. Its MD5 is
`9A031850377B72129E6EADEEB27A2A0A`. The manifest records source, target and patch
hashes. CIC-6102 CRC1/CRC2 remain `FFA89600 C278C65F`.

All 115 tests pass. The builder checks source bytes, descriptors, control streams,
widths, budgets and overlapping edits. Floating IPS independently reproduces the
final ROM and chksum64 agrees with its header in read-only mode. All 985 preceding
catalog entries compare equal. The original ROM and reference EEPROM are intact.

## Runtime and recovery

The exact final ROM cold-booted with an isolated copy of the preserved native
EEPROM. File A retained day 2, 500G, the entered player name and Merlin. The file
menu, ship wake-up and pause menu rendered correctly. No savestate was loaded.
The reference, default working and isolated test EEPROM copies remain identical.
Evidence is under `local/fire-blue-variants-evidence/` in the encrypted archive.

Records 680–882, the Berry gift/inventory and record 831's added page were not
reached in this run. They have build/control/width/allocation checks only. The
previous milestone's opening evidence remains historical; its exploration state
belongs only to MD5 `07EC747C6805124E327FC2A1872EED28` and cannot validate this ROM.
Checks use the supplied emulator environment, not hardware.

The encrypted archive is decrypted and compared byte-for-byte with its ZIP, then
restored into a separate empty directory, verifying all 551 payload files. The restored suite and reproducible
build, asset hashes, evidence hashes, executable modes, library symlink and
exact-ROM 16Kbit EEPROM profile are checked. The source revision and per-file
hashes are recorded in `BACKUP_MANIFEST.json`.

## Next work

Continue Water Blue's main story beginning at record 883 (R-3K, then Kurumi).
Play the new Fire Blue encounter, theft, reward, Musketeers and Mikachi branches,
including record 831's added page. Graphical headings, roster names, the shop
Parts frame, capacity warnings and VS/Transfer Pak branches remain unfinished.
The earlier Dome three-versus-four-win source discrepancy remains documented in
[the Dome notes](battler-dome-alpha.md).
