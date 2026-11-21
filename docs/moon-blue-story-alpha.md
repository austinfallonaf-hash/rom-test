# Moon Blue story alpha

The main Moon Blue encounter sequence now has an English draft through Johnny's
defeat, the Moon Caramela reward and departure toward Fire Blue. This milestone
adds **222 native records**, retaining the preceding 396 records exactly.
Cumulative coverage is **618 native records, 832 UI strings, 299 choice blocks
and three bitmap captions**. This remains a partial translation; regional hints,
the Battler Dome and later seas are still unfinished.

## Added coverage

| Records | Content |
| --- | --- |
| 49–64, 300–315 | Sharol, Free Pass reward and rematches |
| 65–84, 316–335 | Dean, Purple Key reward and island gate |
| 85–104, 336–355 | Godoshii, Clear Key reward and Johnny's gate |
| 105–124, 356–375 | Johnny, Moon Caramela reward, retreat and departure hints |
| 125–188 | Coaster attendants, pass restrictions, return routes and Fire Blue exit |
| 246–248 | Additional post-Johnny transition variant |
| 3673, 3688–3689 | Native inventory labels: Full Moon, Purple and Clear |

There are 219 encounter/coaster/transition entries plus three inventory labels.
The new control-bearing messages contain 326 pages and 817 lines, counting
repeated branches separately. All native record IDs 0–389 now have catalog
entries, including the previously translated tutorial and opening encounters.
This does not establish complete Moon Blue coverage: regional hint records
starting at 390 and Battler Dome material remain untranslated.

## Language and format

Existing provisional character names and Moon Caramela terminology are retained.
Purple Key opens access to Godoshii's island; Clear Key permits the Johnny
challenge. Dialogue uses the full key names. Their six- and five-glyph inventory
fields use Purple and Clear. The nine-glyph treasure label uses Full Moon.
The glossary also records Fire Blue and the alternate companion name Ram.

Dialogue is condensed to the original allocations. Every original portrait,
expression, color, page, line and player-name command retains its exact arguments
and order. Player-name substitution reserves the original five cells. Lines stay
within 16 cells and pages within three lines. No new layout controls, relocated
records, expanded allocations or relaxed codec checks were introduced. Record
172 retains its source's trailing page/reset commands, including the empty page.
The high native-text edits leave CIC-6102 CRC1/CRC2 unchanged.

## Rebuild and validation

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/moon-blue-story-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/moon-blue-story-alpha.z64 --patch local/moon-blue-story-alpha.bps
```

Apply `releases/moon-blue-story-alpha.bps` directly to the exact Japanese original
without stacking patches. The target remains 32 MiB. Its MD5 is
`A6628793B851E3D6602FD7FF9981C121`; source, target and patch hashes are in the
release manifest. CRC1/CRC2 remain `FFA89600 C278C65F`.

The guarded builder checks exact source bytes and metadata, control streams,
widths, allocations and overlapping edits. All 108 tests pass. Floating IPS
independently reproduces the final target from the BPS; chksum64 independently
agrees with its header CRCs. All preceding native entries compare equal.

The final ROM cold-boots using an isolated copy of the preserved native day-2
EEPROM. File A retains 500G, the entered player name and Merlin. Ship/pause and
equipment rendering are checked, including the inherited English bitmap captions.
No older-build state is loaded. Evidence is under `local/moon-blue-story-evidence/`
in the encrypted recovery archive; the immutable reference EEPROM is unchanged.

**The newly translated encounter, reward, gate and coaster branches have build
validation only; they have not been reached in a playthrough of this ROM.**
Runtime checks use the supplied Mupen64Plus/Glide64mk2 environment and establish
a loading/menu regression check, not new-branch or hardware coverage. Earlier
coverage remains in [Blue Pass notes](blue-pass-alpha.md) and
[interface heading notes](interface-headings-alpha.md).

## Next work

Translate the remaining Moon Blue regional hints beginning at record 390 and
the Battler Dome material, then continue Fire Blue. Play through the newly
translated encounters and coaster routes. Other graphical headings, the shop
Parts frame, capacity warnings and VS/Transfer Pak branches remain unfinished.
