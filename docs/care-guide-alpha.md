# Bot-care guide alpha

This cumulative draft adds native records 2659–2672 and seven bot-care topic
labels. It includes the earlier opening, cabin/tutorial, inventory labels,
ship help and bed/save translation. Totals: 156 native records,
136 Shift-JIS UI strings and sixteen native choice blocks.

Apply `releases/care-guide-alpha.bps` to the exact original Japanese ROM. Do not
stack it on an older patch.

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/care-guide-menu.json --story translation/care-guide-text.json \
  --choices translation/dandy-choices.json \
  --output local/care-guide-alpha.z64 --patch local/care-guide-alpha.bps
python -m unittest discover -s tests -q
```

## Added topics

| Menu | Details retained |
| --- | --- |
| CPU | More CPU bits mean greater intelligence; chores and attacks from behind increase bits |
| Gear | Parts act as weapons and affect stats; RAM capacity matters as well as power |
| Apps | Up to three apps per part; available RAM limits installation; higher versions require more RAM; combinations can unlock moves |
| Chores | Cleaning, fishing, massage, maintenance and stoking fuel; bot-specific aptitude; overwork causes stress and failures; successful work earns medals |
| Train | Stretch raises EP, Aim Attack, Catch Defense, Jump Speed and Cross HP; goals grow harder; training costs medals earned through chores |
| Food | Hunger delays battle attacks; some meals raise stats; disliked food increases stress |
| Shower | Showers reduce stress; stress increases the wait before attacking |

All fourteen records retain their original control streams, including every
page break, newline and portrait argument. Record 2662's unusual closing
`200A:0001` on its fuel-stoking page is preserved. The two chore explanations
have different page counts; training and shower page layouts also differ.
The older food guide retains its joke asking children not to be picky, while
Dr. Dandy's version asks the player to learn each bot's food preferences.

English stays within sixteen cells per line and each original record's byte
allocation. No relocation, event changes, stat adjustments or checksum changes
are made. Topic labels are six cells or fewer. In the 2F navigation submenu,
`Bot Book` is shortened to `Book` after its last letter extended past the box.

## Verification

The guarded builder verifies every original record and UI string, all budgets
and the checksum-covered prefix. All 64 existing tests pass. Floating IPS
independently applies the BPS and produces a byte-identical ROM. All earlier
native records are retained unchanged. Earlier UI entries are retained except
for the shorter navigation caption.

A cold boot of the final ROM (`60452D63` MD5 prefix) loaded the existing day-2
EEPROM through file A. The native save was copied under this build's new
MD5-based filename; old-build emulator savestates were not used. The save bytes
remained unchanged throughout these checks. Glide64mk2 is the recommended
renderer.

R navigation reached 2F/Doctor. The shortened `Book` caption fits the navigation
box, and the doctor's greeting displays in English. Under Bot Help, all seven
topics were traversed to their return prompts: CPU (3 pages), Gear (4), Apps
(5), Chores (6), Train (10), Food (8) and Shower (3). Both the upper and lower
sections of the scrolling topic menu fit. The three-app limit, RAM explanation,
medal reward, exercise/stat mappings, disliked-food warning and shower/attack
delay explanation were visible in English.

Local evidence includes `care-final-2f-menu.png`, `care-final-main-menu.png`,
`care-final-topic-menu.png`, `care-final-topics-bottom.png`, `care-cpu-2.png`,
`care-gear-3.png`, `care-apps-5.png`, `care-chores-6.png`,
`care-training-7.png`, `care-food-7.png` and `care-shower-3.png`.
The final release manifest records sizes and SHA-256 hashes; its patch also
matches the independently applied ROM byte-for-byte.

## Remaining work

Battle-help explanations, later story, most names and graphical headings remain
unfinished. Translating these explanations does not verify the mechanics they
describe. The alternate doctor version requires separate runtime coverage.
