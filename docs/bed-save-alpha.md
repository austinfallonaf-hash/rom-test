# Bed and save alpha

This cumulative draft adds twenty UI strings for bed/save interaction, waking up,
doctor greetings, floor selection and ship destinations. The complete catalogs contain
142 native text records, 129 Shift-JIS UI strings and sixteen native Yes/No
blocks. Earlier translated content is retained unchanged.

Apply `releases/bed-save-alpha.bps` to the exact original Japanese ROM; do not
stack it on an earlier patch.

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/bed-save-menu.json --story translation/ship-help-text.json \
  --choices translation/dandy-choices.json \
  --output local/bed-save-alpha.z64 --patch local/bed-save-alpha.bps
python -m unittest discover -s tests -q
```

## New text

The bed confirmation reads `Rest in bed? / Your progress / will be saved.` The
separate refusal reads `A bot still has / chores to do. / You can't sleep.`,
retaining the original highlighted bot text. The shared ship confirmation uses
`Yes` and `No`, with intentional trailing spaces to preserve the original
four-/six-byte label lengths. Unpadded ASCII made this popup size its box too
narrowly; the padded labels restore its original width and fit visibly. The
ordinary wake-up message becomes `Let's do our / best!`, within its
twenty-byte allocation. The special day-100 wake-up message remains unfinished.

The help guide's permission to leave daily activities unfinished does not
override this distinct condition for a bot still doing chores. The patch keeps
both messages and does not change which condition the game checks.

R opens ship navigation. Floor labels use 3F/2F/1F; destination labels include
Bed, Pots, Deck, Helm, GB Link, Btl Sim, Bot Book, Doctor, Store and Stars. The
two doctor greetings become `How's it going?`. Face the bed and tap A to open
its confirmation. Short A taps avoid unintended repeated confirmations during
automated input.

All new edits are guarded against the original Shift-JIS bytes and preserve
addresses, byte budgets, existing color commands and the checksum-covered
region. No save-format or event logic is changed. Glide64mk2 remains the
recommended graphics plugin; see the renderer comparison in
[ship-help notes](ship-help-alpha.md).

## Verification

All 64 existing tests pass. Floating IPS independently applies the final BPS and
reproduces the generated ROM byte-for-byte. The source ROM hash and size are
unchanged.

An initial cold boot traversed the opening/tutorial, starting at day 0 with 500G
and Merlin in the party. Declining the bed prompt returned to control without
creating an EEPROM file. Accepting wrote a 2048-byte EEPROM file and advanced to
the morning scene; the pause menu then showed day 1 and 500G.

The confirmation-label and wake-up wording were finalized after that initial
run. For final-build testing, its day-1 EEPROM was copied to the new ROM's
MD5-based save filename. No emulator savestate was used.

On the exact final build (`793AFD73` MD5 prefix), the fitted Yes/No popup was
visually checked. Declining left day 1, 500G and the EEPROM bytes unchanged.
Accepting wrote a changed 2048-byte EEPROM and advanced to day 2. The emulator
was then closed and started again with the same ROM. Selecting file A restored
day 2 and 500G, with the same entered player name and Merlin visible. Loading
left the saved EEPROM byte-identical. This establishes a real in-game save/load
cycle on the tested emulator, independently of emulator savestates.

The final build is reproducible from the catalogs, and Floating IPS reproduces
it from the shipped BPS. The release manifest records its hashes and sizes.
Local evidence includes `bed-save-final-fitted-prompt.png`,
`bed-save-final-declined-day1.png`, `bed-save-final-accepted-morning.png`,
`bed-save-final-day2-status.png` and `bed-save-reloaded-day2-status.png`.
The native save backup is `local/bed-save-final-saved.eep`; it corresponds to
the final ROM's `793AFD73` save filename and is not an emulator savestate.

## Remaining work

The later story, bot-care/battle help, most names and graphical headings remain
unfinished. Runtime checks covered the floor selector, 3F destinations and bed
flow. The chores refusal, 2F destination labels, both new doctor greetings,
day-100 message and file B need separate coverage.
