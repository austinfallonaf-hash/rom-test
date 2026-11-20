# Bot food alpha

This cumulative partial English draft adds **72 native records**: 30 bot bedtime
lines (2901–2930) and 42 food labels (2931–2973, excluding existing Berry 2954).
Coverage reaches **3,083 native records, 832 UI strings, 299 choice blocks and
three bitmap captions**. All preceding 3,011 catalog entries are identical.

## Voices and food wording

Bedtime lines retain fifteen pairs of different voices: weary workers, the boss
address, reluctance to keep working, pomyu/zari/mel/Osu quirks, duty reporting,
requests for a story, questions about wandering, tomorrow's plans, searching for
a bed and Caramel's moshi/folksy voice. Short English is constrained by each
original allocation. All source portraits, line/page commands and arguments stay
in their original order. The bot-name insertion 200B:0007 in 2915 is unchanged;
its eleven-cell reservation plus the ellipsis fits the line.

Food labels retain noodle/drink/curry/cake/fish/fruit and miscellaneous names.
Kitsune Ramen uses the fried-tofu noodle term; 18 Tea keeps the source's number.
Kuppy, Tropical Eye and Coelazance remain provisional food/fish wordplay, rather
than claims of official names. Fin-O-Fish retains the source fin/fillet joke.
B&W Cookie abbreviates black and white. Tsukimi Sandwich retains the egg/moon-
viewing name. The previous compact Berry label for strawberry mousse is identical.
Item IDs, quantities, food effects, recipes and inventory are not changed.

## Storage and guards

The earlier 86 roster placements remain byte-for-byte identical. New labels use
free intervals derived from each translated donor's unused tail **after
subtracting every existing stored-label range**. There are 41 new food storage
placements and one new in-place label, 18 Tea. The total is 127 disjoint stored
labels in 36 donors. All preceding active text, label data and descriptors match
the prior ROM. Only unclaimed padding and the new labels' descriptors change.

The existing builder checks aligned tail bounds, live-text/sibling overlap,
source metadata, original hash, ASCII and 16-cell label limits. Donor growth into
any occupied label fails until the names are deliberately repacked. Dialogue
keeps its original allocation and strict control stream. No codec, engine,
text-pool size, new page exceptions or extra newline opt-ins were needed.

## Runtime evidence and limits

The exact final ROM cold-boots and loads file A with day 2, 500G, player name and
Merlin intact. File, wake, pause and the existing inventory label were inspected
using Mupen64Plus/Glide64mk2. The saved Japanese Merlin nickname is preserved.
The reference/default/isolated EEPROM copies remain identical; no in-game save
was attempted and no savestate was loaded or created.

The reference save's Food category is unavailable. A separate inventory-label
preview therefore copies only the descriptor of Extra Spicy Soba (2936) into
the existing Ashura label slot (3891). The actual food glyph bytes and borrowed
storage pointer are identical to the final ROM. Loading a separate reference-save
copy and viewing the Item category exercises the shared inventory label field
with a 16-cell food name. This is a test fixture, not a release change to the
Ashura item or its ID/effects/quantity. It does not test every Food-category flow.

Final MD5: `DE539AABBFC65CC723259DFD629B4A97`.
Preview MD5: `00C207636A8D82F4D72439DA98A9DF2E`.
The evidence folder `local/bot-food-evidence/` includes completed logs, final-ROM
screenshots, the preview screenshot, preview BPS and exact descriptor-copy
identity/hashes. Apply the preview BPS to the final bot-food ROM, not the Japanese
original. Use a separate copy of the reference EEPROM with the preview's MD5
filename. Neither run uses a savestate from another ROM.

Actual bedtime triggers, remaining food contexts, custom names, older donor and
regional scenes, five page exceptions, Parts frame and VS/Transfer Pak branches
still need gameplay checks. The final release keeps Berry and the existing
inventory unchanged.

