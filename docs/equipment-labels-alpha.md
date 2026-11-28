# Equipment labels alpha

This cumulative partial English draft adds **135 native records**: **127 equipment
labels** at 3537–3664, skipping the earlier Charm 3604, and **eight Pearlton fuel
warnings** at 3665–3672. Coverage reaches **3,781 native records, 832 UI strings,
299 choices and three bitmap captions**. All preceding 3,646 catalog entries,
active bytes and descriptors remain identical.

## Wording

Names follow existing part/move components where those establish a spelling:
Knuckle, Hammer, Tiger, Mad, Gaia, Gun, Vulcan, Laser, Beam, Scan, Club, Mace,
Power, Doom, Blood, Ashura, Yasha, Zeek, Wise, Win, Cannon, Mine, Rocket and
Missile. Mad Arm/Scan Arm follow the established short components; Doom Hand
retains the project's earlier rendering of Death. Martial arts, swords, bows,
aircraft, ship and tank equipment keep their distinct source identities.

Unfamiliar proper names remain provisional: Wolf Hang preserves ハング instead
of silently changing it to Fang; Raint Hand and Vaid Hand retain ライント and
ヴァイド without inventing Void. Tyrell, Cave, Katock, Bren, Roppo, Rattle and
Erikol are provisional readings. Battle Gammar preserves ガンマー rather than
silently substituting Gunner. The source-to-English table below permits review.
The aircraft きじゅう and tank マシンガン both read Machine Gun while retaining
distinct IDs/effects. Sea Mine distinguishes きらい from tank マイン (Mine).
20mm, 36mm and 46mm Cannon retain the exact source calibers. Charm 3604 remains
unchanged. These are draft project terms, not claimed official localizations.

Fuel warnings retain Pearlton as fuel, escalating shortages, waste warnings,
the ship stopping and GAME OVER, and the last-resort sale of bots to a dealer
for Pearlton. Dealer condenses 回収業者 without claiming an unverified facility
or adding a new mechanic. The two speakers retain different tones and their
farewells. All eight original portraits, resets, line/page controls and arguments
remain in exact order; no new page exceptions or newline opt-ins are introduced.

## Storage and screen layout

Eight new labels fit inline: Mad Arm 3547, Claw 3582, Wing 3627, Jet 3628,
Bomb 3635, Screw 3637, Wave 3640 and Cannon 3655. The other **119 labels**
use **2,280 bytes** in explicit translated donor tails. Best-fit decreasing
allocation subtracts all prior occupied ranges and each donor's live encoded
text before choosing a gap. All 119 selected new donor allocations are dialogue;
no fuel warning is used as a donor. Earlier 130 stored-label placements remain
fixed. The cumulative catalog has **249 stored labels in 155 donors**. Stored
source slots retain their original Japanese bytes; only count/pointer descriptors
redirect the labels. Every range is aligned, within its donor allocation and
disjoint. Changes to donor translations that collide with labels fail the build.

Names contain at most sixteen native ASCII cells. The longest is **Hell
Caterpillar (3652, sixteen cells)**; Pickpocket Hand uses fifteen. A pre-layout
preview revealed that the full-width profile caption clipped Hell Caterpillar.
Four source-guarded MIPS words change horizontal scale from 1.0 to 0.5:

| ROM offset | Context | Source | Target |
| --- | --- | --- | --- |
| 0x21B3A8 | Bot profile equipment name, x=188 / y=112 | 3C013F80 | 3C013F00 |
| 0x217540 | Equipment selection right-column names, x=188 / original row y | 3C013F80 | 3C013F00 |
| 0x216604 | Gear Set initial equipped caption, x=48 / y=106 | 3C013F80 | 3C013F00 |
| 0x2171C0 | Gear Set equipped caption during selection, x=48 / y=106 | 3C013F80 | 3C013F00 |

All four calls retain vertical scale 1.0, coordinates, record-ID lookup and the
native record draw call (jal 0x41EA4). Six-pixel Latin cells fit a sixteen-cell name
in 96 pixels. The existing composed-move scale at 0x219AD0 stays unchanged.
There are now 85 guarded layout words. No item ID, stats, effects, quantities,
inventory, ship fuel or save behavior is changed. All fifteen earlier fixed
grids and all 38 guarded minigame-reader instructions stay unchanged.

