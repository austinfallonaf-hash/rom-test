# Project backup

Latest snapshot: **Ship facility captions alpha**, adding seven UI strings and
completing the eight floating facility labels. Coverage: 4,049 native records,
873 UI strings, 299 choices and three bitmap captions. All 150 tests pass.
Other UI/graphics and runtime coverage remain incomplete.
See `docs/facility-captions-alpha.md`.

The encrypted archive is split into two parts so each is below GitHub's file
limit. `robopon64-facility-captions-alpha-AD3B8484.zip.gpg.parts.json` records the
ordered filenames, byte counts and hashes, plus the whole ciphertext identity.
Both parts together contain the original/current ROMs, emulator, source catalogs,
tools/tests/docs/patches, historical/current runtime evidence, screenshot/input
dependencies and native saves. The exact-ROM emulator profile is included.

The archive contains **996 payload files**, verified by size and SHA-256. The
source suite passes all 150 tests, including after clean restoration.

The archive uses AES-256 and the existing recovery passphrase supplied in the project conversation. The passphrase, Git credentials, repository metadata, raw conversation PDF and duplicate historical ROM builds are excluded. Earlier ROMs can be rebuilt from the original and their included cumulative patches.

## Local checkout size

This workspace uses non-cone sparse checkout to keep the current and preceding
encrypted snapshots on disk. Older encrypted files remain in local Git and on
GitHub; they were omitted only after their working copies matched committed
blob IDs on the verified canonical remote. This frees 2,309,087,743 bytes of
redundant working copies. Source, patches, original ROM and native saves stay
present. The historical snapshots listed below remain available through Git.

Current patterns (the stars are literal Git patterns):

```sh
git sparse-checkout set --no-cone --stdin <<'PATTERNS'
/*
!/backups/*
/backups/README.md
/backups/robopon64-book-interface-alpha-*
/backups/robopon64-facility-captions-alpha-*
PATTERNS
```

For the next milestone, update the included backup slugs before staging new
parts. Keep current/preceding snapshots locally; changing these patterns does
not delete history or Git objects. A trial repository verified that the patterns
preserve source and ignored private assets, accept the next included backup and
reverse correctly. To retrieve one omitted file, use `git show HEAD:backups/FILENAME`
and redirect it to a new staging file. `git sparse-checkout disable` restores the
full tracked tree, requiring the omitted working copies' disk space again.
Git configuration is not archived in the private ZIP; these commands apply to
a Git checkout, not a plain restored source directory.

## Restore

Download both `.part001` and `.part002`, the JSON index and all three checksum
files from this directory. Keep their filenames intact. Verify and join in order:

```sh
sha256sum -c robopon64-facility-captions-alpha-AD3B8484.zip.gpg.parts.sha256
cat robopon64-facility-captions-alpha-AD3B8484.zip.gpg.part001 robopon64-facility-captions-alpha-AD3B8484.zip.gpg.part002 > robopon64-facility-captions-alpha-AD3B8484.zip.gpg
sha256sum -c robopon64-facility-captions-alpha-AD3B8484.zip.gpg.sha256
gpg --output robopon64-facility-captions-alpha-AD3B8484.zip --decrypt robopon64-facility-captions-alpha-AD3B8484.zip.gpg
sha256sum -c robopon64-facility-captions-alpha-AD3B8484.zip.sha256
```

Use a new staging directory to avoid overwriting an earlier decrypted copy.
A missing, damaged or out-of-order part fails the checksum checks. Each part
contains only ciphertext; it is not independently decryptable.

Enter the existing passphrase when prompted. From the latest source checkout, verify and restore into a new directory:

```sh
python tools/verify_backup.py /path/to/robopon64-facility-captions-alpha-AD3B8484.zip
python -m tools.restore_backup /path/to/robopon64-facility-captions-alpha-AD3B8484.zip /path/to/new-directory
```

Follow the restored `rom-test/RESTORE.md` and `RESUME.md`. `BACKUP_MANIFEST.json` records each payload's size and SHA-256. The restore tool preserves executable modes and the emulator library symlink, and refuses an existing destination.

Keep the latest verified restore tree and clear superseded generated test copies
under `/workspace/work/` when needed. Preserve old manifests and check extracted
files for changes before removing their test trees. Extra files must match
canonical copies; preserve unmatched files. A superseded decrypted staging
ZIP can be removed after its hash matches the recorded checksum. This retention
step prevents repeated recovery tests from filling the cloud workspace.

The default native EEPROM remains the verified day-2 file A with 500G, the entered player name and Merlin. It uses the current ROM's `AD3B8484` filename. Separate runtime checkpoints under `local/facility-captions-evidence/`, `local/book-interface-evidence/`, `local/late-dialogue-evidence/`, `local/bot-book-evidence/`, `local/equipment-labels-evidence/`, `local/chore-dialogue-evidence/`, `local/minigame-guide-evidence/`, `local/bot-reactions-evidence/`, `local/bot-interaction-evidence/`, `local/bot-food-evidence/`, `local/roster-names-evidence/`, `local/sunny-blue-variants-evidence/`, `local/sunny-blue-finale-evidence/`, `local/sunny-blue-rematches-evidence/`, `local/land-blue-variants-evidence/`, `local/land-blue-story-evidence/`, `local/gold-blue-variants-evidence/`, `local/gold-blue-story-evidence/`, `local/roulette-variants-evidence/`, `local/roulette-story-evidence/`, `local/water-blue-story-evidence/`, `local/fire-blue-variants-evidence/`, `local/fire-blue-story-evidence/`, `local/battler-dome-evidence/`, `local/moon-blue-story-evidence/`, `local/blue-pass-evidence/`, `local/interface-headings-evidence/`, `local/battle-moves-evidence/`, `local/battle-hud-evidence/` and `local/simulator-evidence/` are test copies, identified by their notes; keep the immutable reference EEPROM intact.

