# Gold Blue story alpha

This cumulative partial English draft adds **166 native records**, reaching
**2,072 native records, 832 UI strings, 299 choice blocks and three bitmap
captions**. All preceding 1,906 entries are identical. The main Gold Blue story
now has a draft; the alternate bank begins at record 1784.

| Records | Added coverage |
| --- | --- |
| 1609–1639 | Fu's Pao Tai trial, initial and repeat challenges, decline/loss/win reactions: 31 records |
| 1640–1711 | Kyonkyonshi, the silent muscular fighter and drunken elder, rematches and empty-island messages: 72 records |
| 1712–1734 except 1726–1728 | Linlin, Gold Caramela reward, Mt. Despera/Land Blue warning and thaw/departure: 20 records |
| 1735–1763 except seven cut messages | Ho's school history, Linlin's expulsion/invasion, frozen-sea explanation and trial referral: 22 records |
| 1764–1783 | Black Musketeer collision, frozen arrival and repeated departure: 20 records |
| 3677 | Nine-cell inventory label: Gold |

Ten cut-message placeholders remain byte-for-byte unchanged, including their
complete descriptors: 1726, 1727, 1728, 1736, 1738, 1747, 1748, 1749, 1750 and
1757. They are excluded from the translation count. There are no new control-only
exclusions in this bank. Earlier cut/portrait-only exclusions remain unchanged.

## Wording and source details

Ho and Fu are twins; Fu is the elder and tests the player through his pupil Pao
Tai. The martial-arts triad しん・ぎ・たい is mind, skill and body, compacted to
mind/skill/body in dialogue. Loss, declined challenges, balanced victory and
repeat-training reactions remain distinct. Caramel is the legendary Robopon;
Caramela names the treasures.

Kyonkyonshi retains the talisman, stutter and hohi laughter. The muscular fighter's
silence, comparisons with Nikuniku and boast/joke remain. The drunken elder keeps
his belches, fart, forgetfulness, drink-related defeat excuse and confused
tomorrow/date joke. His expression changes are retained in the variants.

Li Linlin shortens to Linlin as in the source. She was expelled roughly five years
ago, formed an army and returned a year ago. She values might alone and rejects
the triad; the professor argues that the player's victories restore peace.
The player has four fragments, Linlin has one, and she expects five if she wins.
Her opportunistic Chinese-proverb reference, revenge vow and departure remain.

Gold Caramela reflects its owner's heart. Linlin is unworthy, and her acquisition
freezes Gold Blue; her defeat frees it. The pinball-like machinery is explained
as transport across the ice. The reward uses **Gold** where crowded, including
the inventory label and acquisition message. **Mt. Despera** abbreviates Despera
Mountain. The next sea is Land Blue, with a warning that the Musketeers may steal
the collected Caramela. The collision uses the established compact Black Trio.
All names remain provisional; native roster/speaker labels remain Japanese.

Every new portrait, expression, color, page, line and player-name command retains
its exact arguments and order, including source color choices. English fits the
original allocations, 16 cells per line and three nonempty lines per page.
Player-name substitutions reserve five cells. No new layout exception, codec
change or record relocation was needed. Record 831's inherited page exception
is unchanged. Story events, battle conditions, rewards and transfers are unchanged.

## Build and verification

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/gold-blue-story-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/gold-blue-story-alpha.z64 --patch local/gold-blue-story-alpha.bps
```

Apply `releases/gold-blue-story-alpha.bps` directly to the exact Japanese original;
do not stack patches. The target remains 32 MiB, MD5
`166993B3B9BE78CB74831F8DD821718F`. The release manifest records source, target
and patch hashes. CIC-6102 CRC1/CRC2 remain `FFA89600 C278C65F`.

All 115 existing tests pass. The builder checks exact source bytes, descriptors,
controls, widths, allocations and overlapping edits. Floating IPS independently
reproduces the final ROM from the BPS. Read-only chksum64 agrees with its header.
All preceding entries compare equal, and the ten cut-message records' complete
descriptors and payloads match the original. Original ROM and reference EEPROM
remain intact.

## Runtime and recovery

The exact final ROM cold-boots from an isolated native EEPROM copy. File A retains
day 2, 500G, the entered player name and Merlin. Native file selection, English
Start/Delete options, ship wake and pause rendering were inspected with the supplied
Mupen64Plus/Glide64mk2. No savestate was loaded or created; no in-game save was
attempted. Original ROM and reference/default/isolated EEPROM hashes are unchanged.
The exact-ROM profile retains 16Kbit EEPROM, two players and Transfer Pak metadata.
Screenshots, completed log and file hashes are in `local/gold-blue-story-evidence/`.

The new Gold Blue scenes and inventory label were not reached in playthrough.
Training, fighters, Linlin, reward/thaw, arrival/pinball transport, collision and
departure have build validation only. Earlier Roulette and Water/Fire Blue scenes
still await playthrough. Historical states retain their original ROM identities
and were not used for current validation.

The AES-256 recovery archive decrypts byte-for-byte to its ZIP. A clean restore
verifies all 619 payload files and passes all 115 tests, including ROM/BPS/save
checks, executable modes, the emulator library symlink and exact-ROM profile.
The manifest records the archived source revision. The passphrase stays outside
Git; earlier ROMs rebuild from their cumulative patches. See `backups/README.md`.

## Next work

Continue the alternate Gold Blue bank at record 1784, regional hints and
arrival/collision variants through 1971, then Land Blue at 1972. Play the training
trial, all three fighters, Linlin, reward/thaw, arrival/pinball transport and
collision/departure scenes. Both Roulette routes and earlier Water/Fire Blue
branches still need playthrough checks. Graphical/roster labels, the Parts frame,
capacity warnings and VS/Transfer Pak branches remain. Preserve the Dome
three-versus-four-win discrepancy and check record 831's inherited page split.
