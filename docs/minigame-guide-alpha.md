# Minigame guide alpha

This cumulative partial English draft adds **22 native records** (3320–3341):
three labels, fifteen fixed-grid instructions/control guides and four pest-control
messages. Coverage reaches **3,451 native records, 832 UI strings, 299 choices
and three bitmap captions**. All preceding 3,429 catalog entries are identical.

## Fixed-grid reader

These records are not dialogue paragraphs. The native readers load the record,
copy successive fixed-size rows into a temporary buffer and draw each row:

| IDs | Rows x glyphs | Record bytes | Reader evidence (ROM) |
| --- | --- | --- | --- |
| 3323–3327 | 7 x 10 | 140 | 0x12242C loop 7; 0x122480 copy 20 bytes |
| 3328,3330,3332,3334,3336 | 3 x 21 | 126 | 0x1725C4 loop 3; 0x172620 copy 42 bytes |
| 3329,3331,3333,3335,3337 | 3 x 15 | 90 | 0x1726E8 loop 3; 0x17273C copy 30 bytes |

The row-stride calculations match the copied sizes. The native getter is called
before each loop; the 21- and 15-glyph records are selected in pairs. Evidence
includes exact source instruction words and unchanged reader excerpts. All six
training-guide reader pairs have identical guarded base IDs, loop bounds and copy
lengths (0x1725A4, 0x17AE98, 0x183E3C, 0x18C4C0, 0x19C33C and 0x1A2DA4).

The new fixed_grid catalog kind uses newline-separated ASCII rows. The encoder
permits only these fifteen IDs, requires exact source dimensions without control
words, checks the row count/width and printable ASCII, and pads each row with
blank native glyphs. It writes the full original byte count. All fifteen grid
descriptors, including pool pointers, remain byte-for-byte original. The newline
separators are not encoded as 2000 commands. Dialogue and label limits stay
unchanged; this is not a general long-text bypass or an engine patch.

Six new tests check all verified shapes and row offsets, full-size padding,
unknown IDs, wrong dimensions/source controls, row count/overflow, ASCII and
builder integration, source guards and forbidden storage. The suite totals 134.

## Wording and labels

The five tournament briefs retain rubber pulling/power gauge, jumping blocks for
orbs, protecting the ship from missiles with A, pushing objects with the stick
and A/B for a three-point speed bonus, and boat racing with sharks/whirlpools.
The five training descriptions retain quotas, damage, sinking prevention, dash
and over-mashing fatigue. Control rows remain in A/B/stick order; unused controls
are explicitly marked. Button icons and game behavior are untouched.

Knuckle, Hammer and Punch retain full names using three new aligned free ranges
after subtracting all earlier occupied storage. There are now 130 stored labels
in the same 36 donors. All previous active bytes and descriptors are unchanged.
The three original source label slots remain Japanese and intact; only their
descriptors point to the new English bytes. No pool/ROM expansion is used.

| Label | Storage donor + byte offset |
| --- | --- |
| Knuckle (3320) | 222 + 250 |
| Hammer (3321) | 563 + 400 |
| Punch (3322) | 636 + 426 |

Pest-control text distinguishes protected runners from runners eaten by rat bots.
Both cleaning warnings retain the infestation and total-loss warning, with the
elder's sharper caution and the other version's conditional warning. Runner
follows existing gardening UI terminology. All four original dialogue control
streams, pages and byte budgets are exact; there are no new layout exceptions.
Saved nicknames, Berry, item IDs/effects, task results and events are unchanged.

## Validation and limits

The exact final ROM cold-boots and loads file A with day 2, 500G, the player name
and saved Japanese Merlin nickname intact. File/wake/pause/profile screens retain
the original stats, Charm and Fire v1. Reference/default/isolated EEPROM hashes
are identical. No in-game save was attempted; no savestate was loaded or created.

The new guide, label and pest contexts were not reached. Reader sizes are verified
from code, and all encoded rows/counts/pointers are checked in the ROM. Native
guide frames, control/icon alignment, tournament modes, longer label contexts and
pest success/failure still need gameplay checks. Earlier reaction/mood/bedtime/
food/name/donor/regional scenes, anchored pages and VS/Transfer Pak also remain.
Evidence is in local/minigame-guide-evidence; static reader evidence is labelled
separately from the native-save runtime images.

Final MD5: `207D8DD005BF2BF6E704501AB50C05F4`.
SHA-256: `68d9284ccd8186fdd2f56f282269d172ce0d5a5b14e4fb36359f5d0afffbe97a`.
The 32 MiB ROM keeps CIC-6102 CRC1/CRC2 `FFA89600 C278C65F`.

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/minigame-guide-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/minigame-guide-alpha.z64 --patch local/minigame-guide-alpha.bps
```

Apply the release BPS directly to the exact Japanese original, without stacking
patches. Floating IPS independently reproduces the target. Read-only chksum64
agrees with the header. All 134 tests pass in source and clean restoration.
The preceding bot-reactions ROM also rebuilds byte-identically with the new code.

The AES-256 backup uses two verified ciphertext parts and the existing passphrase,
which stays outside Git. Reassembly reproduces the ciphertext; decryption matches
the packaged ZIP. Clean restoration checks all **822 payload files**, source
revision, ROM/BPS/save/evidence hashes, executable modes, library symlink and the
exact-ROM 16Kbit EEPROM profile. See backups/README.md and RESTORE.md for exact
join/decrypt commands; both parts are required.

Continue ongoing-chore bot dialogue at **3342**, preserving all occupied storage.

## New text

Slash separates grid/dialogue lines; PAGE indicates an original page separator.

| ID | English |
| --- | --- |
| 3320 | Knuckle |
| 3321 | Hammer |
| 3322 | Punch |
| 3323 | Mash A to / pull band. / Keep power / up, below / gauge max. / Beat rival / to win! |
| 3324 | Jump over / blocks to / get orbs. / Too many / block hits / will make / you fail. |
| 3325 | Guard ship / against / falling / missiles! / Press A to / fire beams / at them. |
| 3326 | Face it / with stick / Mash A & B / Push back! / Do it fast / to earn a / 3pt bonus! |
| 3327 | Mash A to / row boat. / Race rival / to finish. / Watch for / sharks and / whirlpools |
| 3328 | Mash A to pull rubber / Keep power above foe / Too fast tires you! |
| 3329 | Pull rubber / Unused / Unused |
| 3330 | Jump blocks; get orbs / Meet the orb quota. / Blocks hurt on impact |
| 3331 | Jump / Unused / Move left/right |
| 3332 | Guard ship with beams / Shoot missile quota. / Keep it from sinking! |
| 3333 | Fire bot beam / Fire bot beam / Move left/right |
| 3334 | Face threats. Mash A / to push objects back. / Meet the push quota. |
| 3335 | Push objects / Push objects / Turn |
| 3336 | Steer boat with stick / Mash A; B to dash. / Beat rival to goal! |
| 3337 | Row boat / Dash / Steer |
| 3338 | Rat bots driven / away! / PAGE / The runners are / safe! |
| 3339 | Rat control / failed! / PAGE / Runners were / eaten... |
| 3340 | Clean often! / or rat bots will / swarm aboard! / PAGE / All your runners / may be lost! / Be careful! |
| 3341 | Clean often! / Rat bots may / swarm aboard / PAGE / Take care or / all runners may / be lost! |
