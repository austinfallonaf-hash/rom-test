# Bot-book biographies alpha

This cumulative partial English draft adds **184 native lines** (3694–3877):
**46 four-line bot-book biographies**. Coverage reaches **3,965 native records,
832 UI strings, 299 choices and three bitmap captions**. All preceding 3,781
catalog entries, active bytes and descriptors remain identical.

## Wording

Each biography keeps four separate native records. English may flow across the
four lines, retaining the paragraph's traits, jokes and qualifications rather
than forcing each Japanese line into its much shorter original allocation.
The source/English table below supports review without assuming that book order
matches the default-name roster order.

Details include the outdated sensor antenna; the special-metal nose drill;
recharging from household sockets without paying the power bill; the wrestler's
claimed 400 unbeaten bouts and gym dream; Bootan learning to work and automatic
stain removal; kogal preferences, expensive parts and money fussiness; racetrack
camera poses; Musashi's rival and two-sword duels; pirate exploits; recorded attack
data, Mach kicks and bullet-cutting saber skills; the nurse's syringe and fans;
Kodevian minions and sweets; carpenter loyalty and tools; energy-draining bites
and temporary immobility; steam jets, tail blades, heavy balls and rusty teeth;
energy delivery, female martial-artist memories, the toilet gag, precision tools,
hockey attacks and rich buyers; handmade treasures, wood/fire and the ancestral
pestle; poor phone reception and threatened discontinuation; flying with mini
bots, golden beam reflection and destructive rays; the approximate fivefold
bullet-train **charging force**, not a fivefold speed claim; knightly temperament,
deep-water armor, space conversion, four/six arms, horns and electric spear;
trial-run rarity, a girl fighter's charm, adaptable justice gear, Micro's shield
and laser blade; mutation and jelly body; nauseating mushroom-like jets; space
station intelligence; unknown materials and possible undersea ancestry; and the
unthreatening ghost of a mistreated discarded bot.

The source's male appearance/female thinking, feigned frailty, arm strength and
heavy head are retained in 3782–3785. Claims and rumors remain claims and rumors;
no bio prose changes combat stats, abilities, production, shops, prices or events.
Bootan (ブータン), Rude (ルード) and Kodevian (コデビアン) are provisional project
terms. Bootan is the name in the source backstory, not a silent replacement of
the earlier Buppy (ブッピー) label. Kogal keeps the source youth-fashion reference.

## Reader, font and storage

Static inspection identifies the reader at **0x109BB0–0x109C88**. It loops over
four rows and draws record `3694 + 4*selected_entry + row` at native x=52,
y=166+14*row. Source rows have 12–18 glyphs. These are independent native strings,
not fixed-stride minigame grids or dialogue commands.

A new guarded `book_line` path accepts only IDs 3694–3877 and 1–36 printable
ASCII cells, without newline/control words. The reader's horizontal scale at
**0x109C04** changes from **3C013F80** (1.0) to **3C013F00** (0.5). Vertical scale,
row positions, ID calculation and native draw call stay exact. Thirty-six
six-pixel cells occupy the source's original 216-pixel maximum. The builder
requires this exact scale edit when building book lines; generic label limits,
dialogue validation and all fifteen fixed-grid layouts remain unchanged.
There are now **86 guarded layout words**.

Existing translated donor padding totals 14,834 bytes but is fragmented into
gaps no larger than 40 bytes. The longer book lines cannot fit those intervals.
Each instead declares an eight-byte-aligned integer `book_storage_offset` in
original 0xFF-filled padding after the existing RAW2 graphic. The graphic ends
at 0x1FFD3C4; book storage starts at **0x1FFD3D0**. The native descriptor loader
accepts full 32-bit pool-relative pointers and rounds read allocations to eight
bytes, while the glyph loop consumes only the declared count.

All 184 lines use **10,694 encoded bytes**, in **11,248 bytes of aligned
allocations**, ending at **0x1FFFFC0**. The final **64 bytes** remain 0xFF. Each
count/pointer redirects to the new text; every original Japanese book slot stays
unchanged. Zero alignment padding lies outside each declared count. No ROM-size
increase, interpreter hook or save-format change is used. Do not spend these
placements or the final 64 bytes casually: growing a line needs a reviewed
allocation change and all global overlap guards still apply.

