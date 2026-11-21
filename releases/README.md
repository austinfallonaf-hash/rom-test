# Experimental patches

Apply one patch to the original big-endian Japanese ROM with SHA-256
`02cda6221c10cba0705f351227e2d6c77e071bdb4f7aa8b5cd3c7c047a2b1881`.
Do not stack patches. Keep a backup of your ROM and saves.

- `bot-book-alpha.bps`: current cumulative partial draft with 3,965 native records,
  832 UI strings, 299 choices and three bitmap captions. Adds 184 lines across
  46 biographies, guarded tail placement and one condensed book-reader word.
  See `docs/bot-book-alpha.md` and its manifest. Apply to the exact original.

- `equipment-labels-alpha.bps`: earlier cumulative partial draft with 3,781 native
  records, 832 UI strings, 299 choices and three bitmap captions. Adds 127 equipment
  labels, eight fuel warnings and four guarded equipment-name font-scale edits.
  See `docs/equipment-labels-alpha.md` and its manifest. Apply to the exact original.

- `chore-dialogue-alpha.bps`: earlier cumulative partial draft with 3,646 native
  records, 832 UI strings, 299 choices and three bitmap captions. Adds 195 ongoing
  chore lines across fifteen voices. See `docs/chore-dialogue-alpha.md` and its
  manifest. Apply directly to the exact Japanese original.

- `minigame-guide-alpha.bps`: earlier cumulative partial draft with 3,451 native
  records, 832 UI strings, 299 choices and three bitmap captions. Adds fifteen
  fixed-grid guides, three labels and four pest-control messages. See
  `docs/minigame-guide-alpha.md` and its manifest. Apply directly to the original.

- `bot-reactions-alpha.bps`: earlier cumulative partial draft with 3,429 native
  records, 832 UI strings, 299 choices and three bitmap captions. Adds 240 bot
  task/training, meal and shower reactions. See `docs/bot-reactions-alpha.md`
  and its manifest. Apply directly to the original Japanese ROM.

- `bot-interaction-alpha.bps`: earlier cumulative partial draft with 3,189 native
  records, 832 UI strings, 299 choices and three bitmap captions. Adds 105 bot
  mood/interaction lines and the ship interior prompt. Preserves all earlier
  text and stored labels. See `docs/bot-interaction-alpha.md` and its manifest.

- `bot-food-alpha.bps`: earlier cumulative partial draft with 3,083 native
  records, 832 UI strings, 299 choices and three bitmap captions. Adds 30 bedtime
  lines and 42 food labels, preserving earlier roster storage and Berry.
  See `docs/bot-food-alpha.md` and its manifest. Apply only to the original.

- `roster-names-alpha.bps`: earlier cumulative partial draft with 3,011 native
  records, 832 UI strings, 299 choices and three bitmap captions. Adds 93 native
  roster/speaker labels and the remaining Dome rank refusal. Longer labels borrow
  guarded text-pool padding. See `docs/roster-names-alpha.md` and its manifest.
  Apply only to the original.

- `sunny-blue-variants-alpha.bps`: earlier cumulative partial draft with 2,917
  native records, 832 UI strings, 299 choices and three bitmap captions. Adds
  alternate Sunny Blue rematches, finale, closing narration and approach scenes.
  See `docs/sunny-blue-variants-alpha.md` and its manifest for scope and validation.
  Apply only to the original.

- `sunny-blue-finale-alpha.bps`: earlier cumulative partial draft with 2,777
  native records, 832 UI strings, 299 choices and three bitmap captions. Adds
  the main Doctor Zero confrontation, Caramel revival, escape and approach.
  See `docs/sunny-blue-finale-alpha.md` and its manifest for scope and validation.
  Apply only to the original.

- `sunny-blue-rematches-alpha.bps`: earlier cumulative partial draft with 2,730
  native records, 832 UI strings, 299 choices and three bitmap captions. Adds
  five returning bosses, united Musketeers, farewell and Sun inventory label.
  See `docs/sunny-blue-rematches-alpha.md` and its manifest for scope and validation.
  Apply only to the original.

- `land-blue-variants-alpha.bps`: earlier cumulative partial draft with 2,637
  native records, 832 UI strings, 299 choices and three bitmap captions. Adds
  alternate Land Blue, rising-island hints and Kujiran/warning/departure variants.
  See `docs/land-blue-variants-alpha.md` and its manifest for scope and validation.
  Apply only to the original.

- `land-blue-story-alpha.bps`: earlier cumulative partial draft with 2,438 native
  records, 832 UI strings, 299 choices and three bitmap captions. Adds main Land
  Blue, shallow/deep Musketeers, rising islands, Kujiran and Earth Caramela. See
  `docs/land-blue-story-alpha.md` and its manifest for scope and validation.
  Apply only to the original.