The earlier shop snapshot `robopon64-progress-2026-11-05_135201-PST.zip.gpg` and bed/save snapshot `robopon64-progress-2026-11-05_012741-PST.zip.gpg` remain historical backups. They do not contain the reconstructed simulator milestone. Historical emulator states belong only to their exact ROMs.

The preceding simulator snapshot `robopon64-simulator-alpha-20B19F3D.zip.gpg` remains available with its original 421-file manifest.

The preceding battle HUD snapshot `robopon64-battle-hud-alpha-7A9FF097.zip.gpg` remains available with its original 441-file manifest.

The preceding battle moves snapshot `robopon64-battle-moves-alpha-79D7C6D9.zip.gpg` remains available with its original 459-file manifest.

The preceding interface headings snapshot `robopon64-interface-headings-alpha-212AB2AA.zip.gpg` remains available with its original 477-file manifest.

The preceding Blue Pass snapshot `robopon64-blue-pass-alpha-A1FA9CE0.zip.gpg` remains available with its original 488-file manifest.

The preceding Moon Blue story snapshot `robopon64-moon-blue-story-alpha-A6628793.zip.gpg` remains available with its original 499-file manifest.

The preceding Battler Dome snapshot `robopon64-battler-dome-alpha-93E5FFD1.zip.gpg` remains available with its original 510-file manifest.

The preceding Fire Blue story snapshot `robopon64-fire-blue-story-alpha-07EC747C.zip.gpg` remains available with its original 535-file manifest. Its opening state belongs only to that earlier ROM.

The preceding Fire Blue variants snapshot `robopon64-fire-blue-variants-alpha-9A031850.zip.gpg` remains available with its original 551-file manifest.

The preceding Water Blue story snapshot `robopon64-water-blue-story-alpha-2B41A32E.zip.gpg` remains available with its original 568-file manifest.

The preceding Roulette story snapshot `robopon64-roulette-story-alpha-353AEA96.zip.gpg` remains available with its original 585-file manifest.

The preceding Roulette variants snapshot `robopon64-roulette-variants-alpha-C87382BA.zip.gpg` remains available with its original 602-file manifest.

The preceding Gold Blue story snapshot `robopon64-gold-blue-story-alpha-166993B3.zip.gpg` remains available with its original 619-file manifest.

The preceding Gold Blue variants snapshot `robopon64-gold-blue-variants-alpha-90537926.zip.gpg` remains available with its original 636-file manifest.

The preceding Land Blue story snapshot `robopon64-land-blue-story-alpha-0838AE41.zip.gpg` remains available with its original 653-file manifest.

The preceding Land Blue variants snapshot `robopon64-land-blue-variants-alpha-85BA29DD.zip.gpg` remains available with its original 670-file manifest.

The preceding Sunny Blue rematches snapshot `robopon64-sunny-blue-rematches-alpha-B38C0083.zip.gpg` remains available with its original 687-file manifest.

The preceding Sunny Blue finale snapshot `robopon64-sunny-blue-finale-alpha-4FFCDEDA.zip.gpg` remains available with its original 704-file manifest.

The preceding Sunny Blue variants snapshot `robopon64-sunny-blue-variants-alpha-2E67F751.zip.gpg` remains available with its original 721-file manifest.

The preceding roster names snapshot `robopon64-roster-names-alpha-F386293C.zip.gpg` remains available with its original 743-file manifest.

The preceding bot food snapshot `robopon64-bot-food-alpha-DE539AAB.zip.gpg` remains available with its original 765-file manifest.

The preceding bot interaction snapshot `robopon64-bot-interaction-alpha-83F535F2.zip.gpg` remains available with its original 783-file manifest. Earlier single-file archives use their adjacent ciphertext and plaintext checksums directly.

The preceding bot reactions snapshot `robopon64-bot-reactions-alpha-84DFA87A.zip.gpg.parts.json` remains available with its two ciphertext parts and original 801-file manifest.

The preceding minigame guide snapshot `robopon64-minigame-guide-alpha-207D8DD0.zip.gpg.parts.json` remains available with both ciphertext parts and its original 822-file manifest.

The preceding chore dialogue snapshot `robopon64-chore-dialogue-alpha-40285335.zip.gpg.parts.json` remains available with both ciphertext parts and its original 840-file manifest.

The preceding equipment labels snapshot `robopon64-equipment-labels-alpha-89C91C55.zip.gpg.parts.json` remains available with both ciphertext parts and its original 865-file manifest.

The older bot-book snapshot `robopon64-bot-book-alpha-6AB9FC59.zip.gpg.parts.json` remains available with both ciphertext parts and its original 896-file manifest.

The older late-dialogue snapshot `robopon64-late-dialogue-alpha-DC99F55B.zip.gpg.parts.json` retains its original 933-file manifest; its ciphertext remains recoverable from Git/GitHub.

The preceding book-interface snapshot `robopon64-book-interface-alpha-D85FAF7B.zip.gpg.parts.json` retains its original 964-file manifest; its working ciphertext parts and verified restore are kept.