Guards reject wrong IDs, source controls/widths, non-ASCII/newline/overwide text,
missing/misaligned/out-of-range/occupied storage, duplicate/overlapping edits,
legacy donor storage on book lines and book offsets on other kinds. These lines
are not donors. The graphics replacement and book text use the same overlap
checks. The 249 earlier donor-stored labels in 155 donors, original label source
slots, raw graphic, fifteen grids and 38 minigame-reader instructions remain exact.

## Runtime evidence and limits

The exact final ROM cold-boots and loads native file A with day 2, 500G,
player name, saved Japanese Merlin nickname, original stats, Charm and Fire v1.
Book entry 38 displays Merlin and all four actual biography records 3842–3845.
The record order is separate from the general name roster. A descriptor-only
preview repeats the real 36-cell line 3757 in every book-line slot; its screenshot
shows the full text in all four native detail rows. The release retains each
actual biography. Both runs use separate native EEPROM copies, unchanged from
the reference. No in-game save or savestate load/create is used. Evidence and
exact identities are in local/bot-book-evidence. Other biographies remain
build-validated; the book introduction, graphical headings and data labels
remain Japanese.

All 184 lines are source/width/pointer/count/actual-ROM checked. These checks do
not establish gameplay coverage of every biography or its species mapping.
Other book entries and earlier fuel/chore/minigame/pest/reaction/name/newline/
donor/regional branches, capacity warnings, five anchored pages, graphical
Parts frames and VS/Transfer Pak retain their previous gameplay limits.

Final ROM MD5: `6AB9FC59830C95098877680C00730FE2`.
SHA-256: `c920c441880110d6280edc072d8e64197ff0d334fa477d5c359897d4e8b3896e`.
The 32 MiB ROM retains CIC-6102 CRC1/CRC2 `FFA89600 C278C65F`.

