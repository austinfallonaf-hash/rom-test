# Bot Book interface alpha

The Bot Book console, introduction, title and data labels now have English drafts.
This adds **34 Shift-JIS UI strings**, reaching **866 UI strings** alongside the
unchanged **4,049 native records, 299 choice blocks and three bitmap captions**.
The heading visible on the gold plate is drawn from text; no new bitmap or tail
allocation is needed. The eight class and twelve type labels follow the existing
bot-status terminology. `Logged` labels the native registered-species count.

## Text and layout

The console and page heading read `Bot Book`. The three-line introduction says:

```
View all data on
bots you've met
or raised here.
```

The two number formatters retain the exact `%03d` argument and reserve three
cells. Their `64 No./` and `GB No./` prefixes give ten cells including the number.
Unknown (`???`) and unavailable (`---`) states retain their source distinction.
The existing list indexes, counts, numeric height/weight values and cm/kg units
are untouched. The Japanese debug/fallback name at 0x10DA0C and full-width
question-mark placeholder at 0x10DB1C remain unchanged; this batch does not count
those placeholders as translation progress.

Height and Weight need six English cells where the native labels have five.
Six guarded horizontal-scale words change from `3C013F80` (1.0) to `3C013F40`
(0.75): **0x1085DC, 0x1086D0, 0x108C78, 0x108D54, 0x109058, 0x109134**.
These are the two label draw calls in each of three native data states. The
label begins at panel x+8; the numeric field begins at x+68, leaving 60 pixels.
Six nine-pixel cells occupy 54 pixels, with a six-pixel gap. Vertical scale,
positions, numeric formatters, units and the original text call remain exact.
There are now **107 guarded layout words**; all previous 88 stay unchanged.

Only the 34 guarded source-string allocations, six scale words, 13 centering
words and repaired CRC1/CRC2 differ from late-dialogue-alpha. All preceding 832 UI entries and the
complete native table/pool stay exact, including all 256 donor labels, 184 book
placements, original source slots, fifteen fixed grids, 38 grid-reader guards,
RAW2 graphic and 66 native exclusions. The book tail still ends at 0x1FFFFC0,
leaving **64 bytes** free. No code relocation, extra ROM storage, decoder change,
mechanic change or saved-name replacement is introduced.

The console and title originally use byte-based Japanese centering, which puts
ASCII `Bot Book` at x=136 instead of x=112. Thirteen additional guarded words
fix the existing readers without extra ROM/code space. The console’s ten-word
block at **0xE081C–0xE0844** uses the first byte’s high bit: Japanese retains
`floor(bytes/2)*6`, ASCII uses `bytes*6`. The local heading reader at
**0x10CE3C–0x10CE68** doubles ASCII length before its original `bytes*3`
calculation. The existing strlen’s delay slot reads the first byte into t0;
the unchanged strlen uses only a0/v0/v1, so t0 survives until the comparison.
The heading’s original signed narrowing, y position, animation and native draw
call stay intact. Other Japanese captions retain their exact original positions.
Both new ASCII captions occupy 96 pixels centered at x=160. Empty strings retain
x=160. These verified readers accept the source Japanese captions and the new
ASCII text; they are not a general mixed-script shaping engine.

The builder now requires these exact centering words when the corresponding
new console/title UI entry is included, and requires each set of measurement
scales when Height or Weight is included. Older catalogs need none of the new
words. This prevents rebuilding the new text with the old Japanese layout.

The console caption at 0xFB84E is inside CIC-6102 checksum coverage. The explicit
checksum option repairs the header while preserving bootcode and all other header
bytes. The 32 MiB ROM has CRC1/CRC2 **FF5EDDAC 400FB7B6**.
MD5: `D85FAF7BD652AFF386B293D6D2633BBF`.
SHA-256: `a603c5572cc2cb59671c1f01fe3833fdc30c4fa42a85e0ee718041a76fbff408`.

## Runtime evidence and limits

The exact final ROM cold-boots into native file A, retaining day 2, 500G,
the entered player name and Merlin’s original stats, Charm and Fire v1. The Book
console caption and gold page heading display Bot Book, correctly centered inside
their plates. The three-line introduction fits. The initial undiscovered entry
displays the translated dash number/type states, Height, Weight and Logged count.
Entry 38 displays Merlin with 64 No./038, GB No./161, Caster, T:Water,
Height 120cm, Weight 130kg and the unchanged four-line biography.
The isolated runtime, default working and immutable reference EEPROMs retain the
same hash. No in-game save or savestate load/create is used.

