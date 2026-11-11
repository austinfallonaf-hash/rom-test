# Project backup

Latest snapshot: **Fire Blue variants alpha**, including both Black Musketeers interludes,
Mikachi recruitment and gifts, alternate Fire Blue story and regional hints, plus
all earlier work. Coverage: 1,189 native records, 832 UI strings, 299 choice blocks
and three bitmap captions. The source suite has 115 tests. See
`docs/fire-blue-variants-alpha.md` for precise validation scope.

`robopon64-fire-blue-variants-alpha-9A031850.zip.gpg` contains the original/current
ROMs, supplied emulator, current catalogs/tools/tests/docs/patches, native-A
runtime evidence, historical evidence/checkpoints, screenshot/input dependencies
and preserved native saves. It includes the current exact-ROM emulator profile.

The archive contains 551 payload files, each verified by size and SHA-256. The
source suite passes all 115 tests, including after a clean restore.

The archive uses AES-256 and the existing recovery passphrase supplied in the project conversation. The passphrase, Git credentials, repository metadata, raw conversation PDF and duplicate historical ROM builds are excluded. Earlier ROMs can be rebuilt from the original and their included cumulative patches.

## Restore

Download the encrypted archive and both adjacent checksum files. In this directory:

```sh
sha256sum -c robopon64-fire-blue-variants-alpha-9A031850.zip.gpg.sha256
gpg --output robopon64-fire-blue-variants-alpha-9A031850.zip --decrypt robopon64-fire-blue-variants-alpha-9A031850.zip.gpg
sha256sum -c robopon64-fire-blue-variants-alpha-9A031850.zip.sha256
```

Enter the existing passphrase when prompted. From the latest source checkout, verify and restore into a new directory:

```sh
python tools/verify_backup.py /path/to/robopon64-fire-blue-variants-alpha-9A031850.zip
python -m tools.restore_backup /path/to/robopon64-fire-blue-variants-alpha-9A031850.zip /path/to/new-directory
```

Follow the restored `rom-test/RESTORE.md` and `RESUME.md`. `BACKUP_MANIFEST.json` records each payload's size and SHA-256. The restore tool preserves executable modes and the emulator library symlink, and refuses an existing destination.

The default native EEPROM remains the verified day-2 file A with 500G, the entered player name and Merlin. It uses the current ROM's `9A031850` filename. Separate runtime checkpoints under `local/fire-blue-variants-evidence/`, `local/fire-blue-story-evidence/`, `local/battler-dome-evidence/`, `local/moon-blue-story-evidence/`, `local/blue-pass-evidence/`, `local/interface-headings-evidence/`, `local/battle-moves-evidence/`, `local/battle-hud-evidence/` and `local/simulator-evidence/` are test copies, identified by their notes; keep the immutable reference EEPROM intact.

The earlier shop snapshot `robopon64-progress-2026-11-05_135201-PST.zip.gpg` and bed/save snapshot `robopon64-progress-2026-11-05_012741-PST.zip.gpg` remain historical backups. They do not contain the reconstructed simulator milestone. Historical emulator states belong only to their exact ROMs.

The preceding simulator snapshot `robopon64-simulator-alpha-20B19F3D.zip.gpg` remains available with its original 421-file manifest.

The preceding battle HUD snapshot `robopon64-battle-hud-alpha-7A9FF097.zip.gpg` remains available with its original 441-file manifest.

The preceding battle moves snapshot `robopon64-battle-moves-alpha-79D7C6D9.zip.gpg` remains available with its original 459-file manifest.

The preceding interface headings snapshot `robopon64-interface-headings-alpha-212AB2AA.zip.gpg` remains available with its original 477-file manifest.

The preceding Blue Pass snapshot `robopon64-blue-pass-alpha-A1FA9CE0.zip.gpg` remains available with its original 488-file manifest.

The preceding Moon Blue story snapshot `robopon64-moon-blue-story-alpha-A6628793.zip.gpg` remains available with its original 499-file manifest.

The preceding Battler Dome snapshot `robopon64-battler-dome-alpha-93E5FFD1.zip.gpg` remains available with its original 510-file manifest.

The preceding Fire Blue story snapshot `robopon64-fire-blue-story-alpha-07EC747C.zip.gpg` remains available with its original 535-file manifest. Its opening state belongs only to that earlier ROM.
