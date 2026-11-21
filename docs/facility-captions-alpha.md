# Ship facility captions alpha

All eight floating ship facility captions now have English drafts. This batch
adds **seven UI strings**, alongside the previous Bot Book caption, reaching
**873 UI strings, 4,049 native records, 299 choices and three bitmap captions**.
These are the labels shown over facilities on the ship, separate from the already
translated R-navigation and doctor-help menus.

The names follow the existing navigation labels: **Stars, Store, GB Link,
Btl Sim, Helm, Pots and Bed**. Store means the bot storage facility; it is not a
shop. The source’s three-character そうこ allocation has six Shift-JIS bytes,
so the existing compact Store label fits while the full Storage would exceed it.
Btl Sim follows the navigation abbreviation and fits its eight-byte source slot.
No donor storage, new tail allocation, font change or interpreter change is used.

## Source and display guards

The seven source strings sit inside 48-byte facility records at 0xFB780–0xFB900.
Only each original NUL-terminated name allocation is overwritten, with zero fill.
The preceding fields (world position/floor/interaction metadata), trailing reach
value, empty padding outside the original name and record boundaries stay exact.
All labels have three to seven ASCII cells and fit inside the native caption
plate. At twelve pixels per cell, the longest occupies 84 pixels. The existing
English caption reader centers them at x=160 using the previous milestone’s
ASCII-aware logic at 0xE081C. All **107 layout words** remain byte-identical.

The builder now requires that exact caption reader for **any** of the eight
facility caption offsets, even when a menu subset omits Bot Book. A new test
checks every caption independently and rejects each missing reader word. Older
unrelated UI catalogs still need no new caption layout. This changes build guards,
not the game executable: only seven string slots and CRC1/CRC2 differ from
book-interface-alpha.

All preceding 866 UI strings, the complete native table/pool, 256 donor labels,
184 book allocations, original source slots, fifteen fixed grids, 66 native
exclusions, graphics, measurement readers and caption code stay exact. The book
tail still ends at 0x1FFFFC0, leaving **64 bytes** of FF padding.

## Runtime evidence and limits

The exact release ROM cold-boots into native file A with day 2, 500G,
the entered player name and Merlin’s original stats, Charm and Fire v1 intact.
R navigation visits all seven newly translated facilities: Bed, Pots, Helm,
GB Link, Btl Sim, Store and Stars. Each floating caption appears centered inside
its original plate. The unchanged Bot Book caption is also observed on this build.
No facility is activated for testing these captions. The immutable reference,
default working and isolated runtime EEPROMs retain their original hash. No
in-game save or savestate load/create is used.

This is a partial English draft. Facility captions do not establish GB transfers,
storage operations, battles, achievement rewards, planting, saving or ship travel
mechanics. Earlier UI/native branch checks retain their documented limits.
Native saved Japanese names remain save data. Other UI and bitmap labels remain
Japanese, including the bot-status hunger/stress/trait plates.

## Build and recovery

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/facility-captions-menu.json --story translation/late-dialogue-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/facility-captions-alpha.z64 --patch local/facility-captions-alpha.bps
```

Apply the cumulative BPS directly to the exact Japanese original. Source caption
bytes lie inside CIC-6102 checksum coverage; CRC1/CRC2 are repaired explicitly.
Bootcode and other header bytes remain unchanged. All **150 tests** pass in source
and clean restoration. Independent Floating IPS application reproduces the ROM;
read-only chksum64 agrees with the repaired header. Actual-ROM proof permits only
seven original string slots and the eight checksum bytes to differ from the prior
release, and checks every new caption’s mandatory layout independently.

ROM MD5: `AD3B84849EACFE1636BC53902D1A768F`.
SHA-256: `3cbacbba12952502e6e03bd582b687858bd7931dc14c7a41923a76a24f09d8da`.
CIC-6102 CRC1/CRC2: **79430F32 1567A7B8**. ROM size remains 32 MiB.

The two-part AES-256 recovery snapshot verifies **996 payload files**
through part hashes, exact joining/decryption and a clean restore. It checks
source revision, ROM/BPS/save/evidence hashes, modes, library symlink and six
regenerated exact-ROM EEPROM profile files. The existing passphrase stays outside
Git. Current/preceding encrypted working copies and verified restores are kept.
The older 933-file restore was checked against its manifest, historical Git source,
canonical private assets and encrypted parts; its 34 extra files were preserved
before removing that generated copy. Older encrypted snapshots remain in local Git
and on GitHub, retrievable with the documented sparse-checkout commands.

Next: investigate the bot-status hunger/stress/trait graphics and a compact
replacement or overlay that preserves book allocations and the final 64 bytes.
Keep all current text, source controls, donors, grids and layout guards. Other
facility operations and native branches still need gameplay coverage.

## Added source and English strings

| ROM offset | Source | English | Encoded ASCII bytes | Caption x |
| --- | --- | --- | --- | --- |
| 0xfb78e | スターコレクション | Stars | 6 | 130 |
| 0xfb7be | そうこ | Store | 6 | 130 |
| 0xfb7ee | ＧＢコンバート | GB Link | 8 | 118 |
| 0xfb81e | バトシム | Btl Sim | 8 | 118 |
| 0xfb87e | そうじゅうせき | Helm | 5 | 136 |
| 0xfb8ae | うえきばち | Pots | 5 | 136 |
| 0xfb8de | ベッド | Bed | 4 | 142 |
