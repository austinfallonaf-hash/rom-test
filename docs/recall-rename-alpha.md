# Recall and Rename alpha

Six Dr. Dandy prompts now have English drafts: both doctors' questions about
calling Collector, both Rename bot-selection prompts, and both name-confirmation
prompts. Cumulative coverage is **4,049 native records, 891 UI strings, 299 choice
blocks and twelve bitmap captions in four resources**. Other UI/gameplay branches
remain incomplete. Saved player/bot names stay unchanged.

## Wording and guards

Collector matches the already translated native NPC name (record 2867). Recall
therefore asks **Call Collector?**, keeping Collector green. Rename asks **Which
bot should / be renamed?** with bot highlighted, then displays the current bot's
name above **Rename this bot?**. The existing Yes/No labels remain unchanged.

`translation/recall-rename-menu.json` retains all 885 earlier entries exactly and
adds six original NUL-terminated allocations. Each source and byte budget stays
guarded. Both Recall questions remain one line; Rename selection/confirmation
remain two lines. Every line is bounded to sixteen cells, with eleven cells
reserved for the formatted bot name. Original color arguments/order, printf
specifiers and newline counts remain exact. No event, branch or name-input code
is modified. The harvest naming question at 0x1041B0 was already translated;
its wording and allocation remain unchanged.

| Offset | Original | English (`/` is a line break) |
| --- | --- | --- |
| 0x1033d8 | かいしゅうやを　よびますよ？ | Call Collector? |
| 0x103400 | かいしゅうやを　よぶんじゃな？ | Call Collector? |
| 0x10380c | どのロボポンの / なまえを　かえたいのですか？ | Which bot should / be renamed? |
| 0x103844 | どのロボポンの / なまえを　かえたいんじゃ？ | Which bot should / be renamed? |
| 0x10387c | %sの / なまえをかえるんですね？ | %s / Rename this bot? |
| 0x1038a8 | %sの / なまえをかえるんじゃな？ | %s / Rename this bot? |

## Native checks and limits

The exact release ROM cold-boots from an isolated reference EEPROM copy.
File A retains day 2, 500G, player name グリアああ and Merlin's original stats,
Charm and Fire v1. Doctor navigation opens the polite doctor's menu. Recall
shows Call Collector? with Collector green; No returns to the doctor menu.
Rename shows Which bot should / be renamed? with bot yellow. Selecting Merlin
shows the saved Japanese nickname above Rename this bot?, with the name yellow.
Both prompts fit their original two-line windows. No returns to bot selection;
B then cancels back to the doctor menu. The name editor is not opened and Collector
is not summoned. Normal exit leaves reference, default and isolated runtime
EEPROM hashes unchanged. No in-game save or savestate is used.

This run checks the polite doctor's three strings and cancellation routes. The
other doctor's three variants are build-validated, not separately played. Calling
Collector, using the Collector service, entering/committing a new name, harvesting
and long-name cases remain unplayed. No completed rename or actual Recall service
is claimed. Earlier evolution, equipment, gameplay and hardware limits remain.

The exact-ROM run cold-boots with a separate reference EEPROM copy and creates or
loads no savestate. Baseline Japanese and final English screenshots/logs, source/
target text records, exact save identity and a portable actual-ROM proof are
retained in private evidence. The saved player name グリアああ remains ten
Shift-JIS bytes at EEPROM 0x3F; it is save data, not an interface label.

## Preservation and build

Only six original text allocations differ from evolution-interface-alpha. Every
other byte remains identical: all 885 earlier UI entries (including harvest naming),
4,049 native records, 299 choices, source slots/donors/grids/exclusions, all 107
guarded layout words, code/checksums, four resource programs, all 184 Book
allocations and final 64 FF bytes. The previous ROM/BPS rebuild byte-for-byte
with current tools and the old menu catalog. No new ROM storage is consumed.

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/recall-rename-menu.json --story translation/late-dialogue-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/parts-graphics.json --update-checksum --validate-moves \
  --output local/recall-rename-alpha.z64 --patch local/recall-rename-alpha.bps
```

Apply the cumulative BPS directly to the exact Japanese original. All **164 tests**
pass in source and clean restoration. Existing source/terminator/byte/color/printf/
line guards pass for all six entries. Floating IPS independently reproduces the
ROM; read-only chksum64 agrees with CIC-6102 CRC1/CRC2 **603D64ED 4BB35E71**.
These values stay unchanged because all edits are beyond its covered region.
ROM size remains 32 MiB.
MD5: `220E75A334B0A9125A68B3BB039A62EC`.
SHA-256: `3deb184dd20233b6a2a4ae7889600307a71fe88ca6d742ba95df09a2ec7b0c0a`.

## Workspace and recovery

Thirty-nine older generated ROM working copies were removed only after each
matched its shipped manifest, patch hash and committed BPS, and Floating IPS
independently reproduced every byte from the immutable original. This freed
**1,308,622,848 bytes**. Original/current/preceding playable ROMs and unmatched
prototype builds remain. Patches and encrypted history stay in Git/GitHub. The
private generated-rom-retention.json ledger records every path, size, SHA-256,
patch/manifest and verified canonical commit. RESUME.md gives the reconstruction
command; do not assume an older working ROM filename remains present.

The archive intentionally includes original/current ROMs plus all historical
patches, instead of duplicate historical ROM builds. It verifies **1,200
payload files**, source revision, hashes, executable modes, emulator library
symlink, native saves/evidence and all six regenerated exact-ROM profile files
through a clean restore. AES-256 parts and plaintext/ciphertext checksum files
are checked; the existing passphrase stays outside Git.

Current/preceding encrypted snapshots and verified restores are retained. The
older 1,120-file Parts restore was manifest/source/canonical/cipher verified,
with 38 generated extras preserved before its test tree is removed only after
the new restoration passes. Historical ciphertext stays in Git/GitHub. See
RESTORE.md and backups/README.md.

Next: remaining name-entry, ship-facility and training interaction UI; unplayed
positive Recall/Rename branches retain their documented limits.
