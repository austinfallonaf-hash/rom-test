# Ship actions alpha

This batch adds **31 ship activity labels, assignment/training setup messages and
facility prompts**. Cumulative coverage is 4,049 native records, 922 UI strings,
299 native choice blocks and twelve bitmap captions in four resources. The game
remains a partial English draft. Training/chore result messages are next.

## Translation and layout

The activity labels match the existing pause-menu terms: Clean, Fish, Massage,
Repair, Fuel, Feed, Wash, Stretch, Jump, Aim, Catch and Cross. Pearlton remains
ship fuel. Chores and Training identify the activity categories. Setup messages
cover showering, task assignment, the one-Medal training cost, earning Medals
through chores, selection confirmation, Special/Menu and sold-out labels.
Facility text covers unfinished chores blocking departure, bringing a bot,
Game Boy linking, the ghost challenge, bot storage and Star Collection.

All edits stay within their original NUL-terminated Shift-JIS allocations;
no pointer, code or layout change is needed. Colors, page boundaries and printf
specifier order remain exact. Lines are bounded to sixteen cells, with narrower
label bounds. Assignment reserves eleven cells each for the saved bot name and
activity (all translated activity labels fit). Generic selection reserves a full
sixteen-cell name on its own line above Use this?. Dialogue uses at most three
lines per page. The no-Medal explanation uses three lines; the ghost prompt keeps
the original page break. Names held in the save remain existing data.

| Offset | Original | English (`/` line break, `//` page break) |
| --- | --- | --- |
| 0x103960 | そうじ | Clean |
| 0x103968 | さかなつり | Fish |
| 0x103974 | マッサージ | Massage |
| 0x103980 | メンテナンス | Repair |
| 0x103990 | パールトンくべ | Fuel |
| 0x1039a0 | おしょくじ | Feed |
| 0x1039ac | シャワー | Wash |
| 0x1039b8 | のばしてポン | Stretch |
| 0x1039c8 | ジャンプでポン | Jump |
| 0x1039d8 | ねらってポン | Aim |
| 0x1039e8 | キャッチでポン | Catch |
| 0x1039f8 | わたってポン | Cross |
| 0x103a08 | おてつだい | Chores |
| 0x103a14 | トレーニング | Training |
| 0x103a24 | シャワーあび | Wash |
| 0x103a44 | ロボポンに　シャワーを / あびさせますか？ | Give your bot a / shower? |
| 0x103a70 | へやそうじ | Clean room |
| 0x103a90 | %sを%sに / させますか？ | %s: / Do %s? |
| 0x103abc | メダルを１まい　しようします / トレーニングを　はじめますか？ | Medal x1 needed. / Start training? |
| 0x103b04 | メダルをもってないですよ / おてつだいをして　もらってね | No Medals. / Earn some doing / chores. |
| 0x103b4c | %sで　いいですか？ | %s / Use this? |
| 0x103b6c | とくべつ | Special |
| 0x103b78 | メニュー | Menu |
| 0x103b84 | きらしてます | Sold out |
| 0x103f70 | まだ　ロボポンが　おてつだいを / おわらせていないので / しゅっぱつ　できません | Your bot is busy / doing chores. / We can't sail. |
| 0x103fdc | ＧＯ！ | GO! |
| 0x103fec | ロボポンと　いっしょに / きてね！！ | Bring your bot / with you! |
| 0x104010 | ＧＢと　れんらくを / とりますか？ | Link with a GB? |
| 0x10405c | おまえか〜 / ロボポンを　そまつに / あつかっているのは〜…… // おばけロボポンを / たいじ　しますか？？ | So it's you... / who mistreats / your bots... // Face the ghost / Robopon? |
| 0x1040c0 | ロボポンの　だしいれを / しますか？ | Deposit or / withdraw bots? |
| 0x1040e4 | スターコレクションを / みますか？ | View your Star / Collection? |

## Native validation and limits

The exact release ROM cold-boots from an isolated reference EEPROM copy.
File A retains day 2, 500G, player name グリアああ and Merlin's original stats,
Charm and Fire v1. Game Boy Link displays Link with a GB? on one line. Star
Collection displays View your Star / Collection? on two lines. Bot storage
shows Deposit or / withdraw bots? on two lines. All three prompts fit the
original windows and keep existing Yes/No choices. Selecting No returns to
the corresponding ship facility each time. The pause Bots check returns to
the bot profile; assignment/training setup and the other 28 new slots remain
build-only. No task is assigned, training started, transfer performed or bot
stored. Normal exit leaves reference/default/runtime EEPROM hashes unchanged;
no in-game save or savestate is used.

The private evidence records exact observed offsets separately from build-only
entries. Prompt/cancellation checks do not establish successful training, chores,
sailing, Game Boy transfer, a ghost battle or storage transactions. No original
ROM, reference/default EEPROM or saved name is changed. No earlier-ROM savestate
is loaded; no savestate or in-game save is created. Other doctor/Collector,
committed rename, successful evolution and hardware remain unplayed.

## Build and preservation

Only the 31 guarded original text allocations differ from recall-rename-alpha.
All earlier 891 UI entries, 4,049 native records, 299 choices, four graphics
programs/owners, 107 layout guards, all 184 Book allocations and the final 64 FF
bytes remain byte-for-byte intact. The prior ROM/BPS reproduce with current tools
and the prior catalog. No new ROM storage is consumed. All 164 tests pass, in
source and a clean restore. Floating IPS independently reproduces the ROM, and
read-only chksum64 agrees with CIC-6102 CRC1/CRC2 603D64ED 4BB35E71.

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/ship-actions-menu.json --story translation/late-dialogue-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/parts-graphics.json --update-checksum --validate-moves \
  --output local/ship-actions-alpha.z64 --patch local/ship-actions-alpha.bps
```

Apply releases/ship-actions-alpha.bps directly to the exact original Japanese ROM.
Do not stack earlier patches. ROM size remains 32 MiB.
MD5: `A7CF0A90FB05F39DEA4208A021852D95`.
SHA-256: `df9965308c48025aca00d76910762c27a1a1213c4dc330c2d6555942c7e99f05`.

## Recovery and next work

The encrypted AES-256 snapshot verifies 1,254 payload files through a
fresh restore: manifest/source hashes, executable modes, emulator library
symlink, native saves/evidence, all six regenerated exact-ROM profile files and
encrypted part/index/checksum identities. Existing recovery passphrase stays
outside Git. Both ordered parts and the index/three checksum files are required.

Current/preceding Recall snapshots and verified restores are kept. The older
1,156-file evolution restore and cipher are reverified against their manifest,
source commit and canonical private assets; 38 generated extras are preserved
before removing its test tree after this clean restore passes. Sparse omission
of its committed cipher working copies frees 144,298,840 bytes; Git/GitHub retain
all history. Thirty-nine older generated ROMs were already removed only after
independent manifest/BPS reproduction. See RESUME.md and backups/README.md.

Next: training/chore results at 0x103C18-0x103F58 and remaining name-entry/other
interaction UI. The overall-power result at 0x103EF8 contains unsupported control
\O333; reverse-engineer it before changing that string. Keep item/name/number
reservations conservative and preserve all controls. This batch leaves those
result messages and the previously translated departure/practice prompts intact.
