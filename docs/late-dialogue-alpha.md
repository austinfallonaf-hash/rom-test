# Late dialogue and native-table coverage alpha

This cumulative partial English draft adds **84 native records**: 52 companion
travel/fuel conversations, 15 evolution reactions, ten achievement messages and
seven full region labels. Coverage reaches **4,049 native records, 832 UI strings,
299 choices and three bitmap captions**. All 3,965 preceding catalog entries,
active bytes and descriptors remain identical.

## Wording and controls

The companion tracks cover the seven seas, Caramela hunting, fuel, Gariman,
Roulette, Kujiran, Despera Mountain, the Musketeers and the journey home. The
mock-funeral joke retains “Namu, namu” and a compact bell/tapping response.
Evolution reactions preserve five voices; the Captain lines ask for continued
guidance. Achievement wording distinguishes 100 battles from wins and 500
minigame clears from plays. GB Link success is translated text, without claiming
a transfer was tested. The seven labels are Moon Blue, Fire Blue, Water Blue,
Tree Blue, Gold Blue, Land Blue and Sunny Blue.

All 77 dialogue records preserve their exact source control stream and arguments,
including ten player-name insertions and one bot-name insertion (3976). Layout
reserves five and eleven cells respectively. No new newline exceptions, page
anchors, interpreter changes or mechanics are introduced. English is condensed
to the original source allocations and the existing 16-cell/three-line limits.

## Label storage and file captions

The seven region labels use **130 encoded bytes** in seven additional translated
donors. The complete catalog has **256 disjoint donor labels in 162 donors**.
The builder subtracts each donor’s active text and every occupied interval;
original Japanese label slots remain unchanged. The allocation ledger is below.

| Label ID | Donor | Relative byte offset |
| --- | --- | --- |
| 4108 | 1656 | 78 |
| 4109 | 1666 | 26 |
| 4110 | 2289 | 80 |
| 4111 | 1824 | 78 |
| 4112 | 1829 | 78 |
| 4113 | 1864 | 320 |
| 4114 | 2293 | 80 |

Native file A/B region fields have 112 pixels available. At the original 1.0
horizontal scale the longest ten-cell labels would occupy 120 pixels. Two
source-guarded words at **0x220580** and **0x220900** change `3C013F80` to
`3C013F40` (0.75), making ten cells 90 pixels. Vertical scale, x/y coordinates,
region-ID lookup and draw calls remain exact. The pause reader at 0x20D8D4 stays
at 1.0. There are now **88 guarded layout words**; all preceding 86 are unchanged.

All 184 bot-book placements, original book slots, RAW2 bitmap, fifteen fixed-grid
records and 38 grid-reader instructions remain exact. Book allocations still end
at **0x1FFFFC0**, leaving only **64 bytes** of original FF tail padding.

## Native coverage audit

`translation/native-coverage.json` accounts for all **4,115** records in the
verified native table: **4,049 English drafts, 48 cut placeholders and 18
portrait-only entries**. The exclusions remain byte-for-byte original, including
descriptors. Cut placeholders contain the source cut marker, and portrait-only
entries contain a single portrait control plus argument. There are no other
untranslated records in this table. This does **not** establish a complete game
translation: separate Shift-JIS UI, bitmap text and gameplay coverage remain.

## Runtime evidence and limits

The final ROM cold-boots into native file A: Moon Blue appears in file selection
and the pause menu; day 2, 500G, saved names, Merlin’s stats, Charm and Fire v1
are intact. A separate cold-boot descriptor-only preview displays the actual
ten-cell Water Blue label in file A, fitting the field, and all four pages of
new record 4096 through the doctor’s Pearlton help slot, including the existing
five-cell saved player name. Only three descriptors differ in that preview;
actual payloads, code, event flags and save data remain unchanged. This checks
display, not the achievement’s native trigger. File B is empty, so its mirrored
caption reader is source/ROM-guarded rather than gameplay-tested. Both isolated
EEPROMs match the immutable reference; no in-game save or savestate is used.

The final ROM cold-boots and loads native file A with day 2, 500G, the saved player
name and Merlin. The pause menu displays Moon Blue. Merlin retains Caster,
T:Water, HP/EP 22, Attack 29, Defense 30, Speed 20, CPU 1, Charm, Fire v1 and
200 Orbs. Saved Japanese nicknames remain save data. The immutable reference,
default working copy and isolated runtime EEPROMs are unchanged. No in-game save
or savestate load/create is used.

