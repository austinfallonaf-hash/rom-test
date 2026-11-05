# Project backup

Latest snapshot: **shop alpha**, created November 05, 2026 at 01:52 PM PST.
Coverage: 220 native records, 185 UI strings and 299 native choice blocks.
All 71 automated tests pass. See `docs/shop-alpha.md` for runtime coverage.

`robopon64-progress-2026-11-05_135201-PST.zip.gpg` is a full restore snapshot, including original/current ROMs,
the supplied emulator, current catalogs/tools/tests/docs/patches, documented
screenshots, historical checkpoints and the verified native day-2 save.
Git metadata, credentials, dependency caches and duplicate intermediate ROMs
are omitted. Source and patch files are also available directly in the repo.

The archive uses the same recovery passphrase supplied separately for the
previous backup. The passphrase is not stored in this repository.

## Restore

Download the encrypted archive and both adjacent checksum files. Run:

```sh
sha256sum -c robopon64-progress-2026-11-05_135201-PST.zip.gpg.sha256
gpg --output robopon64-progress-2026-11-05_135201-PST.zip --decrypt robopon64-progress-2026-11-05_135201-PST.zip.gpg
sha256sum -c robopon64-progress-2026-11-05_135201-PST.zip.sha256
```

Enter the existing recovery passphrase when prompted. Extract the ZIP and follow
`rom-test/RESTORE.md`. `BACKUP_MANIFEST.json` lists per-file hashes. The ZIP was
checked for corruption and every manifest entry verified. Independent patch
application and a rebuild from the archived source/catalogs reproduce the
included current ROM. Decrypting the encrypted copy reproduces the ZIP exactly.

The included current ROM has MD5 prefix `EE13E958`. Its native EEPROM loads
file A at day 2, 500G, with the entered player name and Merlin. A same-build
checkpoint, if included, is for that exact ROM only; new patches require cold
boots for verification.

The earlier bed/save snapshot `robopon64-progress-2026-11-05_012741-PST.zip.gpg`
is retained as a historical backup. It is not required to restore this snapshot.
