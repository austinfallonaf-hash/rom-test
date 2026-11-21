# Native story text and opening narration

## Verified resource layout

The Japanese dialogue is not missing or necessarily compressed. This resource
uses big-endian 16-bit indices into a custom font map:

- Record count: 4,115 (`0x1013`), header at ROM `0x18DF9C0`.
- Record table: `0x18DF9C8`, eight bytes per record: byte length, then byte offset
  relative to the pool. Both fields are big-endian unsigned 32-bit integers.
- Text pool: `0x18E7A60`, ending at `0x19560C2`.
- Font map: `0x19710D0`, 272 two-byte Shift-JIS entries.
- Font bitmaps: `0x19712F8`, 72 bytes per 12x12 CI4 glyph.

Rice texture dumping (`--set Video-Rice[DumpTexturesToFiles]=True`) provided a
12x12 glyph that matched ROM `0x1975990`. Its index is 251, and the map's index
251 is で. Adjacent glyphs and complete decoded narration confirmed the mapping.
The first 95 indices correspond to printable ASCII minus 32, using fullwidth
Japanese code points in the mapping table. The narration builder uses these
indices directly for English.

`python -m tools.story_text local/original.z64 --output local/story-records.json`
exports all 4,115 records without changing the ROM. This is a structural decode,
not 4,115 translated lines. Words above the font range are shown as `<200A>` and
similar tokens. Their arguments/semantics have not all been parsed. The builder
refuses to edit records containing such words.

## Opening alpha

`translation/intro.json` contains 66 opening-caption records. These form the
opening narration, from cannon fire through the legend of Caramel and the seven
Caramela. English is a condensed draft constrained by each original line's glyph
budget. It preserves the principal story beats; terminology and wording remain
subject to review. Cabin dialogue after the prologue remains Japanese.

Each translated record stays in its original allocation. Its byte-length field
is updated to the English length, its pool offset remains unchanged, and unused
space is padded with blank glyphs. Original source metadata, glyph bytes, and ROM
hash are guarded. Narration lines are limited to 16 cells and never exceed their
original byte budget. No resource expansion, executable patch, or N64 checksum
change is needed.

The edits reside beyond IPS's 24-bit address limit, so this cumulative release
uses **BPS**, not IPS. It includes the eleven save-menu translations; apply it to
the exact original ROM, not to a ROM already patched with the menu IPS.

Build:

```sh
python -m tools.build_story local/original.z64
```

Outputs are `local/intro-alpha.z64` and `local/intro-alpha.bps`. The BPS writer
uses SourceRead and TargetRead commands and stores source, target, and patch CRCs.
An independently built Floating IPS (Alcaro/Flips) applied the generated BPS
successfully; its output compared byte-for-byte equal to the generated ROM.

The original source ROM and checksum-covered first MiB remain unchanged. The
suite has 31 passing tests, including BPS integer vectors and footer checksums,
large offsets, source metadata guards, glyph budgets, descriptor updates,
control-bearing record rejection, and the earlier menu checks.

## Continuation notes

The first cabin dialogue is in records 189 onward. Record 192 contains the
brothers' exchange about going to verify Caramel's existence. Record 198 is the
ship computer's name/password instruction; 199 is confirmation, 200 retries,
and 201 starts the ship. Records 202 onward cover the accidental departure.
Those records contain control words and parameters; the current builder refuses
them, rather than interpreting parameters as printable glyphs. Preserve speaker,
portrait, color, page, variable-name, and line commands when adding support.

A baseline run reached the name-entry screen (local image
`local/tutorial-09.png`). Shift-JIS UI labels are at `0x1C11E0` (hiragana),
`0x1C11EC` (katakana), `0x1C11F8` (name), `0x1C1200` (name entry),
`0x1C1218` (confirm), `0x1C1224` (delete), and `0x1C1230` (space). The grid and
name storage expect further investigation before replacing kana with English.
Automated A presses altered only the local test name. No completed in-game save
or save/load cycle has been validated.

Rice dumps remain outside the repository under
`/home/agent/.local/share/mupen64plus/texture_dump/Robopon64/`. Font matching uses
the first **12x12** pixels of the 13x13 dumped texture; the extra row/column can
include neighbouring glyph data. Do not treat those pixels as part of the glyph.

Use a cold boot for validation of each new ROM build. Emulator savestates can
retain loaded text from an older build and are not evidence of fresh ROM loading.

## Runtime checks for this build

A cold boot of `intro-alpha.z64` reached the English save menu and started a new
game. Screenshots captured translated cannon-fire captions, the pirates' return
to their senses, the naming of Caramel, and the final legend text. Caption
centering and line breaks remained within the original screen layout. The final
caption sequence advanced to the closing book animation. This is representative
visual validation and an opening-sequence traversal, not a full-game test or a
word-by-word review of every captured frame.