- `gold-blue-variants-alpha.bps`: earlier cumulative partial draft with 2,252
  native records, 832 UI strings, 299 choices and three bitmap captions. Adds
  alternate Gold Blue, regional hints and arrival/collision variants. See
  `docs/gold-blue-variants-alpha.md` and its manifest for scope and validation.
  Apply only to the original.

- `gold-blue-story-alpha.bps`: earlier cumulative partial draft with 2,072
  native records, 832 UI strings, 299 choices and three bitmap captions. Adds
  main Gold Blue training, fighters, Linlin, frozen-sea history and departure.
  See `docs/gold-blue-story-alpha.md` and its manifest for scope and validation.
  Apply only to the original.

- `roulette-variants-alpha.bps`: earlier cumulative partial draft with 1,906
  native records, 832 UI strings, 299 choices and three bitmap captions. Adds the
  alternate Roulette route, Tree Blue hints and arrival/abduction variants. See
  `docs/roulette-variants-alpha.md` and its manifest for scope and validation.
  Apply only to the original.

- `roulette-story-alpha.bps`: earlier cumulative partial draft with 1,671 native
  records, 832 UI strings, 299 choices and three bitmap captions. Adds the main
  Roulette rescue route, pirate encounters/traps, arrival/abduction and Gold Blue
  departure. See `docs/roulette-story-alpha.md` and its manifest for precise scope
  and validation. Apply only to the original.

- `water-blue-story-alpha.bps`: earlier cumulative partial draft with 1,450
  native records, 832 UI strings, 299 choices and three bitmap captions. Adds
  Water Blue encounters/ID cards, ship-parts quest and swaps, prize game, regional
  hints and radio warning in both routes. See `docs/water-blue-story-alpha.md`
  and its manifest for scope and validation. Apply only to the original.

- `fire-blue-variants-alpha.bps`: earlier cumulative partial draft, with 1,189
  native records, 832 UI strings, 299 choices and three bitmap captions. Adds
  Black Musketeers interludes, Mikachi recruitment, alternate Fire Blue scenes
  and regional hints. See `docs/fire-blue-variants-alpha.md` and its manifest
  for exact scope, layout exception and validation. Apply only to the original.

- `menu-proof.ips`: original two-string proof.
- `save-menu-alpha.ips`: cumulative eleven-string save-menu alpha; supersedes
  the proof. See `docs/save-menu-alpha.md` for runtime coverage and limitations.

Neither file is a full translation. No ROM data is supplied with the patches.

- `intro-alpha.bps`: earlier cumulative opening patch, 66 opening-caption records plus
  the eleven save-menu strings. Apply to the exact original, using Floating IPS
  or another BPS-compatible patcher. This supersedes both earlier IPS files.
  Story wording is a condensed draft, not a complete game translation.
  See `docs/story-format.md` and `intro-alpha-manifest.json` for evidence/hashes.

- `cabin-alpha.bps`: earlier cumulative cabin patch. Adds the first cabin conversation,
  ship-computer name prompts, name-entry labels, and embedded Yes/No choices.
  Supersedes the opening alpha; apply only to the original ROM. See
  `docs/cabin-alpha.md` and `cabin-alpha-manifest.json`.

- `dandy-alpha.bps`: earlier cumulative tutorial patch. Adds Dr. Dandy's recruitment and
  refusal dialogue, the promise sequence, and the first gardening/reward tutorial.
  Supersedes earlier patches; apply only to the original ROM. See
  `docs/dandy-alpha.md` and `dandy-alpha-manifest.json`.

- `ship-menu-alpha.bps`: earlier cumulative patch. Adds compact pause-menu,
  profile, equipment and starter-item labels. Supersedes earlier patches;
  apply only to the original ROM. See `docs/ship-menu-alpha.md` and
  `ship-menu-alpha-manifest.json` for coverage and hashes.

- `ship-help-alpha.bps` and `bed-save-alpha.bps`: earlier cumulative ship guides
  and verified bed/save flow. See their corresponding documents and manifests.
- `care-guide-alpha.bps` and `battle-guide-alpha.bps`: earlier cumulative bot-care
  and battle-help guides. See their corresponding documents and manifests.
- `moon-blue-alpha.bps`: earlier cumulative first-sea story/hint draft, including
  Koron and the Red Pass. See `docs/moon-blue-alpha.md`.
- `shop-alpha.bps`: earlier cumulative patch. Adds shared seed/parts shop UI and
  ten compact color-seed labels. See `docs/shop-alpha.md` and
  `shop-alpha-manifest.json`. Apply only to the exact original ROM.

- `simulator-alpha.bps`: earlier cumulative patch. Adds reconstructed gardening
  text/nine seed names and simulator/battle-result UI. See `docs/simulator-alpha.md`
  for the distinction from the unavailable historical gardening patch and the
  precise runtime coverage. Apply only to the exact original ROM.