## Build and recovery

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/bot-book-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/bot-book-alpha.z64 --patch local/bot-book-alpha.bps
```

Apply the BPS directly to the exact Japanese original without stacking patches.
Floating IPS independently reproduces the ROM and read-only chksum64 agrees with
its header. All **143 tests** pass in source and clean restoration. Nine new tests
cover the reader-specific width, source/ASCII, placement/alignment/padding, layout
requirement, pointer/count behavior, overlap and guard isolation. The actual-ROM
proof checks all new and prior text and permits changes only in the 184 book
descriptors, aligned book tail and single horizontal-scale word. The previous
equipment ROM and BPS reproduce exactly with the new toolchain and prior layout.

The AES-256 backup uses two verified ciphertext parts and the existing passphrase,
kept outside Git. Clean restoration checks **896 payload files**, source
revision, ROM/BPS/save/evidence hashes, executable modes, emulator library symlink
and the exact-ROM 16Kbit EEPROM profile. See backups/README.md and RESTORE.md.

Next: native dialogue from **3918**; 3878–3917 was translated earlier. Keep the
48 cut placeholders and 18 portrait-only entries intact. Preserve all earlier
249 donor ranges and 184 book placements, and inspect source controls before
writing the remaining late dialogue. No additional fixed-grid IDs are verified.

## Four-line biographies and allocation ledger

English lines are reflowed only within each four-record biography. The table
lists source/English lines individually; storage is an absolute ROM offset.

| ID | Source | English | Storage |
| --- | --- | --- | --- |
| 3694 | しょきがた　ベーシックロボポン | An early basic Robopon model. | 0x1ffd3d0 |
| 3695 | げんざいは　もう　つくられていない | No longer produced. | 0x1ffd410 |
| 3696 | あたまの　かんちアンテナも | Even its head-mounted sensor | 0x1ffd438 |
| 3697 | いまでは　のうりょくてきに　ひくい | antenna is now rather weak. | 0x1ffd470 |
| 3698 | はなの　きょだいドリルは | Its huge nose drill is made of | 0x1ffd4a8 |
| 3699 | しんかいはつの　とくしゅ　きんぞく | newly developed special metal. | 0x1ffd4e8 |
| 3700 | じめんも　かたい　てっぱんも | It drills earth and hard | 0x1ffd528 |
| 3701 | もんだいにしない　いりょくだ | steel plates with ease. | 0x1ffd558 |
| 3702 | おうちにある　ソケットを　みかけると | A meticulous fellow that plugs | 0x1ffd588 |
| 3703 | からだの　コンセントを　さしこみ | into household sockets | 0x1ffd5c8 |
| 3704 | じゅうでんする　きちょうめんな　ヤツ | to recharge whenever it sees one. | 0x1ffd5f8 |
| 3705 | もちろん　でんきだいは　はらわない | It never pays the power bill. | 0x1ffd640 |
| 3706 | プロレスように　つくられた　ロボポン | A bot built for pro wrestling. | 0x1ffd680 |
| 3707 | パワーファイトで　てきを　はかいする | It smashes foes with raw power. | 0x1ffd6c0 |
| 3708 | じしょう　４００しあい　まけしらず | Claims 400 bouts without a loss. | 0x1ffd700 |
| 3709 | ゆめは　ジムの　けいえい | Dreams of running its own gym. | 0x1ffd740 |
| 3710 | はたらくことを　おぼえた　ブータンが | Bootan learned how to work | 0x1ffd780 |
| 3711 | クリーニングロボポンに　だいへんしん | and became a cleaning bot! | 0x1ffd7b8 |
| 3712 | がんこな　よごれも　ぜんじどうで | It washes even stubborn stains | 0x1ffd7f0 |
| 3713 | しんぴんどうように　あらってくれる | automatically, good as new. | 0x1ffd830 |
| 3714 | コギャルのしこうを　インプットした | Programmed with a kogal's tastes, | 0x1ffd868 |
| 3715 | ぜんだいみもんの　わがままロボポン | this bot is incredibly selfish. | 0x1ffd8b0 |
| 3716 | いいパーツをつけないと　おこるし | It gets mad without fine parts | 0x1ffd8f0 |
| 3717 | やたらと　おかねに　うるさいのだ | and is very fussy about money. | 0x1ffd930 |
| 3718 | レースじょうで　よくみられるロボポン | Often seen at racetracks. | 0x1ffd970 |
| 3719 | カメラこぞうの　シャッターおんに | It senses camera buffs' shutters | 0x1ffd9a8 |
| 3720 | びんかんにはんのうし　すばやく | and instantly strikes a pose: | 0x1ffd9e8 |
| 3721 | ポーズをとる　きのうがついている | a feature built into its body. | 0x1ffda28 |
| 3722 | てんかむてきの　にとうりゅうは | Its peerless two-sword style | 0x1ffda68 |
| 3723 | さいこうの　きれあじを　ほこる | boasts the keenest cutting edge. | 0x1ffdaa0 |
| 3724 | １たい１の　しょうぶでは　まけしらず | Undefeated in one-on-one duels, | 0x1ffdae0 |
| 3725 | サムライだましいを　もっている | it has a true samurai spirit. | 0x1ffdb20 |
| 3726 | ムサシの　しょうがいのライバル | Musashi's lifelong rival. | 0x1ffdb60 |
| 3727 | すばやいうごきで　てきを　かくらんし | It confuses foes with swift moves, | 0x1ffdb98 |
| 3728 | かれいな　けんさばきで　きりさく | then cuts with elegant swordplay: | 0x1ffdbe0 |
| 3729 | これが　ひっさつの　フルコースだ | a full course of deadly attacks. | 0x1ffdc28 |
| 3730 | ねっけつスポーツマンの　ロボポン | A passionate sportsman bot | 0x1ffdc68 |
| 3731 | まがったことが　だいきらいで | that hates anything dishonest. | 0x1ffdca0 |
| 3732 | おんなのコからの　にんきも　たかい | Popular with girls, it is like | 0x1ffdce0 |
| 3733 | たよれる　アニキみたいな　ヤツだ | a big brother you can count on. | 0x1ffdd20 |
| 3734 | ななつの　うみを　わたってきた | A pirate bot that has | 0x1ffdd60 |
| 3735 | かいぞくがたの　ロボポン | sailed all seven seas. | 0x1ffdd90 |
| 3736 | かずおおくの　げきとうを　せいした | Victorious in countless fierce | 0x1ffddc0 |
| 3737 | つわものといって　いいだろう | battles, it is a true veteran. | 0x1ffde00 |
| 3738 | たたかった　てきの　こうげきデータは | A fighting bot that records | 0x1ffde40 |
| 3739 | すべて　きおくする　かくとうロボポン | all foes' attack data in battle. | 0x1ffde78 |
| 3740 | かたい　こぶしは　いわをもくだき | Its hard fists smash rocks; its | 0x1ffdeb8 |
| 3741 | マッハキックで　てつを　けりやぶる | Mach kicks pierce iron plates. | 0x1ffdef8 |
| 3742 | かずかずのあらなみを　のりこえてきた | A pirate bot that has | 0x1ffdf38 |
| 3743 | かいぞくがたの　ロボポン | weathered countless rough seas. | 0x1ffdf68 |
| 3744 | サーベルさばきには　ていひょうがあり | Its famous saber skills can even | 0x1ffdfa8 |
| 3745 | とんでくるだんがんを　きりおとすほど | slice bullets out of the air. | 0x1ffdfe8 |
| 3746 | はくいのまぶしい　かんごふロボポン | A nurse bot in bright white. | 0x1ffe028 |
| 3747 | おおきなちゅうしゃきを　かかえて | Carrying an enormous syringe, | 0x1ffe060 |
| 3748 | いそがしくびょういんを　はしりまわる | it rushes around the hospital. | 0x1ffe0a0 |
| 3749 | だんせいに　いじょうな　にんきがある | Wildly popular with men. | 0x1ffe0e0 |
| 3750 | ルードロボポンの　たいしょうかく | A leader among the Rude Robopon. | 0x1ffe110 |
| 3751 | コデビアンぐんだんを　あやつり | Commands an army of Kodevians | 0x1ffe150 |
| 3752 | せかいせいふくを　たくらんでいる | and plots to conquer the world. | 0x1ffe190 |
| 3753 | あまい　おかしが　だいこうぶつ | Loves sweet treats. | 0x1ffe1d0 |
| 3754 | したまちうまれの　だいくロボポン | A carpenter born downtown. | 0x1ffe1f8 |
| 3755 | くちはわるいが　しごとは　はやい | Foul-mouthed, but quick at work. | 0x1ffe230 |
| 3756 | ぎりにんじょうに　あつくて | Deeply loyal and warmhearted, | 0x1ffe270 |
| 3757 | クギと　トンカチを　てばなさない | it never lets go of hammer or nails. | 0x1ffe2b0 |
| 3758 | おんなドラキュラがたの　ロボポン | A female Dracula-type bot. | 0x1ffe2f8 |
| 3759 | かみついて　エネルギーを　すいとる | Its bites suck away energy. | 0x1ffe330 |
| 3760 | はがたがつくと　しばらくのあいだ | The tooth marks leave victims | 0x1ffe368 |
| 3761 | うごきが　とめられてしまう | unable to move for a short time. | 0x1ffe3a8 |
| 3762 | すいじょうきの　ちからでうごく | A rare steam-powered Robopon. | 0x1ffe3e8 |
| 3763 | めずらしいタイプの　スチームロボポン | When its surface turns red-hot, | 0x1ffe428 |
| 3764 | ひょうめんが　まっかになると | it lets out a hissing jet | 0x1ffe468 |
| 3765 | とてもあついゆげを　シューッとだす | of extremely hot steam. | 0x1ffe4a0 |
| 3766 | クールな　ころしやロボポン | A cool assassin Robopon. | 0x1ffe4d0 |
| 3767 | しっぽのカッターで　きりきざみ | It slices foes with its tail blade | 0x1ffe500 |
| 3768 | おもいたまで　とどめをさす | and finishes them with a heavy ball. | 0x1ffe548 |
| 3769 | コイツにねらわれては　いきのこれない | Once targeted, no one survives. | 0x1ffe590 |
| 3770 | するどい　はの　ならんだくちは | Its rows of sharp teeth easily | 0x1ffe5d0 |
| 3771 | きんぞくを　かんたんに　かみくだく | crunch through metal. | 0x1ffe610 |
| 3772 | しかし　すぐ　サビてしまうので | They rust quickly, so it must | 0x1ffe640 |
| 3773 | まいばんの　はみがきは　かかせない | brush its teeth every night. | 0x1ffe680 |
| 3774 | エネルギーをはこぶ　ロボポンのため | A bot that transports energy. | 0x1ffe6b8 |
| 3775 | ルードたちに　よく　ねらわれるが | The Rudes often target it, | 0x1ffe6f8 |
| 3776 | せんとうのうりょくが　たかく | but its great fighting ability | 0x1ffe730 |
| 3777 | かんたんに　やられることは　ない | makes it very hard to defeat. | 0x1ffe770 |
| 3778 | ゆうかんな　おんなかくとうかたちの | Programmed with the memories | 0x1ffe7b0 |
| 3779 | きおくが　インプットされている | of brave female martial artists. | 0x1ffe7e8 |
| 3780 | パワー　テクニック　スピードの | A fighter with a perfect mix of | 0x1ffe828 |
| 3781 | ３びょうし　そろった　ファイターだ | power, technique and speed. | 0x1ffe868 |
| 3782 | みためはおとこ　しこうはおんな | Male looks, a female mind. | 0x1ffe8a0 |
| 3783 | かよわいふりをして　ほんとうは | It acts frail, but has tremendous | 0x1ffe8d8 |
| 3784 | ものすごく　わんりょくがつよい | arm strength. It always holds up | 0x1ffe920 |
| 3785 | あたまがおもくて　いつもささえている | its heavy head. | 0x1ffe960 |
| 3786 | いつも　ピカピカボディの | A clean-loving toilet bot | 0x1ffe980 |
| 3787 | きれいずきな　トイレがたロボポン | with an ever-sparkling body. | 0x1ffe9b8 |
| 3788 | やくにたちたいのに　きみがわるいので | It wants to help, but creeps people | 0x1ffe9f0 |
| 3789 | だれも　つかってくれない | out, so nobody will use it. | 0x1ffea38 |
| 3790 | せいみつきかいを　しゅうりしたり | A tool bot that repairs and | 0x1ffea70 |
| 3791 | ぶんかいする　こうぐロボポン | dismantles precision machinery. | 0x1ffeaa8 |
| 3792 | さまざまな　パーツこうかんをして | By swapping its various parts, | 0x1ffeae8 |
| 3793 | バトルでも　いりょくを　はっきする | it shows its strength in battle. | 0x1ffeb28 |
| 3794 | たたかうあいてを　バラバラにしないと | A cruel Robopon, never satisfied | 0x1ffeb68 |
| 3795 | きがすまない　ざんこくロボポン | until its foe is torn to pieces. | 0x1ffeba8 |
| 3796 | ショルダータックルで　ぶちかまし | It slams in with a shoulder tackle, | 0x1ffebe8 |
| 3797 | とどめは　スティックで　メチャなぐり | then clubs foes with its stick. | 0x1ffec30 |
| 3798 | おおがねもちが　じまんをするために | The rich often buy it to show off. | 0x1ffec70 |
| 3799 | かうことがおおく　よわいロボポンなら | Weak Robopon flee at the mere | 0x1ffecb8 |
| 3800 | すがたをみただけで　にげだしてしまう | sight of it. It goes on rampages, | 0x1ffecf8 |
| 3801 | わんりょくにものをいわせて　あばれる | letting its brute strength speak. | 0x1ffed40 |
| 3802 | おたからど　ナンバーワンで　だれもが | The greatest treasure: a Robopon | 0x1ffed88 |
| 3803 | ゆめみる　てのとどかない　ロボポン | everyone dreams of but cannot buy. | 0x1ffedc8 |
| 3804 | いったいいったいが　てづくりなので | Each is handmade, so they | 0x1ffee10 |
| 3805 | たいりょうせいさんが　できない | cannot be mass-produced. | 0x1ffee48 |
| 3806 | きで　できた　めずらしいロボポン | A rare bot made of wood. | 0x1ffee78 |
| 3807 | ほのおには　とても　よわいが | Very weak to fire, but otherwise | 0x1ffeea8 |
| 3808 | それいがいなら　もちこたえられる | it can hold its own. Its pestle | 0x1ffeee8 |
| 3809 | キネは　せんぞだいだいの　いっぴん | is a treasured family heirloom. | 0x1ffef28 |
| 3810 | けいたいがた　でんわきロボポン | A portable-phone Robopon. | 0x1ffef68 |
| 3811 | でんぱの　よわいちいきに　いくと | It cannot fight in places | 0x1ffefa0 |
| 3812 | たたかうことが　できなくなる | with poor reception. Rumors say | 0x1ffefd8 |
| 3813 | ちかく　せいさんちゅうしの　うわさ | production will end soon. | 0x1fff018 |
| 3814 | ミニロボポンを　せなかにのせ | It coils up and flies through | 0x1fff050 |
| 3815 | とぐろをまいて　おおぞらを　とぶ | open skies with mini Robopon aboard. | 0x1fff090 |
| 3816 | おうごんボディは　ビームをはねかえし | Its golden body reflects beams; | 0x1fff0d8 |
| 3817 | くちから　はかいこうせんを　はく | its mouth fires destructive rays. | 0x1fff118 |
| 3818 | でんせつの　かくとうロボポン | A legendary fighting Robopon. | 0x1fff160 |
| 3819 | すさまじい　とっしんパワーは | Its charging force is about five | 0x1fff1a0 |
| 3820 | なんと　しんかんせんの　やく５ばい | times that of a bullet train! | 0x1fff1e0 |
| 3821 | がんめんこうげきが　だいきらい | It hates being struck in the face. | 0x1fff220 |
| 3822 | くうきを　きりさくほどの　スピードで | A female knight bot whose | 0x1fff268 |
| 3823 | けんをあつかう　おんなきしロボポン | sword moves fast enough to cut air. | 0x1fff2a0 |
| 3824 | きしょうも　あらく　まけずぎらい | Fierce-tempered and hates losing. | 0x1fff2e8 |
| 3825 | あまくみていると　ケガをするぞ | Underestimate her and get hurt! | 0x1fff330 |
| 3826 | しんかいはつの　ロボポン | A newly developed bot. | 0x1fff370 |
| 3827 | すいあつに　たえられるように | Its armor is very sturdy to | 0x1fff3a0 |
| 3828 | そうこうは　かなりがんじょうだ | withstand deep-water pressure. | 0x1fff3d8 |
| 3829 | おとなしく　たたかいがきらい | It is gentle and hates fighting. | 0x1fff418 |
| 3830 | ザリガを　うちゅうようにかいぞう | Zariga modified for space. | 0x1fff458 |
| 3831 | エイリアンと　たたかうために | Armed with assorted equipment | 0x1fff490 |
| 3832 | さまざまな　そうびで　みをかためた | to battle aliens, its sharp claws | 0x1fff4d0 |
| 3833 | するどいツメで　てきもタジタジ | leave enemies reeling. | 0x1fff518 |
| 3834 | くっきょうな　ロボポンせんし | A tough bot warrior. | 0x1fff548 |
| 3835 | よんほんのうでは　りったいてきに | Its four arms attack and defend | 0x1fff570 |
| 3836 | こうげき　ぼうぎょを　くりかえし | from every angle, over and over. | 0x1fff5b0 |
| 3837 | あいてを　けっして　にがさない | It never lets its opponent escape. | 0x1fff5f0 |
| 3838 | たたかうためだけに　うみだされた | The ultimate combat bot, | 0x1fff638 |
| 3839 | さいきょうの　せんとうロボポン | born solely to fight. Its six | 0x1fff668 |
| 3840 | ろっぽんのうでと　あたまのつので | arms and head horns wound foes; | 0x1fff6a8 |
| 3841 | きずつけ　でんじやりで　とどめをさす | its electric spear finishes them. | 0x1fff6e8 |
| 3842 | ロボまるの　おんなのこバージョン | Robomaru's girl version. | 0x1fff730 |
| 3843 | テストてきに　せいさんされたので | Made only as a trial run, it is | 0x1fff760 |
| 3844 | かずがすくなく　マニアのあいだでは | rare and commands high prices | 0x1fff7a0 |
| 3845 | こうがくで　とりひきされている | among collectors. | 0x1fff7e0 |
| 3846 | せいぎのみかたを　きどっている | A girl fighter bot that plays | 0x1fff808 |
| 3847 | おんなのこファイターロボポン | the champion of justice. | 0x1fff848 |
| 3848 | とくいの　セクシーさっぽうには | Even villains fall for its | 0x1fff878 |
| 3849 | あくとうも　メロメロなのだ | specialty: sexy fighting moves. | 0x1fff8b0 |
| 3850 | せいぎのために　うまれたロボポン | A bot born to fight for justice. | 0x1fff8f0 |
| 3851 | そうびを　いろいろとつけかえることで | By swapping its many pieces of gear, | 0x1fff930 |
| 3852 | どんなあいてにも　たいおうできる | it can handle any opponent. | 0x1fff978 |
| 3853 | たよりになる　ヤツがあらわれたゾ | A dependable new hero is here! | 0x1fff9b0 |
| 3854 | ミクロが　かんぜんぶそうしたすがた | Micro in full combat gear. | 0x1fff9f0 |
| 3855 | シールドで　こうげきを　はねかえし | Its shield deflects attacks; | 0x1fffa28 |
| 3856 | レーザーブレードで　はんげきする | its laser blade strikes back. | 0x1fffa60 |
| 3857 | どんなワルモノにも　くっしない | It never yields to any villain. | 0x1fffaa0 |
| 3858 | いかなるきせきが　うみだしたのか？ | What miracle could have made it? | 0x1fffae0 |
| 3859 | とつぜんへんいした　スーパーロボポン | A super bot born of mutation. | 0x1fffb20 |
| 3860 | ゼリーのような　やわらかいからだには | Its soft, jellylike body stays fine | 0x1fffb60 |
| 3861 | いくらこうげきされても　へっちゃら | no matter how often it is attacked. | 0x1fffba8 |
| 3862 | つちから　はえる　キモい　ロボポン | A creepy bot that sprouts | 0x1fffbf0 |
| 3863 | はきけが　するほど　クチャいにおい | from soil. Its stink is nauseating. | 0x1fffc28 |
| 3864 | ねどこさがしに　ジェットで　いどう | It jets about looking for a bed. | 0x1fffc70 |
| 3865 | キノコに　にているが　たべられない | Mushroomlike, but inedible. | 0x1fffcb0 |
| 3866 | うちゅうステーション　うまれの | A state-of-the-art space Robopon | 0x1fffce8 |
| 3867 | さいしんがた　スペースロボポン | born on a space station. | 0x1fffd28 |
| 3868 | あたまが　ものすごく　よく | Extremely intelligent, it does | 0x1fffd58 |
| 3869 | なにを　やっても　パーフェクトだ | everything to perfection. | 0x1fffd98 |
| 3870 | うちゅうから　きた　ナゾの　ロボポン | A mysterious Robopon from space. | 0x1fffdd0 |
| 3871 | いったい　なにで　できているのか | Its material and inner workings | 0x1fffe10 |
| 3872 | どんな　こうぞうなのか　ふめい | are unknown. It may be an ancestor | 0x1fffe50 |
| 3873 | かいていじんの　そせんらしい | of the undersea people. | 0x1fffe98 |
| 3874 | そまつにあつかわれて　すてられた | A ghost Robopon born from the | 0x1fffec8 |
| 3875 | ロボポンが　おんねんとなって | grudge of an abused, discarded bot. | 0x1ffff08 |
| 3876 | ばけて　でた　ゆうれいの　ロボポン | It came back to haunt the world, | 0x1ffff50 |
| 3877 | しかし　ぜんぜん　こわくない | but is not scary at all. | 0x1ffff90 |
