# Project backup

The dated encrypted archive preserves the full translation workspace at the
bed/save alpha milestone, including original/current ROMs, the supplied Linux
emulator, all source catalogs/tools/tests/docs, all patches, 34 documented
screenshots, historical checkpoints and the verified day-2 EEPROM save.

The project source and release patches are also available directly in this
repository. ROM images and private save data are contained only in the encrypted
archive. The recovery passphrase is supplied separately in the project chat.

## Restore the full backup

Download the `.zip.gpg` file and its checksum files using GitHub's download
button, or clone this repository. With GnuPG installed, run in this directory:

```sh
sha256sum -c robopon64-progress-2026-11-05_012741-PST.zip.gpg.sha256
gpg --output robopon64-progress-2026-11-05_012741-PST.zip --decrypt robopon64-progress-2026-11-05_012741-PST.zip.gpg
sha256sum -c robopon64-progress-2026-11-05_012741-PST.zip.sha256
```

Enter the recovery passphrase when prompted. Extract the resulting ZIP and
follow `rom-test/RESTORE.md`. Its `BACKUP_MANIFEST.json` contains per-file hashes.
The archive was verified before encryption, and decrypting this encrypted copy
was verified to reproduce the original ZIP byte-for-byte.

The backup was created on November 5, 2026, at 1:27 a.m. Pacific time.
The day-2 EEPROM corresponds to the included ROM's MD5 prefix `793AFD73`.