New companion/evolution/achievement triggers remain unplayed. Earlier book,
fuel/chore/minigame/pest/reaction/name/newline/donor/regional branches, five
anchored pages, graphical Parts frames and VS/Transfer Pak retain their documented
gameplay limits. Display preview evidence does not establish those mechanics.

Final ROM MD5: `DC99F55BF5F61E3DDA19610B393DC050`.
SHA-256: `d38e683c2e4efea7aec4a78526c90bea79db58a9e8a823562b730f3e30177778`.
The 32 MiB ROM retains CIC-6102 CRC1/CRC2 `FFA89600 C278C65F`.

## Build and recovery

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/late-dialogue-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/late-dialogue-alpha.z64 --patch local/late-dialogue-alpha.bps
```

Apply the cumulative BPS directly to the exact Japanese original. Independent
Floating IPS application reproduces the ROM; read-only chksum64 agrees with its
header. All **143 tests** pass in source and clean restoration. Actual-ROM proof
checks every active record, prior bytes/descriptors, all controls/placements,
66 exclusions, existing layout and the two isolated new caption scale words.

The AES-256 backup uses two verified ciphertext parts and the existing passphrase,
kept outside Git. Clean restoration checks **933 payload files**, source
revision, ROM/BPS/save/evidence hashes, modes, emulator library symlink and the
exact-ROM 16Kbit EEPROM profile. See backups/README.md and RESTORE.md.

To prevent workspace exhaustion, non-cone sparse checkout now keeps only current
and preceding encrypted backup working copies. **96 older committed files,
2,309,087,743 bytes**, were verified against Git blobs and omitted from the working
tree; all remain in local Git and on the canonical GitHub branch. No historical
snapshot was removed from Git. The older equipment restore was manifest-verified,
its extra files retained, then its generated copy removed. The preceding 896-file
bot-book restore remains. See backups/README.md for retrieval and future pattern
updates. The ZIP deliberately excludes Git, ciphertext, secrets and old built ROMs.

Next: separate Shift-JIS UI, starting with the observed Bot Book introduction at
**0x104108**, then its data labels/headings. Preserve the 256 donor labels, 184
book allocations, fifteen grids, 88 layout guards and all 66 source exclusions.

## Added source and English records

The table keeps explicit control tokens for review. `<br>` marks a display line
break in this documentation only; the catalog preserves the original stream.

| ID | Source | English |
| --- | --- | --- |
| 3918 | <200A>！<2003>！カラメル<2003>　みつけて<2000>ハッピーに　なろう！<2000><200A>”ウハウハに　なろう！ | [200A:0001]Find [2003:0001]Caramel[2003:0000][2000]Happy![2000][200A:0002]Live it up |
| 3919 | <200A>！<2003>！カラメル<2003>　みつけて<2000>ハッピーに　なろう！<2000><200A>”ウハウハに　なろう！ | [200A:0001]Find [2003:0001]Caramel[2003:0000][2000]Happy![2000][200A:0002]Live it up |
| 3920 | <200A>！<2003>％ほのおのカラメラ<2003>　を<2000>とりかえして　<2003>！ガーリマン<2003>　さんに<2000>かえして　あげよーぜ！<200A>＄ | [200A:0001][2003:0005]Fire Caramela[2003:0000][2000]to [2003:0001]Gariman[2003:0000][2000]Get it back![200A:0004] |
| 3921 | <200A>！いやー　あんなに<2000>かんしゃしてもらえるなんて……<2000>ひとだすけって　いいもんだね！<200A>” | [200A:0001]So many thanks![2000]Helping feels[2000]so good![200A:0002] |
| 3922 | <200A>＃くらいなあ……イメージわるいよ<2000>なんか　このうみってさ！ | [200A:0003]So dark...[2000]This sea's grim! |
| 3923 | <200A>！あたらしい　フネが<2000>もらえるんでしょ！<2000>どんなのか　たのしみだなあ！<200A>” | [200A:0001]New ship![2000]What kind?[2000]Can't wait![200A:0002] |
| 3924 | <200A>％おお！<2000>イカスよ　しんぴん！<2000><200A>”とくしたって　マジで！ | [200A:0005]Wow![2000]New and cool![2000][200A:0002]A deal! |
| 3925 | <200A>！ルーレッとうって　スゴイよね！<2000>いったい　ダレが　どんな<2000>もくてきで　つくったのかなあ？<200A>　 | [200A:0001]Roulette's wild![2000]Who built it,[2000]and what for?[200A:0000] |
| 3926 | <200A>！<2003>％おうごんのカラメラ<2003>　を<2000>にいちゃんが　てにいれたら<2000>どうなんの？　なあ　どうなん？<200A>　 | [200A:0001][2003:0005]Gold Caramela[2003:0000][2000]If Bro gets it,[2000]then what?[200A:0000] |
| 3927 | <200A>”うみが　もとにもどった！<2000>にいちゃんって　スッゴイねー！<2000>うーん　エライったら　もう！ | [200A:0002]Sea's back![2000]You're amazing![2000]Great, Bro! |
| 3928 | <200A>！しまが　しずんだり　ういたり<2000>なんだか　いそがしいね！<2000>おつかれさんって　かんじだね！<200A>　 | [200A:0001]Islands rise[2000]and sink! Busy![2000]Good work![200A:0000] |
| 3929 | <200A>！クージランごうは　スゴイんだぜ！<2000>ロボポンシップの　なかでも<2000>さいこうきゅうの　フネらしいね！<200A>　 | [200A:0001]Kujiran's great![2000]A top-class ship[2000]so they say![200A:0000] |
| 3930 | <200A>！<2003>”デスペラーマウンテン<2003>　かー……<2000><200A>＄いったいなにが　まっているのか<2000>わからないな……なんか　コワイね | [200A:0001][2003:0002]Despera Mountain[2003:0000][2000][200A:0004]What awaits us?[2000]Scary... |
| 3931 | <200A>！うみのたびは　あきないね！<2000>ぼうけんは　おわらない<2000><200A>”……ってかんじだね　まったく！ | [200A:0001]Sea trips rock![2000]Adventure[2000][200A:0002]never ends, eh? |
| 3932 | <200A>％ふねの　エネルギーが<2000>ゼロになったら…かんがえたでけで<2000>おそろしいっ！！ | [200A:0005]No ship fuel?[2000]The thought[2000]scares me! |
| 3933 | <200A>％ゲ　ゲームオーバー？？？<2000><200A>＃パールトンが　ゼロになったら<2000>ぼうけんが　おわっちゃうよー！ | [200A:0005]G-GAME OVER?![2000][200A:0003]No Pearlton,[2000]no more trip! |
| 3934 | <200A>＃うわぁ　なんで　こんなダメな<2000>アニキをもったんだろう<2000>ふこうなオレ…… | [200A:0003]My lousy Bro...[2000]Why him?[2000]Poor me... |
| 3935 | <200A>！にいちゃん！<2000><2003>！カラメル<2003>　を　ぜったいに<2000>みつけようね！<200A>” | [200A:0001]Bro![2000]Find [2003:0001]Caramel[2003:0000][2000]For sure[200A:0002] |
| 3936 | <200A>！にいちゃん！<2000><2003>！カラメル<2003>　を　ぜったいに<2000>みつけようね！<200A>” | [200A:0001]Bro![2000]Find [2003:0001]Caramel[2003:0000][2000]For sure[200A:0002] |
| 3937 | <200A>！<2003>％ほのおのカラメラ<2003>　を<2000>とりかえして　<2003>！ガーリマン<2003>　さんに<2000>かえして　あげようよ！<200A>＄ | [200A:0001][2003:0005]Fire Caramela[2003:0000][2000]to [2003:0001]Gariman[2003:0000][2000]Get it back![200A:0004] |
| 3938 | <200A>！ゆうきって　ひとを<2000>つよくするんだね！<2000>がんばった　かいがあったネ！<200A>　 | [200A:0001]Courage[2000]makes us strong![2000]Worth it![200A:0000] |
| 3939 | <200A>！よるの　せかいなのかな？<2000><200A>＄なんだか　くらい　うみだね | [200A:0001]Night world?[2000][200A:0004]A dark sea... |
| 3940 | <200A>！あたらしい　フネって<2000>どんなのかなあ？<2000>たのしみだね　にいちゃん！<200A>　 | [200A:0001]New ship?[2000]What kind?[2000]Can't wait![200A:0000] |
| 3941 | <200A>”やったー！　あったらしい<2000>フネ！　かっちょいいー！<2000>イカスぜ　スゴイぜ！ | [200A:0002]Yay! A new ship![2000]So cool![2000]Awesome! |
| 3942 | <200A>！ルーレッとうって　スゴイよね！<2000>いったい　ダレが　どんな<2000>もくてきで　つくったのかなあ？<200A>　 | [200A:0001]Roulette's wild![2000]Who built it,[2000]and what for?[200A:0000] |
| 3943 | <200A>！<2003>％おうごんのカラメラ<2003>　を<2000>にいちゃんが　てにいれたら<2000>どうなんのかなー？<200A>　 | [200A:0001][2003:0005]Gold Caramela[2003:0000][2000]Bro gets it...[2000]Then?[200A:0000] |
| 3944 | <200A>！うみが　もとにもどった！<2000>やっぱり　にいちゃんはスゴイや！<200A>” | [200A:0001]Sea's back![2000]Great work, Bro![200A:0002] |
| 3945 | <200A>！なんか　しまが　ういたり<2000>しずんだり　してるね<2000>かわってるね！<200A>　 | [200A:0001]Islands rise[2000]and sink...[2000]Weird![200A:0000] |
| 3946 | <200A>！クージランごうは　スゴイんだ！<2000>ロボポンシップの　なかでも<2000>さいこうきゅうの　フネなんだよ！<200A>　 | [200A:0001]Kujiran's great![2000]One of the[2000]very best ships![200A:0000] |
| 3947 | <200A>！<2003>”デスペラーマウンテン<2003>　まで<2000>とうとう　きちゃったよ！<2000>ここまできたら　まけらんないよ！<200A>＄ | [200A:0001][2003:0002]Despera Mountain[2003:0000][2000]Made it![2000]Can't lose now![200A:0004] |
| 3948 | <200A>！うみのたびは　たのしいなあ！<2000>やっぱ　ひろいトコはいいね！<2000>ぼうけんは　いいね！<200A>” | [200A:0001]Sea trips rock![2000]Wide spaces![2000]Adventure![200A:0002] |
| 3949 | <200A>＄おにいちゃん　パールトンを<2000>たくさん　あつめないと<2000>ふねが　ばくはつしちゃうよ！ | [200A:0004]Bro, Pearlton[2000]Get more or[2000]we'll blow up! |
| 3950 | <200A>＄おにいちゃん　もうヤバイよ！<2000>もう　じかんギリギリだよ！<2000><200A>＃パールトン　どこ〜！？ | [200A:0004]Bro! No time![2000]It's bad![2000][200A:0003]Pearlton? Where? |
| 3951 | <200A>！ナ〜ム〜　ナ〜ム〜<2000>ポクポクポク　チ〜ンっ！！<2000>おだぶつっ！！<200A>” | [200A:0001]Namu, namu![2000]Tap-tap, ding![2000]RIP![200A:0002] |
| 3952 | <200A>！これから　よろしくね！<2000>いっしょに　がんばろーネ！<200A>” | [200A:0001]Hi there![2000]Let's try hard![200A:0002] |
| 3953 | <200A>！なによ　キンニクキンニクって！<2000>もう　なんか　キンニクだらけで<2000>アタマ　いたくなってきた……！<200A>　 | [200A:0001]Muscles! Ugh![2000]Muscles galore![2000]My head hurts![200A:0000] |
| 3954 | <200A>！ダレかのために　がんばるって<2000>けっこう　きもちいいんだね！<2000>これからも　がんばろーネ！<200A>　 | [200A:0001]Helping folks[2000]feels so good![2000]Let's keep on![200A:0000] |
| 3955 | <200A>％ぶきみな　ところね……<2000>うみも　なんか　ヘンだし？<2000><200A>！いったい　なんなのかしら？<200A>　 | [200A:0005]Eerie place.[2000]Weird sea too![2000][200A:0001]What is it?[200A:0000] |
| 3956 | <200A>！バリヤーとかで<2000>みんなを　かんりしてるなんて<2000>おかしいよ　ぜったい！<200A>　 | [200A:0001]Barriers[2000]to control us?[2000]So wrong![200A:0000] |
| 3957 | <200A>！うみを　じゆうに　いききできる<2000>なんて　あたりまえだけど……<2000>ステキだよネ　ホント！<200A>　 | [200A:0001]Free sea trips[2000]seem normal[2000]but are lovely![200A:0000] |
| 3958 | <200A>！まったく　ゆるせないッ！<2000>かいぞくたちめ！　はやく<2000><2003>！パンチ<2003>　を　たすけださないとネ！<200A>　 | [200A:0001]Those pirates![2000]Hurry! Must[2000]rescue [2003:0001]Punch[2003:0000]![200A:0000] |
| 3959 | <200A>！まったく　ゆるせないッ！<2000>かいぞくたちめ！　はやく<2000><2003>！ラム<2003>　を　たすけださないとネ！<200A>　 | [200A:0001]Those pirates![2000]Hurry! Must[2000]rescue [2003:0001]Ram[2003:0000]![200A:0000] |
| 3960 | <200A>！<2003>”ゴールド＝ブルー<2003>　って<2000>どんなところ　だろう？<200A>　 | [200A:0001][2003:0002]Gold Blue[2003:0000][2000]What place?[200A:0000] |
| 3961 | <200A>！うみが　きんいろなんて　ステキ！<2000>ゆうやけが　こおりに<2000>はんしゃしてるから　なんだって！<200A>　 | [200A:0001]A gold sea![2000]Sunset off ice,[2000]they say! Lovely[200A:0000] |
| 3962 | <200A>！あと２つで　<2003>％カラメラ<2003>　がぜんぶ<2000>そろうのネ！　どんなねがいごと<2000>しようかな？　ドキドキしちゃう！<200A>　 | [200A:0001]Last 2 [2003:0005]Caramela[2003:0000]![2000]What to wish?[2000]So excited![200A:0000] |
| 3963 | <200A>！<2003>！さんじゅうし<2003>　って　キライ！<2000>あのヒトたち　エラそーで<2000>ごういんだし　めいわくしちゃう！<200A>　 | [200A:0001][2003:0001]Musketeers[2003:0000]! Ugh![2000]Bossy, pushy![2000]What a pain![200A:0000] |
| 3964 | <200A>！このフネって　どこがスゴイのよ？<2000>なかみは　いままでとおなじだし<2000>わたしは　わたしのへやがほしい！<200A>　 | [200A:0001]What's so great?[2000]Same inside...[2000]Want my own room[200A:0000] |
| 3965 | <200A>！<2003>！<200B>　<2003>　　がんばって……！<2000>あなたなら　ぜったいできる！<2000>わたし　しんじてるから！<200A>　 | [200A:0001][2003:0001][200B:0000][2003:0000], do it![2000]You can do it![2000]I trust you![200A:0000] |
| 3966 | <200A>！もうこうなったら　トコトンよ！<2000>やれるだけ　やってみましょう！<2000>どこまでも　ついていくわ！<2001><200A>　<200A>！もう　どんなことがあったって<2000>コワクないよ！　だって<2000><2003>！<200B>　<2003>　と　いっしょだからネ！<200A>　 | [200A:0001]Go all out![2000]Do all we can![2000]I'll follow you![2001][200A:0000][200A:0001]Nothing scares[2000]me now, since[2000]I'm with [2003:0001][200B:0000][2003:0000]![200A:0000] |
| 3967 | <200A>＃パールトンが　なくなったら<2000>ぼうけんどころか　あたしたちの<2000>いのちまで　なくなっちゃうのよ！ | [200A:0003]No Pearlton,[2000]no adventure...[2000]And no lives! |
| 3968 | <200A>％はやく　パールトンを　さがして！<2000>あたし　こんなところで……<2000><200A>＄イヤだーーーーーーーーっ！！ | [200A:0005]Find Pearlton![2000]Not dying here![2000][200A:0004]Noooooooo!! |
| 3969 | <200A>＃もうダメーっ！　あとは<2000>かみさまに　おいのりするだけ！<2000>どうなっちゃうの　あたしたち！ | [200A:0003]We're done![2000]Pray to God now![2000]What'll we do? |
| 3970 | <200A>！ザリ？<2000>なにが　おきたザリ？<200A>　 | [200A:0001]Zari?[2000]What?![200A:0000] |
| 3971 | <200A>！ザリー……<2000>からだが　おもくなったザリー<200A>　 | [200A:0001]Zari...[2000]I'm heavier![200A:0000] |
| 3972 | <200A>！ザリ！<2000>ツメが　のびたザリ！<200A>　 | [200A:0001]Zari[2000]Big claws[200A:0000] |
| 3973 | <200A>！タイチョー！<2000>スゴクなった　きがします！<2000>がんばって　いくであります！<200A>　 | [200A:0001]Captain![2000]Feel stronger![2000]I'll try![200A:0000] |
| 3974 | <200A>！タイチョー！<2000>これからも　よろしく<2000>おねがいします！<200A>　 | [200A:0001]Captain![2000]Guide me[2000]onward![200A:0000] |
| 3975 | <200A>！うまれかわっても<2000>ガンバルであります！<200A>　 | [200A:0001]Reborn![2000]I'll try![200A:0000] |
| 3976 | <200A>！<200B>’<2000>すこし　おとなに<2000>なったみたーい！<200A>　 | [200A:0001][200B:0007][2000]I feel[2000]grown up![200A:0000] |
| 3977 | <200A>！あー！<2000>ビックリした！<200A>　 | [200A:0001]Ah![2000]Whoa![200A:0000] |
| 3978 | <200A>！あら？<2000>すこし　やせたかしら？<200A>　 | [200A:0001]Oh?[2000]Slimmer?[200A:0000] |
| 3979 | <200A>！ボクの　かっこう<2000>つよそうに　みえる？<200A>　 | [200A:0001]Do I look[2000]strong?[200A:0000] |
| 3980 | <200A>！どーしたんだ？<2000>なにが　おこったんだ？？<200A>　 | [200A:0001]What?[2000]What happened?[200A:0000] |
| 3981 | <200A>！あれ？？<2000>ボク　かっこよく<2000>なっちゃったよ！<200A>　 | [200A:0001]Huh?![2000]I look[2000]cool now![200A:0000] |
| 3982 | <200A>！うっ……<2000>わたしは　いままで<2000>なにを　やっていたのだろう……<200A>　 | [200A:0001]Ugh...[2000]What was I[2000]doing...?[200A:0000] |
| 3983 | <200A>！これが　ほんらいの<2000>すがたなのか……<200A>　 | [200A:0001]My true[2000]form...?[200A:0000] |
| 3984 | <200A>！すけて　しまったが<2000>だいじょうぶ　なのだろうか……<200A>　 | [200A:0001]See-through...[2000]Is it OK?[200A:0000] |
| 4096 | <200A>！ついに　<2003>％カラメラ<2003>　あつめの<2000>ぼうけんも　おわりじゃな<200A>　<2001><200A>！わしも　でんせつの　<2003>！カラメル<2003>　を<2000>みることができて　うれしいぞ<200A>　<2001><200A>！しかし　<2003>！<200B>　<2003>　の　ぼうけんは<2000>まだまだ　おわらないのじゃ<200A>　<2001><200A>！せかい　いちの<2000>ロボポンガーデナーを　めざす<2000>ぼうけんの　はじまりじゃ！<200A>　 | [200A:0001][2003:0005]Caramela[2003:0000] hunt[2000]over at last![200A:0000][2001][200A:0001]Legend [2003:0001]Caramel[2003:0000]![2000]Glad I saw it![200A:0000][2001][200A:0001][2003:0001][200B:0000][2003:0000]'s quest[2000]goes on![200A:0000][2001][200A:0001]New quest![2000]World's best[2000]Robopon gardener[200A:0000] |
| 4097 | <200A>！おめでとう！<2000>バトル　１００かい<2000>たっせいじゃ！<200A>　<2001><200A>！これで　<2003>！<200B>　<2003>　も<2000>いちにんまえの<2000>ロボポンバトラーじゃ<200A>　<2001><200A>！しかし　ゆだんしては　いかんぞ！<2000>うえには　うえが　おるからな<200A>　 | [200A:0001]Congrats![2000]100 battles[2000]done![200A:0000][2001][200A:0001]Now [2003:0001][200B:0000][2003:0000]:[2000]a true bot[2000]battler![200A:0000][2001][200A:0001]Stay sharp![2000]Stronger await![200A:0000] |
| 4098 | <200A>！おめでとう！<2000>ミニゲーム　５００かい　クリアー<2000>たっせいじゃ！<200A>　<2001><200A>！<2003>！<200B>　<2003>　は<2000>ミニゲームの　たつじんじゃな<200A>　 | [200A:0001]Bravo![2000]500 minigame[2000]clears![200A:0000][2001][200A:0001][2003:0001][200B:0000][2003:0000]:[2000]Minigame master![200A:0000] |
| 4099 | <200A>！ＧＢコンバート　せいこうじゃ！<200A>　<2001><200A>！ＧＢコンバートを　つかって<2000>こうりつよく　ロボポンを<2000>そだてるんじゃぞ<200A>　 | [200A:0001]GB Link worked![200A:0000][2001][200A:0001]Use it[2000]to raise bots[2000]efficiently![200A:0000] |
| 4101 | <200A>！ロボポンずかんの<2000>かんせいじゃ！<200A>　<2001><200A>！わしにも　できなかったことを<2000>やってしまうとは……<200A>　<2001><200A>！<2003>！<200B>　<2003>　は<2000>ロボポンはかせ　じゃな<200A>　 | [200A:0001]Bot Book[2000]done![200A:0000][2001][200A:0001]You did it![2000]I couldn't![200A:0000][2001][200A:0001][2003:0001][200B:0000][2003:0000]:[2000]Robopon expert![200A:0000] |
| 4102 | <200A>！ついに　<2003>％カラメラ<2003>　あつめの<2000>ぼうけんも　おわりですね<200A>　<2001><200A>！わたしも　でんせつの　<2003>！カラメル<2003>　を<2000>みることができて　うれしいです<200A>　<2001><200A>！しかし　<2003>！<200B>　<2003>　の　ぼうけんは<2000>まだまだ　おわりません<200A>　<2001><200A>！せかい　いちの<2000>ロボポンガーデナーを　めざす<2000>ぼうけんの　はじまりです！<200A>　 | [200A:0001][2003:0005]Caramela[2003:0000] hunt[2000]is now over.[200A:0000][2001][200A:0001]Legend [2003:0001]Caramel[2003:0000]![2000]A joy to see it.[200A:0000][2001][200A:0001][2003:0001][200B:0000][2003:0000]'s quest[2000]goes on.[200A:0000][2001][200A:0001]New quest:[2000]World's top[2000]Robopon gardener[200A:0000] |
| 4103 | <200A>！おめでとう！<2000>バトル　１００かい<2000>たっせいです！<200A>　<2001><200A>！これで　<2003>！<200B>　<2003>　も<2000>いちにんまえの<2000>ロボポンバトラーです<200A>　<2001><200A>！しかし　うえには　うえが　います<2000>ゆだんしないでくださいね<200A>　 | [200A:0001]Well done![2000]100 battles[2000]done.[200A:0000][2001][200A:0001][2003:0001][200B:0000][2003:0000]:[2000]a true bot[2000]battler.[200A:0000][2001][200A:0001]Stay alert.[2000]Stronger await.[200A:0000] |
| 4104 | <200A>！おめでとう！<2000>ミニゲーム　５００かい　クリアー<2000>たっせいです！<200A>　<2001><200A>！<2003>！<200B>　<2003>　は<2000>ミニゲームの　たつじんですね<200A>　 | [200A:0001]Bravo![2000]500 minigames[2000]cleared![200A:0000][2001][200A:0001][2003:0001][200B:0000][2003:0000]:[2000]Minigame master[200A:0000] |
| 4105 | <200A>！ＧＢコンバート　せいこうです！<200A>　<2001><200A>！ＧＢコンバートを　つかって<2000>こうりつよく　ロボポンを<2000>そだててください<200A>　 | [200A:0001]GB Link success![200A:0000][2001][200A:0001]Use it[2000]to raise bots[2000]efficiently.[200A:0000] |
| 4107 | <200A>！ロボポンずかんの<2000>かんせいです！<200A>　<2001><200A>！わたしにも　できなかったことを<2000>やってしまうなんて……<200A>　<2001><200A>！<2003>！<200B>　<2003>　は<2000>ロボポンはかせ　ですね<200A>　 | [200A:0001]Bot Book[2000]done.[200A:0000][2001][200A:0001]You did it.[2000]I could not.[200A:0000][2001][200A:0001][2003:0001][200B:0000][2003:0000]:[2000]Robopon expert.[200A:0000] |
| 4108 | ムーン＝ブルー | Moon Blue |
| 4109 | ファイア＝ブルー | Fire Blue |
| 4110 | ウォータ＝ブルー | Water Blue |
| 4111 | ツリー＝ブルー | Tree Blue |
| 4112 | ゴールド＝ブルー | Gold Blue |
| 4113 | ランド＝ブルー | Land Blue |
| 4114 | サニー＝ブルー | Sunny Blue |
