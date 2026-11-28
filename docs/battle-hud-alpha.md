# Battle HUD alpha

This cumulative draft adds 159 guarded UI strings to simulator-alpha, for
279 native records, 420 UI strings and 299 native choice blocks. All previous
catalog entries are preserved unchanged. It is a partial English translation.

## New text

- Sixteen base bot names used by battle/demo tables. Native save nicknames and
  names drawn through other tables are unchanged.
- Battle escape/reward/defeat and give-up prompts, the miss notice and EP popup.
- Thirty status/effect notices: curse, heat, bug, fog, stop, rust, soaking/oil,
  extra/recoil damage, software/move restrictions, stat changes and defenses.
- Eleven energy-orb notices and eleven compact HUD status labels.
- Four special move names and 79 shared move-name components, including the
  Fire/Fara components used by the starter bot. The longest translated prefix
  plus suffix is at most sixteen cells. A few four/six-byte components lack
  room for a separating space; names and specialized terminology are provisional.

The tiny status frame uses at most three cells: `OK` (normal), `Pry` (prayer),
`Cur` (curse), `Hot`, `Bug`, `Fog`, `Inf` (むし, provisional), `Stp` (stopped),
`Rst` (rust) and `Mad` (rampage), plus the unused/dummy `---`.
`Roll` is the compact provisional translation of うけみ; `Shield` fits the
six-byte バリア allocation. These do not establish the precise mechanics of
unplayed effects.

## Build and checksums

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-hud-menu.json --story translation/garden-recovery-text.json \
  --choices translation/story-choices.json --layout translation/battle-hud-layout.json \
  --update-checksum --output local/battle-hud-alpha.z64 --patch local/battle-hud-alpha.bps
```

Apply `releases/battle-hud-alpha.bps` to the exact Japanese original; do not
stack patches. See the release manifest for exact hashes.

These strings lie in the checksum-covered executable. Explicit opt-in repairs
CIC-6102 CRC1/CRC2 while retaining the bootcode and all other header bytes.
The launcher creates an isolated Mupen data directory preserving the source
16Kbit EEPROM and game metadata. See [checksum and emulator notes](n64-checksums.md).
The original ROM and reference EEPROM remain immutable.

All 96 automated tests pass, including independent checksum vectors, opt-in and
bootcode guards, and emulator-profile/save-type preservation. The guarded build
checks every source string, byte budget, printf/control argument and width.
chksum64 independently agrees with the new header checksum. Floating IPS applies
the BPS to produce the exact target ROM.

## Runtime and remaining work

The exact final ROM (MD5 `7A9FF0971182E81B1CCCE3357AF57EB3`) cold-booted
with a separately named copy of the day-2 native EEPROM. The pause screen
showed day 2, 500G and the entered player name, and Merlin remained present.
The simulator roster entered practice battle. Both condensed Attack labels fit
inside their frames, clear of the element icons; the normal OK status label
and Give up / A: Yes / B: No prompt displayed correctly.

Evidence and a same-build exploration state are under `local/battle-hud-evidence/`.
No older-build emulator state was used. Miss/effect variants remain build-validated unless explicitly recorded in the evidence.
Other status effects, bot names and move combinations are build-validated only.
Graphical battle command labels, many full special-move names, most later story,
VS/Transfer Pak branches and the shop Parts frame still need work. Gardening's
five-night runtime coverage belongs to simulator-alpha; see its notes for the
reconstructed text's provenance and limits.

## Battle label layout

The original opponent-name/move alignment counted bytes and divided by two,
which positioned ASCII too far right. The battle layout catalog replaces the
counting loops with Shift-JIS-aware glyph counters: ASCII and half-width kana
count once, and a two-byte lead skips its following byte. Existing name-table
and selected-move pointers/strides are retained. The routines are guarded at
`0xB7278..0xB72EF` and `0xB75F0..0xB766B`; their branches retain delay slots.
Tests execute the shipped MIPS words against ASCII, Japanese, mixed strings,
half-width kana, empty strings and nonzero selection indices.

Both teams' name/move labels use horizontal scale 0.5 and original vertical
scale 1.0, allowing ten name cells and sixteen move cells inside the frames.
The opponent anchors stay fixed: name `236+(10-glyphs)*6` and move
`170+(16-glyphs)*6`, in native screen coordinates. Other captions and the tiny
status font retain their existing scale. This includes 69 guarded battle
instruction words and the unchanged earlier shop layout edit.