The run cold-boots with an isolated native EEPROM copy; no savestate is loaded
or created.
The immutable reference and working EEPROMs remain unchanged. This is a partial
game translation: other UI/graphics and earlier native event/branch checks remain
unfinished. The new GB number labels do not establish Transfer Pak functionality.
Class/type and number branches not observed during this run are build-validated.

## Build and recovery

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/book-interface-menu.json --story translation/late-dialogue-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/book-interface-alpha.z64 --patch local/book-interface-alpha.bps
```

Apply the cumulative BPS directly to the exact Japanese original. All **149 tests**
pass in source and clean restoration. Six new tests execute the actual integer
centering instructions for ASCII and Japanese text, check unchanged stack/frame/return registers, preserve all eight
original facility captions, and enforce the exact required layout, including
missing/wrong words and iterator inputs. No text encoding logic changed.
Actual-ROM proof checks all 34 guarded strings, format reservations, unchanged prior bytes, exact
six label readers, both centering routines, unchanged strlen and the final 64-byte padding. Floating IPS independently
reproduces the ROM and read-only chksum64 agrees with its header.

The AES-256 snapshot has **964 payload files**, verified through encrypted
part hashes, byte-identical join/decrypt round trip and clean restoration. Recovery
also checks source revision, ROM/save/evidence hashes, modes, library symlink and
all six regenerated exact-ROM EEPROM profile files. The existing passphrase stays
outside Git. Current/preceding encrypted snapshots and verified restores are kept;
older encrypted working copies remain recoverable from Git/GitHub. See RESTORE.md
and backups/README.md.

Next: the seven remaining facility captions near **0xFB78E–0xFB8DE**: Stars,
Storage, GB Link, Battle Sim, Helm, Pots and Bed. The new console centering already
supports ASCII captions; validate each source allocation and display width.
Bot-status hunger/stress/trait plates need graphical investigation. Preserve all
current text/guards, 66 native exclusions and book allocations; only 64 tail bytes
remain. Keep current/preceding encrypted working copies and verified restores;
update sparse patterns for the next slug and preserve unique files before cleanup.

## New source and English strings

| ROM offset | Source | English | Cell limit |
| --- | --- | --- | --- |
| 0xfb84e | ロボポンずかん | Bot Book | 8 |
| 0x104108 | いままでに　そだてたり　であった\Nロボポンたちのデータが　すべて\Nみられるコンピュータだよ | View all data on\Nbots you've met\Nor raised here. | 16 |
| 0x10d9f8 | ロボポンファイル | Bot Book | 8 |
| 0x10da2c | とうろくすう | Logged | 6 |
| 0x10da40 | ６４ナンバー/%03d | 64 No./%03d | 10 |
| 0x10da54 | ＧＢナンバー/%03d | GB No./%03d | 10 |
| 0x10da68 | ＧＢナンバー/??? | GB No./??? | 10 |
| 0x10dc2c | ６４ナンバー/--- | 64 No./--- | 10 |
| 0x10dc40 | ＧＢナンバー/--- | GB No./--- | 10 |
| 0x10da7c | しんちょう | Height | 6 |
| 0x10da8c | たいじゅう | Weight | 6 |
| 0x10da98 | アームパンチ | Punch | 7 |
| 0x10daa8 | アームナイト | Knight | 7 |
| 0x10dab8 | アームヒーラー | Healer | 7 |
| 0x10dac8 | アームガンマン | Gunner | 7 |
| 0x10dad8 | アームシーフ | Thief | 7 |
| 0x10dae8 | アームファイター | Fighter | 7 |
| 0x10dafc | アームデビル | Devil | 7 |
| 0x10db0c | アームソーサー | Caster | 7 |
| 0x10db30 | タイプ：ノーマル | T:Normal | 8 |
| 0x10db44 | タイプ：ひ | T:Fire | 8 |
| 0x10db50 | タイプ：みず | T:Water | 8 |
| 0x10db60 | タイプ：かぜ | T:Wind | 8 |
| 0x10db70 | タイプ：つち | T:Earth | 8 |
| 0x10db80 | タイプ：かみなり | T:Elec | 8 |
| 0x10db94 | タイプ：こおり | T:Ice | 8 |
| 0x10dba4 | タイプ：せい | T:Holy | 8 |
| 0x10dbb4 | タイプ：じゃ | T:Dark | 8 |
| 0x10dbc4 | タイプ：りく | T:Land | 8 |
| 0x10dbd4 | タイプ：うみ | T:Sea | 8 |
| 0x10dbe4 | タイプ：そら | T:Sky | 8 |
| 0x10dbf4 | タイプ：？？？？ | T:???? | 8 |
| 0x10dc1c | タイプ：???? | T:???? | 8 |
| 0x10dc70 | タイプ：---- | T:---- | 8 |
