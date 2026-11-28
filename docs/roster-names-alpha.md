# Roster names alpha

This cumulative partial English draft adds **94 native records**: the remaining
Dome lower-rank refusal 2719 and all **93 native roster/speaker labels 2808–2900**.
Coverage reaches **3,011 native records, 832 UI strings, 299 choice blocks and
three bitmap captions**. All preceding 2,917 catalog entries are identical.

Dome 2719 says the player must clear the lower rank first, climb rank by rank,
and return. It keeps all source portraits, lines and pages. The 93 labels include
49 Robopon/default names and 44 character/role labels. Names follow existing
battle/glossary spellings where available and remain provisional. Native Porthos
versus story Dartagnan, and native Anio versus story Aniro, preserve their source
differences. Saved nicknames are separate and are not rewritten.

## Full names within the existing text pool

Japanese glyph allocations are too short for many English names: native Merlin
has four cells and Captain Ladder nine. Seven short English labels fit in place.
The other **86 labels borrow unused trailing padding from 14 already-translated
records**. No ROM/text-pool expansion or game-engine patch is used.

Each relocated label declares storage.record_id and storage.byte_offset. The
builder first verifies and encodes all source records. It permits plain ASCII
labels of at most 16 cells to occupy an aligned range wholly after the donor's
active text and within its original allocation. It updates the label descriptor's
byte count and pool-relative pointer. The original label bytes remain in place.
All 2,917 preceding descriptors and active text bytes match the previous ROM;
only selected unused donor tails change. Donor text is length-delimited, so the
stored names lie outside its declared text. The native-reader preview below
exercises the new pointers and full lengths.

Guards reject untranslated/missing/relocated donors, malformed storage, odd
positions, live-text overlap, donor overflow, overlapping labels, control-bearing
labels and overlong/non-ASCII text. A donor that later grows into a name causes
a build failure. Existing global overlap, source metadata, original hash and
checksum guards remain. Source offsets in the catalog stay immutable even when
the final descriptor points elsewhere. Future allocations must account for
these 86 occupied ranges; deliberately repack names when changing donors.

Nine new storage tests cover pointer/count correctness, original name and donor
preservation, catalog order, multiple names, guard failures and a later donor
translation growing into a label. Two width tests reserve **eleven cells** for
bot-name command 200B:0007, covering Mochimocchi, the longest translated default
bot name. Existing 2709 still fits. Player-name argument 0 remains five cells;
dynamic-item argument 6 retains its full-line rule. Native storage is independent
of the entered-name field and saved nickname bytes.

| Donor ID | Active bytes | Used tail end | Original allocation |
| --- | --- | --- | --- |
| 2376 | 788 | 908 | 908 |
| 2522 | 788 | 908 | 908 |
| 2481 | 1704 | 1808 | 1808 |
| 2627 | 1704 | 1804 | 1808 |
| 891 | 394 | 486 | 486 |
| 1009 | 394 | 484 | 486 |
| 2597 | 120 | 200 | 200 |
| 2615 | 120 | 196 | 200 |
| 898 | 252 | 324 | 324 |
| 1016 | 252 | 320 | 324 |
| 2732 | 624 | 684 | 690 |
| 2736 | 622 | 678 | 688 |
| 2738 | 624 | 686 | 688 |
| 2728 | 198 | 216 | 260 |

## Runtime evidence and limits

The final ROM cold-boots and loads native file A with day 2, 500G, the player
name and Merlin intact. The file prompt, wake text and pause display were
inspected with Mupen64Plus/Glide64mk2. The immutable EEPROM contains Merlin's
Japanese Shift-JIS nickname at byte offset 340, explaining the unchanged name
in the file and bot menus. This patch does not rename an existing saved bot.
No in-game save was attempted; reference, default and isolated EEPROM hashes
remain unchanged. No savestate was loaded or created.

A **separate test-only preview ROM** copies the final-ROM Merlin, Dr. Mighty and
Captain Ladder descriptors into the 66 opening-caption slots, cycling the names.
It changes only those descriptor ranges; the actual label glyphs and their
borrowed storage pointers are identical to the final ROM. A cold boot with an
empty isolated save folder starts the opening book. The screenshot shows all
three full names rendered correctly, including the 14-cell Captain Ladder.
This demonstrates the native reader's pointer and length handling, not every
roster UI or every donor dialogue scene.