## Runtime evidence and limits

The exact final ROM cold-boots and loads a separate reference EEPROM copy.
File A retains day 2, 500G, the player name and saved Japanese Merlin nickname,
Caster/Water, Charm, Fire v1, HP/EP 22, ATK 29, DEF 30, SPD 20, CPU 1 and
200 Orbs. Reference/default/isolated EEPROMs keep the original hash. No in-game
save or savestate load/create is used.

A separate preview changes only record 3604's eight-byte descriptor to the final
3652 descriptor. It displays the real stored Hell Caterpillar bytes in Charm's
fields while leaving equipment IDs, stats, inventory and saved data untouched.
The preview verifies that the full sixteen-cell name fits the profile and
Gear Set equipped-part caption after condensation. The right-hand inventory is empty in
this save, so its item rows are checked by source/disassembly only. Its BPS applies to the final translated ROM,
not the original, and is test evidence only; the release retains Charm. Exact
ROM/preview identities, screenshots and completed emulator logs are under
local/equipment-labels-evidence. Preview scenes do not prove that Merlin can
equip the actual Hell Caterpillar part or that it is obtainable at this point.

All 127 names are source/storage/actual-ROM validated; only the longest-name
fixture and ordinary Charm screens were observed. Other item contexts, including
other profile readers, shop/battle captions and graphical Parts frames, need
checks. Fuel-warning events were not triggered. Earlier chore/minigame/pest/
reaction/name/newline/donor/regional branches, capacity warnings, five anchored
pages and VS/Transfer Pak also retain their previous gameplay limits.

Final MD5: `89C91C559F9740CF8520542EEFFB339F`.
SHA-256: `d0a83d8970895ffdb01eab0539673baf65e277ba25d6433b5dea2e5ceefcf667`.
The 32 MiB ROM retains CIC-6102 CRC1/CRC2 `FFA89600 C278C65F`.

