# Experimental patches

Apply one patch to the original big-endian Japanese ROM with SHA-256
`02cda6221c10cba0705f351227e2d6c77e071bdb4f7aa8b5cd3c7c047a2b1881`.
Do not stack patches. Keep a backup of your ROM and saves.

- `fire-blue-variants-alpha.bps`: current cumulative partial draft, with 1,189
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
