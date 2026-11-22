# Evolution interface alpha

Twelve Dr. Dandy evolution strings now have English drafts: bot selection,
two-name confirmation, target-form name, readiness/refusal, missing Orbs,
remaining-Orb counter and chores status. This covers both doctor text variants
in the build. Cumulative coverage is **4,049 native records, 885 UI strings,
299 choices and twelve bitmap captions in four resources**.

The file-screen text previously called a progress label is actually the saved
player name **グリアああ**. The immutable EEPROM stores its ten Shift-JIS bytes
`834f838a834182a082a0` at **0x3F**. It appears in the file and pause player panels.
The handoff now records this correction. That name and all save data stay intact.

## Text and layout

`translation/evolution-menu.json` preserves the preceding 873 UI entries and
adds twelve original NUL-terminated allocations at 0x10342C–0x1035C4. Each slot
retains its exact source guard, terminator and capacity. The existing `-----`
placeholder at 0x103510 stays untouched. No reader coordinates or code change.

The two selection prompts and two confirmation variants retain their original
two-line layout. Both formatted confirmation names reserve **eleven cells**;
compact `name / to name?` keeps each name on its own line. The target-form field
shows the name alone, omitting Japanese へ to fit the original fixed slot.
The narrower status pane uses at most **ten cells** per single-line label:
Evolve: No / Evolve: OK, Need Orbs, Evolve, the Orb counter and On chores!.
All original color arguments/order and printf specifiers remain exact; the
`%3d` counter reserves three display cells. Original newline counts are unchanged.

| Offset | Original text | English draft (`/` is a line break) |
| --- | --- | --- |
| 0x10342c | どのロボポンを / しんか　させますか？ | Which bot should / evolve? |
| 0x10345c | どのロボポンを / しんか　させたいのじゃ？ | Which bot should / evolve? |
| 0x10349c | %sを　%sに / しんか　させますか？ | %s / to %s? |
| 0x1034d4 | %sを　%sに / しんか　させるのじゃな？ | %s / to %s? |
| 0x103518 | しんかできません | Evolve: No |
| 0x103534 | %sへ | %s |
| 0x103544 | しんか　かのう！ | Evolve: OK |
| 0x103560 | エネだまぶそくで | Need Orbs |
| 0x10357c | 　しんかできません | Evolve: No |
| 0x10359c | つぎのしんかまで | Evolve |
| 0x1035b0 | エネだまあと：%3d | Orbs: %3d |
| 0x1035c4 | おてつだいちゅう！ | On chores! |

## Native checks and limits

The exact release ROM cold-boots from a reference EEPROM copy. File A retains
day 2, 500G, the saved player name グリアああ and Merlin's original stats, Charm
and Fire v1. Native 2F Doctor navigation opens Dr. Dandy's menu and its Evolve
selection. The polite prompt reads Which bot should / evolve? with the bot color
retained. Merlin's insufficient-Orb pane reads Need Orbs, Evolve: No, Evolve and
Orbs: 200; color focus stays on Orbs/evolve. Both lines of the prompt and all
status labels fit their original windows. Attempting this ineligible selection
leaves the refusal pane intact; B cancels back to the doctor menu. No evolution
confirmation is reached. The emulator closes normally. Reference, default working
and isolated runtime EEPROM hashes stay unchanged; no save or savestate is used.

The exact-ROM cold boot uses an isolated copy of the reference EEPROM. No older
ROM state or descriptor preview is used. Screenshots, completed emulator logs,
source/target text records, save identity and a portable actual-ROM proof are
retained in private evidence.

Only the polite doctor's selection and insufficient-Orb path are exercised here.
The other doctor variant, eligible/ready target, two-name confirmation, chores
restriction and successful evolution remain build-validated and unplayed. This
does not claim that a bot evolved, equipment changed, any save operation ran,
or those unvisited branches/hardware were validated. Earlier gameplay limits remain.

## Preservation and build

Actual-ROM proof permits changes only in the twelve original text allocations.
Every other byte remains identical to parts-graphics-alpha: all 873 earlier UI
entries, 4,049 native records, 299 choices, source slots/donors/grids/exclusions,
107 guarded layout words, code, checksums, four resource programs, all 184 Book
allocations and final 64 FF bytes. The prior ROM and BPS rebuild byte-for-byte
with current tools and their original catalogs. No new ROM storage is consumed.

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/evolution-menu.json --story translation/late-dialogue-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/parts-graphics.json --update-checksum --validate-moves \
  --output local/evolution-interface-alpha.z64 --patch local/evolution-interface-alpha.bps
```

Apply the cumulative BPS directly to the exact Japanese original. All **164 tests**
pass in source and clean restoration. Existing guards check byte/line/printf/color
budgets, with explicit single-line ten-cell status limits and two-line sixteen-cell
prompt limits. Floating IPS independently reproduces the ROM. Read-only chksum64
agrees with CIC-6102 CRC1/CRC2 **603D64ED 4BB35E71**. These values are unchanged
because the edits lie beyond its covered range. ROM size remains 32 MiB.
MD5: `267BE64B5F4A94836339693CA8C6E5B1`.
SHA-256: `9f7e2530035ab14feee0ca76ee514335a88ca839194c23e5b848bce307bf5732`.

The encrypted AES-256 archive verifies **1,156 payload files**, source
revision, hashes, modes, emulator library symlink, native saves/evidence and six
regenerated exact-ROM profile files through a clean restore. The existing
passphrase stays outside Git. Current/preceding encrypted copies and verified
restores are retained. The older 1,077-file save-file restore was manifest/source/
canonical/cipher verified, with 38 extra files preserved before its generated
tree is removed after the new restore passes. Historical ciphertext remains
in Git/GitHub. See RESTORE.md and backups/README.md.

Next: remaining untranslated UI, including Recall/Rename and unplayed evolution
branches. The saved player name is not pending translation work.
