# Dr. Dandy and gardening tutorial alpha

This draft adds native records 215–245: Dr. Dandy's recruitment, refusal dialogue,
the promise to keep trying, the first Robopon, and the seed/medal tutorial. It
includes the previously translated opening and cabin scene. English remains
condensed to fit the original record allocations; later story text and most game
menus are still Japanese.

Build the cumulative patch from the exact original:

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/cabin-menu.json --story translation/dandy.json \
  --choices translation/dandy-choices.json \
  --output local/dandy-alpha.z64 --patch local/dandy-alpha.bps
python -m unittest discover -s tests -v
```

## Text layout changes

The Merlin reward message has three colored names on what was a two-line window.
Its English names do not fit together on one 16-cell line. Record 241 explicitly
opts into `allow_layout_newlines`; the builder may insert line breaks while
requiring every original control word and argument to remain in order. Other
records retain strict control equality. Page, portrait, color, and variable-name
controls cannot be added or changed by this option.

The replacement is three lines, `PLAYER+Punch / Merlin / joins`. It stays within
the original 33-word allocation and keeps the original text-record address.
This changes the message's presentation; party/reward event instructions remain
untouched.

A trailing newline after three filled lines is also supported. The original
refusal message (223) uses that cursor position without drawing a fourth line.
Visible text on a fourth line remains a build error.

The original ROM hash, ROM size, and checksum-covered first MiB are preserved.
The BPS was applied independently with Floating IPS and the resulting ROM
compared byte-for-byte with the builder output. The added tests cover layout
opt-in, unchanged control arguments, retained original line breaks, empty
trailing cursor lines, and the 31-record catalog's budgets.

Names and terminology remain provisional. Merlin translates メルリン; Ashura Seed
translates アシュラシード. This phase translates the reward messages, not all party
or inventory screens that display those objects.


The event menus are separate from dialogue records. `dandy-choices.json` includes
14 additional guarded Yes/No blocks found in the loaded guardian/promise event
scripts, plus the two earlier name-confirmation blocks. Matching original byte
contexts located them in the ROM. Labels change from 2+3 glyphs to 3+2 glyphs,
so each 14-byte block and every surrounding event address stay the same.
Some blocks belong to mirrored event variants; not every variant is separately
exercised. No refusal/acceptance branch or game-over condition is changed.

## Final release validation

A cold boot of the final ROM traversed the opening/cabin flow and reached the
new recruitment dialogue. The guardian and promise menus both rendered English
Yes/No. Choosing No showed the translated refusal responses; subsequently
accepting allowed the tutorial to continue. These checks cover one refusal in
each sequence; repeated-refusal game-over endings and mirrored event variants
were not separately exercised.

The complete affirmative path then grew the starter Robopon, displayed the
three-line colored Merlin recruitment message, showed the seed/medal tutorial,
and returned to normal ship control with Merlin visible in the HUD. The HUD's
Robopon name and most other gameplay menus remain Japanese. The reward-message
checks do not replace an inventory/save/load test.

All 56 automated tests pass. Floating IPS applied `releases/dandy-alpha.bps` to
the original ROM, and its output matches `local/dandy-alpha.z64` byte-for-byte.
The release manifest records hashes and file sizes. The original ROM remains unchanged. The checksum-covered region in the modified
copy remains identical to the original.

Useful local artifacts:

- `local/guardian-choice-release.png`: English guardian choice.
- `local/guardian-no-response.png`: first refusal response.
- `local/promise-choice-release.png`: English promise choice.
- `local/promise-no-response.png`: first broken-promise response.
- `local/gardening-release-16.png`: three-line Merlin reward, with player name.
- `local/gardening-release-end.png`: control returned to the ship.
- `local/after-gardening-dandy-alpha.st0`: exploration checkpoint for this exact build.

The next work is the ship's gameplay menus and the first island/Caramela quest.
Record 246 onward resumes later story material. Use cold boots to validate new
builds; savestates can retain old loaded text.
