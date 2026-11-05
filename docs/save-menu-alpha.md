# Save-menu alpha

This iteration extends the two-string proof to eleven strings. Use
`translation/save-menu.json` and `releases/save-menu-alpha.ips`; the original
proof remains available separately. Apply either patch to the exact unmodified
Japanese ROM, not on top of another patch.

## Catalog

| Offset | English | Runtime coverage |
| --- | --- | --- |
| `0x2212D8` | Select a / save file. | Save selection |
| `0x221324` | New File | Both empty slots |
| `0x2212A0` | B: Cancel | Selected slot and action menu |
| `0x2212B8` | Start | Action popup |
| `0x2212C8` | Delete | Action popup, disabled for empty slot |
| `0x221290` | Yes | Included; confirmation path not yet exercised |
| `0x221298` | No | Included; confirmation path not yet exercised |
| `0x221308` | P left | Included; populated-save display not yet exercised |
| `0x221338` | No save data. | Included; message not yet exercised |
| `0x22134C` | Delete file A? / Continue? | Included; populated-save deletion not yet exercised |
| `0x221380` | Delete file B? / Continue? | Included; populated-save deletion not yet exercised |

The instruction and confirmation slashes above denote explicit newline commands,
not literal slashes. The action popup is narrower than the bottom dialogue box:
`Start Game` and `Delete File` visibly overflowed, so final labels are `Start` and
`Delete`, with a six-cell build limit. `P left` abbreviates the original Pearlton
remaining label to fit its original eight-glyph footprint; its exact placement
still requires a populated save.

The builder validates byte budgets, source bytes, full-ROM identity, line cell
limits, unsupported/malformed escape sequences, and preserved format parameters.
It also refuses output paths that overwrite the input ROM. All eleven entries
remain in place; neither pointers nor executable code change. The real IPS was
replayed and compared byte-for-byte with the generated ROM. The original hash
and N64 checksum-covered bytes remain unchanged. Eighteen automated tests pass.

## Story and name entry

Selecting Start with the original proof reached the opening harbour and the
illustrated pirate-ship scene. The visible sound-effect subtitles could not be
found as the corresponding plain Shift-JIS strings. This does not establish a
specific compression format. No story bytes were patched based on that mismatch.
The name-entry screen has not yet been reached or translated.

Next work is a new-game/save/load traversal and investigation of the opening
subtitle renderer/asset format. Save-slot header artwork and title artwork remain
Japanese; these are outside this plain-text patch.
