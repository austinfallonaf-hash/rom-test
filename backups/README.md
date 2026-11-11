# Project backup

Latest snapshot: **Moon Blue story alpha**, including Sharol, Dean, Godoshii and Johnny, their key/treasure rewards, the coaster route toward Fire Blue and all earlier work. Coverage: 618 native records, 832 UI strings, 299 choice blocks and three bitmap captions. The source suite has 108 tests. See `docs/moon-blue-story-alpha.md` for validation limits; new branches await playthrough verification.

`robopon64-moon-blue-story-alpha-A6628793.zip.gpg` contains the original/current ROMs, supplied emulator, current catalogs/tools/tests/docs/patches, documented evidence, historical checkpoints, Python screenshot/input dependencies and preserved native saves.

The archive contains 499 payload files, each verified by size and SHA-256. The
source suite passes all 108 tests, including after a clean restore.

The archive uses AES-256 and the existing recovery passphrase supplied in the project conversation. The passphrase, Git credentials, repository metadata, raw conversation PDF and duplicate historical ROM builds are excluded. Earlier ROMs can be rebuilt from the original and their included cumulative patches.

## Restore

Download the encrypted archive and both adjacent checksum files. In this directory:

```sh
sha256sum -c robopon64-moon-blue-story-alpha-A6628793.zip.gpg.sha256
gpg --output robopon64-moon-blue-story-alpha-A6628793.zip --decrypt robopon64-moon-blue-story-alpha-A6628793.zip.gpg
sha256sum -c robopon64-moon-blue-story-alpha-A6628793.zip.sha256
```

Enter the existing passphrase when prompted. From the latest source checkout, verify and restore into a new directory:

```sh
python tools/verify_backup.py /path/to/robopon64-moon-blue-story-alpha-A6628793.zip
python -m tools.restore_backup /path/to/robopon64-moon-blue-story-alpha-A6628793.zip /path/to/new-directory
```

Follow the restored `rom-test/RESTORE.md` and `RESUME.md`. `BACKUP_MANIFEST.json` records each payload's size and SHA-256. The restore tool preserves executable modes and the emulator library symlink, and refuses an existing destination.

The default native EEPROM remains the verified day-2 file A with 500G, the entered player name and Merlin. It uses the current ROM's `A6628793` filename. Separate runtime checkpoints under `local/moon-blue-story-evidence/`, `local/blue-pass-evidence/`, `local/interface-headings-evidence/`, `local/battle-moves-evidence/`, `local/battle-hud-evidence/` and `local/simulator-evidence/` are test copies, identified by their notes; keep the immutable reference EEPROM intact.

The earlier shop snapshot `robopon64-progress-2026-11-05_135201-PST.zip.gpg` and bed/save snapshot `robopon64-progress-2026-11-05_012741-PST.zip.gpg` remain historical backups. They do not contain the reconstructed simulator milestone. Historical emulator states belong only to their exact ROMs.

The preceding simulator snapshot `robopon64-simulator-alpha-20B19F3D.zip.gpg` remains available with its original 421-file manifest.

The preceding battle HUD snapshot `robopon64-battle-hud-alpha-7A9FF097.zip.gpg` remains available with its original 441-file manifest.

The preceding battle moves snapshot `robopon64-battle-moves-alpha-79D7C6D9.zip.gpg` remains available with its original 459-file manifest.

The preceding interface headings snapshot `robopon64-interface-headings-alpha-212AB2AA.zip.gpg` remains available with its original 477-file manifest.

The preceding Blue Pass snapshot `robopon64-blue-pass-alpha-A1FA9CE0.zip.gpg` remains available with its original 488-file manifest.
