# Cabin and name-entry alpha

This cumulative BPS includes the prior 66 opening captions and eleven save-menu
strings, plus 26 cabin dialogue records (189–214), seven name-entry labels, and
two embedded Yes/No choice blocks. It contains 112 catalog entries; each choice
block contains two labels. It is an incomplete, condensed English draft.

## Build and apply

From `/workspace/rom-test`:

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/cabin-menu.json --story translation/cabin.json \
  --choices translation/cabin-choices.json \
  --output local/cabin-alpha.z64 --patch local/cabin-alpha.bps
python -m unittest discover -s tests -v
```

Apply `releases/cabin-alpha.bps` to the exact original Japanese ROM with a BPS
patcher. Do not stack it over an earlier patch. The source SHA-256 is
`02cda6221c10cba0705f351227e2d6c77e071bdb4f7aa8b5cd3c7c047a2b1881`.

## Dialogue controls

The conservative codec in `tools/dialogue.py` supports the controls observed in
this conversation:

| Word | Arguments | Observed role |
| --- | --- | --- |
| `2000` | none | New line |
| `2001` | none | Wait/page break |
| `2003` | one word | Text color |
| `200A` | one word | Portrait/expression state |
| `200B` | one word | Player-name insertion |

Catalogue markup such as `[200A:0001]` preserves these exact words and arguments.
The builder rejects unknown commands, missing arguments, altered control
sequences, over-budget records, and lines wider than 16 cells. It reserves five
cells for the player name and limits a dialogue page to three explicit lines.
English text is compacted within the original record allocation; its byte-length
field changes, and its pool offset stays unchanged. Unused allocated bytes are
blank glyphs excluded from the new length.

The first cabin's Yes/No menus are embedded in event bytecode at `0x1969FD4` and
`0x196A02E`, separate from the 4,115-record text pool. Each known 14-byte block is
`2, は, い, 3, い, い, え`. The replacement is `3, Y, e, s, 2, N, o` in native
16-bit glyph indices. Both counts change but the combined size is identical;
surrounding event instructions and addresses remain untouched. Exact original
bytes are guarded, and arbitrary script edits are not supported.

## Scope and remaining work

The cabin translation reaches Dr. Dandy's intervention and the apology for taking
the Gyojin. His longer discussion from record 215 onward remains Japanese. Names
and terminology are provisional and tracked in `translation/glossary.json`.

Name-entry headings, the name label, the Hira/Kana toggle, space, delete and
confirmation labels are translated. The kana grid and initial player name remain
Japanese. Latin input and name-storage changes require separate work.

The original ROM and ROM size are preserved; checksum-covered bytes in the
modified copy remain identical to the original.
Floating IPS independently applies the BPS, yielding a ROM byte-identical to the
builder's output. The automated suite has 49 passing tests, including control
preservation, page/line limits, player-name width, and native choice lengths.

For fast manual testing, `--nospeedlimit` disables the emulator's speed cap. In a
new game, Return/Start skips the opening narration and reaches the first cabin
conversation. Left Shift is A; left Control is B. Short `tools/desktop.py --hold
0.03 --key Down` input is useful for navigating menus with the speed cap off.
Use a cold boot when validating a new ROM; do not rely on cached text in older
savestates.

## Runtime evidence for the release build

A cold boot reached the translated opening cabin conversation. Representative
screens verified portrait changes, two colors in the Caramela/Caramel exchange,
and three-line English dialogue. The ship computer displayed its English
password instructions and opened the translated Name Entry screen.

A five-character test name appeared correctly in the colored confirmation
placeholder. The first embedded choice block rendered **Yes / No** with the
original popup width. Choosing Yes registered the name, launched the ship, and
advanced through the rescue to record 214's English apology to Dr. Dandy.
Choosing No in a separate traversal displayed `ENTER / YOUR PASSWORD / AGAIN.`.
This is functional branch coverage, not a word-by-word review of every frame.
The second embedded choice block and the reverse Hira toggle were not separately
exercised. No completed in-game save/load cycle has been verified.

Local research artifacts for this exact ROM include:

- `local/name-entry-cabin-alpha.st0`: checkpoint before entering a test name.
- `local/after-cabin-alpha.st0`: checkpoint after the translated conversation.
- `local/name-retry-ready.png`: translated name-entry labels, kana grid unchanged.
- `local/name-choice-english.png`: English Yes/No choices and colored player name.
- `local/name-retry-english.png`: No branch's English retry prompt.
- `local/departure-19.png`: translated apology after Dr. Dandy's intervention.

These are local emulator artifacts, not in-game save files. When the ROM changes,
use a cold boot for validation to avoid old text retained in a savestate.
