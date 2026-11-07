# Project backup

Latest snapshot: **battle HUD alpha**, including battle status notices, common move components and the reconstructed gardening/simulator work. Coverage: 279 native records, 420 UI strings and 299 native choice blocks. The current source suite has 96 tests. See `docs/battle-hud-alpha.md` for exact runtime coverage and the historical gardening patch's provenance.

`robopon64-battle-hud-alpha-7A9FF097.zip.gpg` contains the original/current ROMs, supplied emulator, current catalogs/tools/tests/docs/patches, documented evidence, historical checkpoints, Python screenshot/input dependencies and preserved native saves.

The archive contains 441 payload files, each verified by size and SHA-256. The
source suite has 96 passing tests, including after a clean restore.

The archive uses AES-256 and the existing recovery passphrase supplied in the project conversation. The passphrase, Git credentials, repository metadata, raw conversation PDF and duplicate historical ROM builds are excluded. Earlier ROMs can be rebuilt from the original and their included cumulative patches.

## Restore

Download the encrypted archive and both adjacent checksum files. In this directory:

```sh
sha256sum -c robopon64-battle-hud-alpha-7A9FF097.zip.gpg.sha256
gpg --output robopon64-battle-hud-alpha-7A9FF097.zip --decrypt robopon64-battle-hud-alpha-7A9FF097.zip.gpg
sha256sum -c robopon64-battle-hud-alpha-7A9FF097.zip.sha256
```

Enter the existing passphrase when prompted. From the latest source checkout, verify and restore into a new directory:

```sh
python tools/verify_backup.py /path/to/robopon64-battle-hud-alpha-7A9FF097.zip
python -m tools.restore_backup /path/to/robopon64-battle-hud-alpha-7A9FF097.zip /path/to/new-directory
```

Follow the restored `rom-test/RESTORE.md` and `RESUME.md`. `BACKUP_MANIFEST.json` records each payload's size and SHA-256. The restore tool preserves executable modes and the emulator library symlink, and refuses an existing destination.

The default native EEPROM remains the verified day-2 file A with 500G, the entered player name and Merlin. It uses the current ROM's `7A9FF097` filename. Separate runtime checkpoints under `local/battle-hud-evidence/` and `local/simulator-evidence/` are test copies, identified by their notes; keep the immutable reference EEPROM intact.

The earlier shop snapshot `robopon64-progress-2026-11-05_135201-PST.zip.gpg` and bed/save snapshot `robopon64-progress-2026-11-05_012741-PST.zip.gpg` remain historical backups. They do not contain the reconstructed simulator milestone. Historical emulator states belong only to their exact ROMs.

The preceding simulator snapshot `robopon64-simulator-alpha-20B19F3D.zip.gpg` remains available with its original 421-file manifest.