## Build and recovery

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/bot-food-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/bot-food-alpha.z64 --patch local/bot-food-alpha.bps
```

Apply releases/bot-food-alpha.bps directly to the exact Japanese original;
do not stack release patches. The 32 MiB target and patch hashes are recorded in
the manifest. CIC-6102 CRC1/CRC2 remain `FFA89600 C278C65F`.

All **128 tests** pass in the source checkout and after clean restoration.
Floating IPS independently reproduces the ROM from the BPS; read-only chksum64
agrees with the header. Verification checks the exact new IDs, all 3,011 prior
entries/active bytes/descriptors, all 127 occupied storage ranges and every new
label/control stream. Original relocated source slots and Berry remain intact.

The AES-256 archive decrypts byte-for-byte to its ZIP. Clean restoration verifies
all **765 payload files**, source revision, ROM/BPS/save/evidence hashes, executable
modes, emulator library symlink and exact-ROM 16Kbit EEPROM profile. The preview
is independently reconstructed and checked for its sole descriptor change.
The recovery passphrase stays outside Git. See backups/README.md and RESTORE.md.

Continue bot interaction text at record 2974, preserving occupied storage.

## Food labels

| ID | Japanese | English | Storage |
| --- | --- | --- | --- |
| 2931 | きつねラーメン | Kitsune Ramen | 233 + 238 |
| 2932 | ミソうどん | Miso Udon | 233 + 264 |
| 2933 | ワンタンめん | Wonton Noodles | 2720 + 622 |
| 2934 | たちぐいそば | Standing Soba | 2720 + 650 |
| 2935 | うどんラーメン | Udon Ramen | 2740 + 626 |
| 2936 | ゲキからソバ | Extra Spicy Soba | 2740 + 646 |
| 2937 | オイルソーダ | Oil Soda | 233 + 282 |
| 2938 | おとなのコーヒー | Adult Coffee | 2670 + 596 |
| 2939 | ハーブティー | Herbal Tea | 2670 + 620 |
| 2940 | ジュウハチちゃ | 18 Tea | In place |
| 2941 | みそしるドリンク | Miso Soup Drink | 2742 + 632 |
| 2942 | こどものココア | Kids' Cocoa | 2742 + 662 |
| 2943 | インドカレー | Indian Curry | 2451 + 376 |
| 2944 | ゲキあまカレー | Very Sweet Curry | 822 + 464 |
| 2945 | ハヤシライス | Hayashi Rice | 2451 + 400 |
| 2946 | ポンカレー | Pon Curry | 822 + 496 |
| 2947 | くさいカレー | Stinky Curry | 2734 + 634 |
| 2948 | モンゴルカレー | Mongolian Curry | 646 + 466 |
| 2949 | クリームケーキ | Cream Cake | 2734 + 658 |
| 2950 | くりくりケーキ | Chestnut Cake | 2469 + 386 |
| 2951 | フルーツトルテ | Fruit Torte | 2469 + 412 |
| 2952 | ナポレオンパイ | Napoleon Pie | 2663 + 562 |
| 2953 | ダイエットケーキ | Diet Cake | 646 + 496 |
| 2955 | トロピカルアイ | Tropical Eye | 2663 + 586 |
| 2956 | クッピー | Kuppy | 2670 + 640 |
| 2957 | ひれおフィッシュ | Fin-O-Fish | 2722 + 426 |
| 2958 | あきざかな | Autumn Fish | 2722 + 446 |
| 2959 | くさいさかな | Stinky Fish | 2728 + 216 |
| 2960 | シーラザンス | Coelazance | 2728 + 238 |
| 2961 | レッドチェリー | Red Cherry | 2733 + 220 |
| 2962 | グリーンチェリー | Green Cherry | 2733 + 240 |
| 2963 | ブルーチェリー | Blue Cherry | 2739 + 220 |
| 2964 | イエローチェリー | Yellow Cherry | 563 + 374 |
| 2965 | アップル | Apple | 2739 + 242 |
| 2966 | でんちアメ | Battery Candy | 636 + 400 |
| 2967 | シロクロクッキー | B&W Cookie | 724 + 374 |
| 2968 | カラフルクッキー | Colorful Cookie | 2735 + 222 |
| 2969 | おいしいニク | Tasty Meat | 724 + 394 |
| 2970 | ばくだんチョコ | Bomb Chocolate | 2737 + 220 |
| 2971 | チャンコなべ | Chanko Hotpot | 2741 + 220 |
| 2972 | ぼんぼんランチ | Bonbon Lunch | 222 + 226 |
| 2973 | つきみサンド | Tsukimi Sandwich | 1907 + 278 |

Record 2954 remains Berry, exactly as in the preceding catalog.
