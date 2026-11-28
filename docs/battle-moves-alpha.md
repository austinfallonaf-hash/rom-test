# Battle moves alpha

This cumulative draft adds 412 UI strings and 44 native app labels to battle-hud-alpha.
Totals: 323 native records, 832 UI strings and 299 native choice blocks. The
previous catalogs remain unchanged within these cumulative files. This is a
partial translation; graphical command/stat headings and later story remain.

## New coverage

The complete verified battle-name pool at `0xC7FA0..0xC899B` now has 244 English
components. This milestone supplies the remaining 161: elemental combinations,
orb spells, summons, defenses, special effects and the longer standalone moves.
The existing four Alpha/Omega names and 79 shared components are retained.
A separate 244-string copy used by equipment screens is translated with the
same names, giving 488 translated strings across the two pools.

All 45 basic app names now have compact native-font labels (Fire was already
translated). Most native allocations allow only two to four glyphs, so labels
such as `Thnd`, `Shld` and `Drgn` are abbreviations. The battle HUD uses fuller
names. Specialized names and transliterations remain provisional. Some prefixes
use their entire byte allocation and leave no room for a separating space.

Power/EP values and empty-value placeholders, the Full inventory marker,
the equipped-app removal refusal and the remove-all/re-equip question are also
translated. Existing printf/color controls and their order are retained.

## Name composition guard

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/battle-moves-text.json \
  --choices translation/story-choices.json --layout translation/battle-moves-layout.json \
  --update-checksum --validate-moves \
  --output local/battle-moves-alpha.z64 --patch local/battle-moves-alpha.bps
python -m tools.move_names local/original.z64 --catalog translation/battle-moves-menu.json --equipment
```

Apply `releases/battle-moves-alpha.bps` only to the exact Japanese original.
Do not stack patches. The final ROM MD5 is `79D7C6D9FC8B8DB1F04A3E9AFDD81240`.

`tools.move_names` reads 196 eight-byte app recipes at `0xC6820`, 128 two-byte
part-name descriptors at `0xC6E40`, and 48 suffix pointers at `0xC6F40`. The
loaded overlay maps these pointers with bias `0x8001FDA0`. The original name
assembler at `0xC3278..0xC3443` uses a recipe flag to choose a standalone name,
or combines the recipe and part components in the order specified by the part.

The guard checks every recipe against every part descriptor: 25,088 combinations,
with a maximum of sixteen cells. The equipment copy is checked independently
against its own recipes (`0x21D298`), part descriptors (`0x21D8B8`) and suffix
pointers (`0x21D9B8`), with overlay bias `0x7FEAE060`. Both sets must agree;
50,176 recipe/part combinations are checked across the two pools. This deliberately checks a broad set of names;
it does not establish that every pairing is reachable with normal app/RAM rules.
Missing translations, changed source strings, invalid pointers/metadata and
oversized combinations fail validation. The existing battle layout, checksum
repair, exact-source/width/budget guards and isolated emulator profile are retained.

All 101 tests pass. The new tests cover component order, standalone names,
combined width, incomplete translations and malformed table references. chksum64
independently agrees with CRC1/CRC2, and Floating IPS independently applies the
BPS to reproduce the final ROM. See the release manifest for hashes.

The equipment screen displays move names in two columns at native x=52 and
x=172. Its draw-call horizontal scale at `0x219AD0` changes from 1.0 to 0.5,
retaining the vertical scale and column positions. This gives sixteen Latin
cells room inside each column. The previous seventy guarded layout words are
retained, for seventy-one in the current catalog.

## Runtime coverage

The exact final ROM cold-booted with an isolated copy of the preserved native
EEPROM. File A retained day 2, 500G, the entered player name and Merlin. The
Apps/Set equipment screen showed Attack and Fire Charm in separate columns,
with room before the frame edges. Removing Fire transferred it to inventory and
reduced the move list to Attack; re-equipping restored Fire Charm. The Apps/Del
inventory showed Fire v1 with PWR 10, EP 3 and RAM 10M. The test did not delete it. The same final ROM then entered a simulator
practice battle with the normal HUD displayed.

Evidence is under `local/battle-moves-evidence/`. The equipment exploration state
belongs to this exact ROM and cannot validate later builds. No older-build
emulator state was loaded. Most app/move combinations, empty stat placeholders,
capacity/removal warnings and later result variants remain build-validated only.
Earlier runtime coverage is documented in [battle HUD notes](battle-hud-alpha.md)
and [simulator/gardening notes](simulator-alpha.md).

## Compact native app labels

The orb codes use F=Fire, W=Water, I=Ice, E=Electric, A=Wind, G=Earth, D=Dark,
H=Holy, L=Land, S=Sea and K=Sky. `SD` means self-destruct. Two-glyph element
abbreviations and other shortened labels below reflect the existing allocations.

| App ID | Japanese source | Native label | Battle component |
| --- | --- | --- | --- |
| 1 | ファイア | Fire | Fire |
| 2 | アクア | Aqa | Aqua |
| 3 | アイス | Ice | Ice |
| 4 | サンダー | Thnd | Thunder |
| 5 | ウィンド | Wind | Wind |
| 6 | グランド | Grnd | Ground |
| 7 | じゃ | Ev | Evil |
| 8 | シャドー | Shdw | Shadow |
| 9 | せい | Ho | Holy |
| 10 | ライト | Lgt | Light |
| 11 | キッス | Kis | Kiss |
| 12 | りく | Ld | Land |
| 13 | ガス | Gs | Gas |
| 14 | うみ | Se | Sea |
| 15 | そら | Sk | Sky |
| 16 | ドラゴン | Drgn | Dragon |
| 17 | パワー | Pwr | Power |
| 18 | すいとり | Dran | Drain |
| 19 | オイル | Oil | Oil |
| 20 | ウイルス | Virs | Virus |
| 21 | がまん | End | Endure |
| 22 | スコープ | Scop | Scope |
| 23 | スピード | Spd | Speed |
| 24 | シールド | Shld | Shield |
| 25 | アタック | Atk | Attack |
| 26 | オメガ | Omg | Omega |
| 27 | うけみ | Rol | Roll |
| 28 | はんげき | Cntr | Counter |
| 29 | アルファ | Alph | Alpha |
| 30 | パルス | Pls | Pulse |
| 31 | ダウン | Dwn | Down |
| 32 | ひだま | FOr | F-Orb |
| 33 | みずだま | WOrb | W-Orb |
| 34 | れいだま | IOrb | I-Orb |
| 35 | らいだま | EOrb | E-Orb |
| 36 | かぜだま | AOrb | A-Orb |
| 37 | つちだま | GOrb | G-Orb |
| 38 | じゃだま | DOrb | D-Orb |
| 39 | せいだま | HOrb | H-Orb |
| 40 | りくだま | LOrb | L-Orb |
| 41 | うみだま | SOrb | S-Orb |
| 42 | そらだま | KOrb | K-Orb |
| 43 | きあい | Chi | Focus |
| 44 | いのり | Pry | Prayer |
| 45 | じばく | SD | Boom |