## Build and recovery

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/equipment-labels-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/equipment-labels-alpha.z64 --patch local/equipment-labels-alpha.bps
```

Apply the release BPS directly to the exact Japanese original. Floating IPS
independently reproduces the ROM and read-only chksum64 agrees with its header.
All **134 tests** pass in source and clean restoration. The additional byte
proof checks the exact 135 additions, warning controls, all prior active bytes/
descriptors, all 249 stored labels and all four isolated scale edits.

The AES-256 backup uses two verified ciphertext parts and the existing passphrase,
kept outside Git. Reassembly and decryption reproduce the packaged ZIP. Clean
restoration verifies **865 payload files**, source revision, ROM/BPS/
save/evidence hashes, executable modes, emulator library symlink and exact-ROM
16Kbit EEPROM profile. See backups/README.md and RESTORE.md.

Next: bot-book text from **3694**; 3673–3693 are already translated. Inspect
its four-line reading layout and varying 12–18-cell native widths before deciding
on encoding. Do not force unverified records through the existing grid path or
discard text to satisfy a generic label guard. Preserve every occupied donor
range and all earlier source controls.

## New equipment and allocation ledger

Offsets are bytes relative to each donor's original allocation; inline labels
retain their original slots. Counts/pointers and every stored byte are checked
against the actual built ROM.

| ID | Source | English | Storage |
| --- | --- | --- | --- |
| 3537 | ナックルアーム | Knuckle Arm | 182 + 244 (22 bytes) |
| 3538 | ヘヴィナックル | Heavy Knuckle | 426 + 388 (26 bytes) |
| 3539 | ハンマーアーム | Hammer Arm | 52 + 130 (20 bytes) |
| 3540 | ヘヴィハンマー | Heavy Hammer | 207 + 78 (24 bytes) |
| 3541 | サンボアーム | Sambo Arm | 223 + 350 (18 bytes) |
| 3542 | ボクサーアーム | Boxer Arm | 323 + 144 (18 bytes) |
| 3543 | ムエタイアーム | Muay Thai Arm | 1746 + 228 (26 bytes) |
| 3544 | ウルフハング | Wolf Hang | 331 + 148 (18 bytes) |
| 3545 | タイガーアーム | Tiger Arm | 390 + 276 (18 bytes) |
| 3546 | ぶとうハンド | Martial Hand | 502 + 168 (24 bytes) |
| 3547 | ぼうそうアーム | Mad Arm | inline |
| 3548 | ダガーアーム | Dagger Arm | 60 + 134 (20 bytes) |
| 3549 | ソードアーム | Sword Arm | 395 + 30 (18 bytes) |
| 3550 | サムライソード | Samurai Sword | 1936 + 228 (26 bytes) |
| 3551 | ムラマサアーム | Muramasa Arm | 590 + 194 (24 bytes) |
| 3552 | トマホーク | Tomahawk | 70 + 158 (16 bytes) |
| 3553 | ライントハンド | Raint Hand | 221 + 170 (20 bytes) |
| 3554 | ピックアーム | Pick Arm | 113 + 288 (16 bytes) |
| 3555 | レイピアアーム | Rapier Arm | 325 + 272 (20 bytes) |
| 3556 | スピアアーム | Spear Arm | 418 + 306 (18 bytes) |
| 3557 | グレイブアーム | Glaive Arm | 424 + 274 (20 bytes) |
| 3558 | ヴァイドハンド | Vaid Hand | 430 + 484 (18 bytes) |
| 3559 | ハーブアーム | Herb Arm | 285 + 96 (16 bytes) |
| 3560 | タロットアーム | Tarot Arm | 535 + 254 (18 bytes) |
| 3561 | ミスリルアーム | Mithril Arm | 242 + 54 (22 bytes) |
| 3562 | エンゼルアーム | Angel Arm | 694 + 112 (18 bytes) |
| 3563 | ゴッドハンド | God Hand | 300 + 190 (16 bytes) |
| 3564 | ミカドアーム | Mikado Arm | 451 + 230 (20 bytes) |
| 3565 | ルーンアーム | Rune Arm | 364 + 292 (16 bytes) |
| 3566 | ウラヌスハンド | Uranus Hand | 411 + 94 (22 bytes) |
| 3567 | じょうかハンド | Purifying Hand | 518 + 74 (28 bytes) |
| 3568 | ジャッジハンド | Judge Hand | 524 + 78 (20 bytes) |
| 3569 | ガイアハンド | Gaia Hand | 812 + 30 (18 bytes) |
| 3570 | ガンハンド | Gun Hand | 528 + 276 (16 bytes) |
| 3571 | ライフルアーム | Rifle Arm | 830 + 146 (18 bytes) |
| 3572 | ショットガン | Shotgun | 7 + 238 (14 bytes) |
| 3573 | ガトリング | Gatling | 85 + 300 (14 bytes) |
| 3574 | バルカンアーム | Vulcan Arm | 542 + 142 (20 bytes) |
| 3575 | グレネード | Grenade | 101 + 126 (14 bytes) |
| 3576 | バズーカアーム | Bazooka Arm | 495 + 244 (22 bytes) |
| 3577 | レーザーアーム | Laser Arm | 856 + 112 (18 bytes) |
| 3578 | メガレーザー | Mega Laser | 627 + 220 (20 bytes) |
| 3579 | ビームアーム | Beam Arm | 600 + 84 (16 bytes) |
| 3580 | ハイパービーム | Hyper Beam | 788 + 220 (20 bytes) |
| 3581 | ナイフアーム | Knife Arm | 920 + 380 (18 bytes) |
| 3582 | カギヅメ | Claw | inline |
| 3583 | りゅうのつめ | Dragon Claw | 553 + 54 (22 bytes) |
| 3584 | なげなわアーム | Lasso Arm | 948 + 354 (18 bytes) |
| 3585 | スリハンド | Pickpocket Hand | 797 + 412 (30 bytes) |
| 3586 | ぶんどりアーム | Plunder Arm | 676 + 114 (22 bytes) |
| 3587 | イカサマアーム | Cheat Arm | 953 + 354 (18 bytes) |
| 3588 | たんさアーム | Scan Arm | 603 + 52 (16 bytes) |
| 3589 | ふきや | Blowgun | 125 + 238 (14 bytes) |
| 3590 | だいごうきゅう | Great Bow | 973 + 484 (18 bytes) |
| 3591 | クロスボウ | Crossbow | 612 + 48 (16 bytes) |
| 3592 | タイレルアーム | Tyrell Arm | 813 + 784 (20 bytes) |
| 3593 | クラブアーム | Club Arm | 617 + 84 (16 bytes) |
| 3594 | メイスアーム | Mace Arm | 641 + 184 (16 bytes) |
| 3595 | フレイルアーム | Flail Arm | 981 + 878 (18 bytes) |
| 3596 | レッスルアーム | Wrestle Arm | 711 + 196 (22 bytes) |
| 3597 | バスターアーム | Buster Arm | 873 + 192 (20 bytes) |
| 3598 | パワーアーム | Power Arm | 1038 + 380 (18 bytes) |
| 3599 | ブレイドアーム | Blade Arm | 1066 + 354 (18 bytes) |
| 3600 | ケイブアーム | Cave Arm | 670 + 124 (16 bytes) |
| 3601 | カトックアーム | Katock Arm | 1147 + 226 (20 bytes) |
| 3602 | パイルバンカー | Pile Bunker | 718 + 210 (22 bytes) |
| 3603 | ハイパークロー | Hyper Claw | 1334 + 166 (20 bytes) |
| 3605 | ナーガハンド | Naga Hand | 1071 + 354 (18 bytes) |
| 3606 | デスハンド | Doom Hand | 1161 + 96 (18 bytes) |
| 3607 | スキュラハンド | Scylla Hand | 838 + 114 (22 bytes) |
| 3608 | グールハンド | Ghoul Hand | 1718 + 232 (20 bytes) |
| 3609 | ブラッドハンド | Blood Hand | 1752 + 274 (20 bytes) |
| 3610 | アシュラハンド | Ashura Hand | 875 + 362 (22 bytes) |
| 3611 | ヤシャハンド | Yasha Hand | 1890 + 232 (20 bytes) |
| 3612 | ジークハンド | Zeek Hand | 1254 + 76 (18 bytes) |
| 3613 | ワイズアーム | Wise Arm | 720 + 156 (16 bytes) |
| 3614 | スレッジハンド | Sledge Hand | 880 + 210 (22 bytes) |
| 3615 | ブレンアーム | Bren Arm | 761 + 84 (16 bytes) |
| 3616 | ケミカルハンド | Chemical Hand | 2054 + 502 (26 bytes) |
| 3617 | マジックアーム | Magic Arm | 1257 + 68 (18 bytes) |
| 3618 | ライトニング | Lightning | 1391 + 96 (18 bytes) |
| 3619 | ウィンアーム | Win Arm | 195 + 74 (14 bytes) |
| 3620 | シェルハンド | Shell Hand | 1940 + 274 (20 bytes) |
| 3621 | ロッポウアーム | Roppo Arm | 1484 + 76 (18 bytes) |
| 3622 | レジストアーム | Resist Arm | 2037 + 166 (20 bytes) |
| 3623 | サーブハンド | Serve Hand | 2104 + 80 (20 bytes) |
| 3624 | ラートルハンド | Rattle Hand | 887 + 186 (22 bytes) |
| 3625 | エリコルアーム | Erikol Arm | 2108 + 80 (20 bytes) |
| 3626 | プロペラ | Propeller | 1487 + 68 (18 bytes) |
| 3627 | ウイング | Wing | inline |
| 3628 | ジェット | Jet | inline |
| 3629 | ターボジェット | Turbo Jet | 1651 + 78 (18 bytes) |
| 3630 | グライダー | Glider | 5 + 162 (12 bytes) |
| 3631 | ブースター | Booster | 212 + 72 (14 bytes) |
| 3632 | カミカゼ | Kamikaze | 764 + 52 (16 bytes) |
| 3633 | きじゅう | Machine Gun | 908 + 152 (22 bytes) |
| 3634 | ソニック | Sonic | 12 + 152 (10 bytes) |
| 3635 | ばくだん | Bomb | inline |
| 3636 | アトミック | Atomic | 10 + 142 (12 bytes) |
| 3637 | スクリュー | Screw | inline |
| 3638 | ホバー | Hover | 19 + 128 (10 bytes) |
| 3639 | ソナー | Sonar | 67 + 80 (10 bytes) |
| 3640 | ウェーブ | Wave | inline |
| 3641 | ２０ミリほう | 20mm Cannon | 968 + 102 (22 bytes) |
| 3642 | ３６ミリほう | 36mm Cannon | 1005 + 186 (22 bytes) |
| 3643 | ４６ミリほう | 46mm Cannon | 1026 + 152 (22 bytes) |
| 3644 | ヘッジボム | Hedge Bomb | 2145 + 326 (20 bytes) |
| 3645 | バトルガンマー | Battle Gammar | 2126 + 570 (26 bytes) |
| 3646 | ぎょらい | Torpedo | 215 + 384 (14 bytes) |
| 3647 | きらい | Sea Mine | 768 + 284 (16 bytes) |
| 3648 | ローラー | Roller | 92 + 114 (12 bytes) |
| 3649 | ビッグローラー | Big Roller | 2222 + 166 (20 bytes) |
| 3650 | とげローラー | Spiked Roller | 2327 + 570 (26 bytes) |
| 3651 | キャタピラ | Caterpillar | 1103 + 102 (22 bytes) |
| 3652 | ヘルキャタピラ | Hell Caterpillar | 414 + 224 (32 bytes) |
| 3653 | マシンガン | Machine Gun | 1258 + 80 (22 bytes) |
| 3654 | ストロングほう | Strong Cannon | 2452 + 462 (26 bytes) |
| 3655 | キャノンほう | Cannon | inline |
| 3656 | バズーカー | Bazooka | 228 + 254 (14 bytes) |
| 3657 | マイン | Mine | 39 + 68 (8 bytes) |
| 3658 | きかんほう | Machine Cannon | 539 + 220 (28 bytes) |
| 3659 | ロケットほう | Rocket Cannon | 2472 + 366 (26 bytes) |
| 3660 | ミサイル | Missile | 346 + 384 (14 bytes) |
| 3661 | スパイクタイヤ | Spiked Tire | 1315 + 38 (22 bytes) |
| 3662 | ビッグフット | Bigfoot | 352 + 126 (14 bytes) |
| 3663 | ばくちく | Firecrackers | 690 + 82 (24 bytes) |
| 3664 | てなげだん | Hand Grenade | 713 + 360 (24 bytes) |

## New fuel warnings

Slash separates visible lines; double slash separates source pages.

| ID | English |
| --- | --- |
| 3665 | Mind your / Pearlton fuel / supply now. // No Pearlton / Ship stops! / GAME OVER! // Don't waste it! / Think before / using it, OK? |
| 3666 | Hey! Pearlton's / getting low! / Do something! // I told you: / Don't waste your / Pearlton! // Use it wisely. / GAME OVER means / no more trip! |
| 3667 | Hey! Pearlton / is nearly gone! / I warned you // You always / waste it! // No Pearlton / Ship stops! / GAME OVER! // Worst case, sell / bots to a dealer / for Pearlton! |
| 3668 | Ah... Dark. / Hopeless... / No way out. // That means / GAME OVER... / Bye, bye, bye! |
| 3669 | Mind the / Pearlton / left, please. // Fuel gone / Ship stops / GAME OVER // Take care. / Use it wisely / Understood? |
| 3670 | Excuse me! / Pearlton / is in danger! // Think calmly. / GAME OVER would / spoil our trip. // Use it wisely. / Is that clear? / Understood? |
| 3671 | Pearlton / is very low! / What now...? // No fuel left / Ship stops! / GAME OVER! // Worst case, sell / bots to a dealer / for Pearlton. |
| 3672 | Pitch dark / Nothing can / be done now. // It's GAME OVER / Sorry to part / We can't go on |
