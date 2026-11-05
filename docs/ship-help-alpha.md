# Ship help alpha

This cumulative draft adds eight ship-help topics for both doctor variants
(native records 2673–2688), plus eighteen topic/menu prompts. The catalogs now
contain 142 native text records, 109 Shift-JIS UI strings and sixteen native
Yes/No blocks. Earlier opening, cabin, tutorial and pause-menu translations are
included unchanged.

Apply `releases/ship-help-alpha.bps` to the exact original Japanese ROM. Do not
apply it on top of an earlier patch.

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/ship-help-menu.json --story translation/ship-help-text.json \
  --choices translation/dandy-choices.json \
  --output local/ship-help-alpha.z64 --patch local/ship-help-alpha.bps
python -m unittest discover -s tests -q
```

## Added topics

| Topic | Details retained |
| --- | --- |
| Pearlton | Fuel meter at upper left; running out sinks the ship; selling bots or defeating pirates supplies fuel |
| Pots | Robopon and software seeds; five days for bots, three for software; shops, pirates and training bonuses supply seeds |
| Bed | Resting allows saving; sleep advances one day; unfinished daily tasks do not prevent using the bed |
| GB Link | Transfers in both directions, swapping stored bots between saves A/B, making food once per day |
| Battle Sim | Practice battles using owned Robopon |
| Bot Book | Discovered bots and their descriptions; distinct from the stats display; discover all to complete it |
| Storage | Three active bots, storage/party exchanges, unlimited daily deposits and withdrawals |
| Stars | Achievement rewards and checking which records earned stars |

The English is condensed to sixteen cells per line, within each original
allocation. All original page breaks, line breaks, portrait arguments and the
player-name insertion remain in their original order. No event instructions,
branch targets, save mechanics, or ROM checksums are changed. The two doctor
variants share the English wording while retaining their respective source
records and control streams.

## Verification

The guarded builder validates each new record against the original ROM, checks
line/page and byte budgets, and preserves the checksum-covered region. All 64
existing automated tests pass. Floating IPS independently applies the BPS and
produces a byte-identical ROM. The cumulative catalogs retain all previous
entries unchanged.

A fresh boot of this exact build traversed the opening/tutorial and reached
normal ship control. While facing Dr. Dandy's seated help desk, Z opens the
interaction menu; A confirms a topic, and the stick selects entries.
The six-entry main menu and scrolling eight-topic ship submenu fit. The follow-up
`Anything else? / Ask away!` prompt displays in English. The initial greeting
still appears in Japanese.

The fuel and bed explanations were traversed to the topic menu, with their
facility camera transitions intact. The star explanation retains and displays
the entered player name. The bed guide's three pages display saving, the one-day
advance, and permission to rest before daily tasks are complete. These are help
screens: no actual in-game save/load was performed.

All eight Dr. Dandy topics were traversed, including all eleven seed pages and
their five-day/three-day timings. The GB food guide retains its once-per-day
limit; storage retains three active bots and unlimited daily exchanges. The
other doctor variant (2673–2680) is build-validated, not separately played.

The input helper recognizes Mupen64Plus by its X11 window class as well as its
title, so it also focuses the Glide64mk2 window. Its F7 load was checked with a
checkpoint from this identical ROM build; no earlier-build state was used to
validate the new text.

Rice rendering sometimes puts foreground world geometry over the help window
(seen in the simulator, encyclopedia and GB Link camera views). On this same ROM
build, the bundled Glide64mk2 displays complete dialogue above foreground
geometry in all three affected views. Glide64mk2 is therefore the recommended
renderer; no ROM change was needed for this display difference. A later steady
capture also confirms the complete `Sleeping will / advance one day.` page.

Local evidence includes `ship-help-topic-menu.png`, `ship-help-topics-bottom.png`,
`ship-help-bed-1.png`, `ship-help-bed-2-steady.png`, `ship-help-seeds-8.png`,
`ship-help-stars-1.png`, `ship-help-glide-sim-2.png`,
`ship-help-glide-book-3.png` and `ship-help-glide-gb-food.png` under `local/`.
`local/after-ship-help-alpha.st0` is a checkpoint at Dr. Dandy's ship-help menu
for this exact ROM build. Cold-boot future builds; a state can retain previously loaded script data.

## Remaining work

Bot-care and battle-help explanations, evolution/recall/rename prompts, actual
bed/save dialogs, later story, graphic headings, most names and the kana grid
still need work. Translating a guide does not verify the described mechanics:
in-game saving/loading, GB transfer and every help variant need separate runtime
coverage. Emulator savestates are exploration checkpoints, not in-game saves.