Final ROM MD5: `F386293C419701AD5901D2394AF58BF1`.
Preview MD5: `C6A747C8EF1C07C125E451B5A00BDC8E`.
The preview is reproduced by applying local evidence preview.bps to the final
ROM, rather than to the Japanese original. Its identity lists every copied
descriptor. Both completed logs and screenshots, preview BPS and identity/hashes
are in `local/roster-names-evidence/`. The preview ROM and its empty/new-game
save data are not release assets. Neither run uses a historical savestate.

The Dome refusal, remaining roster contexts, donor scenes and earlier regional
scenes/anchored pages still need gameplay testing. Custom-name behavior and all
late-game label layouts are not claimed validated. Five earlier page exceptions
are unchanged. No new page exceptions or cut/portrait exclusions were needed.

## Build and recovery

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/roster-names-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/roster-names-alpha.z64 --patch local/roster-names-alpha.bps
```

Apply releases/roster-names-alpha.bps directly to the exact Japanese original;
do not stack release patches. The 32 MiB target and patch hashes are in the
release manifest. CIC-6102 CRC1/CRC2 remain `FFA89600 C278C65F`. The builder also
reproduces the preceding Sunny Blue variants ROM without a byte change.

All **128 tests** pass in the source checkout and after clean restoration.
Floating IPS independently reproduces the final ROM from the BPS; read-only
chksum64 agrees with the header. Verification checks all original entries,
active bytes/descriptors, new name bytes/counts/pointers, donor bounds, source
name preservation, 17 existing UI spellings and the exact new ID set.

The AES-256 backup decrypts byte-for-byte to its ZIP. Clean restoration verifies
all **743 payload files**, the source revision, final ROM/BPS/save checks,
executable modes, emulator library symlink, exact-ROM EEPROM profile and evidence
hashes. The preview is independently reconstructed and checked against its
identity and descriptor-copy ranges. The existing passphrase stays outside Git.
See backups/README.md and RESTORE.md.

Continue bedtime dialogue 2901–2930, food labels 2931–2973 and bot interactions.
Preserve the explicit storage ranges when adding text or revising donors.

## Native label spellings

These are provisional project spellings, not a claim of official localization.

| ID | Japanese | English | Storage |
| --- | --- | --- | --- |
| 2808 | ロボまる | Robomaru | 2376 + 788 |
| 2809 | ドリリアン | Drillian | 2376 + 804 |
| 2810 | デンチャン | Denchan | 2376 + 820 |
| 2811 | メガロ | Megalo | 2376 + 834 |
| 2812 | ブッピー | Buppy | 2376 + 846 |
| 2813 | ギャルル | Gyaruru | 2376 + 856 |
| 2814 | ヒトミ | Hitomi | 2376 + 870 |
| 2815 | ムサシ | Musashi | 2376 + 882 |
| 2816 | コジロウ | Kojiro | 2376 + 896 |
| 2817 | アーメフト | Ameft | In place |
| 2818 | カイゾーグ | Kaizorg | 2522 + 788 |
| 2819 | ハオウ | Haoh | 2522 + 802 |
| 2820 | ドクロイド | Dokuroyd | 2522 + 810 |
| 2821 | ナース | Nurse | 2522 + 826 |
| 2822 | デビアン | Devian | 2522 + 836 |
| 2823 | オヤカタ | Oyakata | 2522 + 848 |
| 2824 | キュラ | Kyura | 2522 + 862 |
| 2825 | ボイラース | Boilars | 2522 + 872 |
| 2826 | テッキュー | Tekkyu | 2522 + 886 |
| 2827 | カプカプ | Kapukapu | 2481 + 1704 |
| 2828 | タンイチ | Tanichi | 2481 + 1720 |
| 2829 | マーシャル | Marshal | 2481 + 1734 |
| 2830 | ヌーハーフ | Nuhalf | 2481 + 1748 |
| 2831 | ベンザー | Benzer | 2481 + 1760 |
| 2832 | ドライバル | Drival | 2481 + 1772 |
| 2833 | ホッケイ | Hockey | 2481 + 1784 |
| 2834 | シルバーン | Silvern | 2627 + 1704 |
| 2835 | ゴールドン | Goldon | 2481 + 1796 |
| 2836 | モチモッチ | Mochimocchi | 2627 + 1718 |
| 2837 | ピッチ | Pitch | 2522 + 898 |
| 2838 | ドルッピ | Doluppi | 2627 + 1740 |
| 2839 | クージラン | Kujiran | 2627 + 1754 |
| 2840 | ウーマンボ | U-Manbo | 2627 + 1768 |
| 2841 | ギョジン | Gyojin | 2627 + 1782 |
| 2842 | フライヤー | Flyer | In place |
| 2843 | グラジ | Glaji | 2627 + 1794 |
| 2844 | メスカル | Mescal | 891 + 394 |
| 2845 | ザリガ | Zariga | 891 + 406 |
| 2846 | ザリーグ | Zarigue | 891 + 418 |
| 2847 | シフォン | Chiffon | 891 + 432 |
| 2848 | ロッポニカ | Ropponica | 891 + 446 |
| 2849 | メルリン | Merlin | 891 + 464 |
| 2850 | メルリアス | Merlias | 1009 + 394 |
| 2851 | ミクロ | Micro | 891 + 476 |
| 2852 | マクロ | Macro | 1009 + 408 |
| 2853 | ニークロ | Nikuro | 1009 + 418 |
| 2854 | タンビ | Tanbi | 1009 + 430 |
| 2855 | ピパ | Pipa | 1009 + 440 |
| 2856 | カラメル | Caramel | 1009 + 448 |
| 2857 | グリア | Gria | 1009 + 462 |
| 2858 | パーム | Palm | 1009 + 470 |
| 2859 | パンチ | Punch | 2597 + 120 |
| 2860 | ラム | Ram | 1009 + 478 |
| 2861 | ダンディはかせ | Dr. Dandy | 2597 + 130 |
| 2862 | マイティはかせ | Dr. Mighty | 2597 + 148 |
| 2863 | ミカチ | Mikachi | 2597 + 168 |
| 2864 | アトス | Athos | 2597 + 182 |
| 2865 | ポルトス | Porthos | 2615 + 120 |
| 2866 | アラミス | Aramis | 2615 + 134 |
| 2867 | かいしゅうや | Collector | 2615 + 146 |
| 2868 | いっぱんじん | Civilian | 2615 + 164 |
| 2869 | ドクターゼロ | Dr. Zero | 2615 + 180 |
| 2870 | コロン | Koron | 898 + 252 |
| 2871 | プーすけ | Pusuke | 898 + 262 |
| 2872 | エーやん | E-yan | 898 + 274 |
| 2873 | シャロル | Sharol | 898 + 284 |
| 2874 | ディーン | Dean | In place |
| 2875 | ゴドシー | Godoshii | 898 + 296 |
| 2876 | ジョニー | Johnny | 898 + 312 |
| 2877 | ガーリマン | Gariman | 1016 + 252 |
| 2878 | ヘンペー | Henpei | 1016 + 266 |
| 2879 | マーク | Mark | 2597 + 192 |
| 2880 | コムーラ | Komura | 1016 + 278 |
| 2881 | ドンゴー | Dongo | 1016 + 290 |
| 2882 | ムーラ | Mura | 1016 + 300 |
| 2883 | アニオウ | Anio | In place |
| 2884 | オバーン | Oban | In place |
| 2885 | Ｒ３−Ｋ | R-3K | In place |
| 2886 | クルミ | Kurumi | 1016 + 308 |
| 2887 | メカオ | Mekao | 2732 + 624 |
| 2888 | Ｊ・Ｄ | J.D. | 2732 + 634 |
| 2889 | ドン・オヤージ | Don Oyaji | 2732 + 642 |
| 2890 | キャム | Cam | In place |
| 2891 | コロン | Koron | 2732 + 660 |
| 2892 | ダイコック | Daicook | 2732 + 670 |
| 2893 | カイリ | Kairi | 2736 + 622 |
| 2894 | キャプテン・ラダー | Captain Ladder | 2736 + 632 |
| 2895 | フーろうし | Master Fu | 2736 + 660 |
| 2896 | パオ・タイ | Pao Tai | 2738 + 624 |
| 2897 | キョン・キョンシー | Kyonkyonshi | 2738 + 638 |
| 2898 | ライゲン | Raigen | 2738 + 660 |
| 2899 | ロン・チュー | Ron Chu | 2738 + 672 |
| 2900 | リー・リンリン | Li Linlin | 2728 + 198 |