The tested build subsequently entered the first cabin dialogue without a crash.
A local checkpoint is `local/cabin-intro-alpha.st0` for this exact ROM build.
Use it for exploration, and cold-boot any newly translated build for validation.

## Explicit layout pages in later catalogs

The current codec preserves the complete original control stream and permits
additional pages only at declared source-control indices in `layout_pages_before`.
An anchor may precede an unpaged original portrait (`200A`) or a name-color start
(`2003:0001`). The latter supports full English cast names, notably 2490's
Punch/Dandy/Mikachi list. Other color values, resets and already-paged anchors
are rejected. This declaration does not authorize changing arguments, removing
commands, adding arbitrary pages, exceeding three lines/16 cells or growing the
record. Source metadata and the final ROM bytes remain independently checked.
See `docs/sunny-blue-finale-alpha.md` for the exact 2490 addition and runtime limit.

## Native label storage in translated padding

Plain labels can declare `storage: {"record_id": 2376, "byte_offset": 788}` to
borrow an aligned unused tail from a translated, non-relocated donor. The label
keeps its guarded original metadata; its final descriptor receives the new byte
count and pool-relative pointer. The donor's active bytes and descriptor remain
unchanged. No ROM/pool expansion is used. Labels remain ASCII, at most 16 cells.
Malformed/overlapping storage, live-text overlap, overflow and control-bearing
labels are rejected. Future donor growth must fail until labels are repacked.
See `docs/roster-names-alpha.md` for the ledger and separate reader-preview proof.
Bot-name command `200B:0007` reserves eleven cells for the default translated
roster; player-name argument 0 stays five and dynamic item 6 reserves sixteen.

## Fixed minigame instruction grids

Records 3323–3337 use `kind: fixed_grid`, with newline-separated ASCII rows in
`translation`. Their readers copy rows of a fixed size, independent of dialogue
line controls. Records 3323–3327 are seven rows of ten glyphs; even records
3328–3336 are three rows of 21, and odd records 3329–3337 are three rows of 15.
`tools/fixed_grid.py` permits only these IDs and exact source dimensions. It
rejects source controls, wrong row counts, overwide rows and nonprintable/non-ASCII
targets. Rows are right-padded with blank glyphs and encoded at their original
full size. Descriptor counts and pointers remain unchanged; newline separators
do not become `2000` controls. This path does not relax dialogue or label limits.
See `docs/minigame-guide-alpha.md` for reader locations and runtime coverage.

## Bot-book biography lines in remaining ROM padding

The book reader at `0x109BB0–0x109C88` draws four separate records per entry:
`3694 + 4 * selected_entry + row`, for rows 0–3. Text begins at native x=52,
y=166+14*row. Source records 3694–3877 have 12–18 glyphs apiece and contain no
controls. These are independent length-delimited lines, unlike the fixed grids.

`kind: "book_line"` is restricted to those 184 IDs. It accepts 1–36 printable
ASCII cells and requires the exact horizontal-scale edit at `0x109C04` from
`3C013F80` (1.0) to `3C013F00` (0.5). Vertical scale, row positions, record-ID
calculation and native draw call remain unchanged. At six pixels per Latin
cell, 36 cells fit the source's 216-pixel maximum. Generic labels retain their
sixteen-cell guard; fixed-grid shapes and dialogue rules remain separate.

Each line declares an integer `book_storage_offset`, aligned to eight bytes,
inside `0x1FFD3D0–0x2000000`. This is original 0xFF padding after the existing
RAW2 graphic, which ends at `0x1FFD3C4`. The builder verifies the original padding,
zero-pads each allocation to eight bytes for the native reader, redirects its
count/pool-relative descriptor and leaves its original Japanese slot intact.
It rejects missing/misaligned/out-of-range/occupied placements, overlapping edits,
legacy donor storage on book lines, and book offsets on other kinds. These lines
are not donors. Graphics and layout edits share the same overlap guards.

The native descriptor loader at `0x470DC` uses the full 32-bit pool-relative
pointer and rounds the allocation size to eight bytes; the glyph loop consumes
only the declared count. No pointer-width change, compression, interpreter hook,
ROM-size increase or save-format change is needed. The book occupies 11,248 bytes
through `0x1FFFFC0`; the final 64 bytes stay 0xFF. Preserve these placements when
continuing. Longer wording or a larger graphic must not consume another record's
allocation. Existing donor-label ranges remain unchanged and separately guarded.
