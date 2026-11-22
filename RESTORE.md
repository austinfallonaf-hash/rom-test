# Restore this project

The latest private asset snapshot is the parts-graphics-alpha split encrypted ZIP
named in `backups/README.md`. Download both parts and the index/checksum files.
Verify the part hashes, concatenate .part001 then .part002, verify the whole
ciphertext hash, decrypt with the existing recovery passphrase, then verify the
ZIP hash. `PROJECT_STATE.latest_encrypted_backup` points to the parts JSON index.
The exact commands are in `backups/README.md`.

Using the latest source checkout, run:

```sh
python tools/verify_backup.py /path/to/decrypted.zip
python -m tools.restore_backup /path/to/decrypted.zip /path/to/new-directory
```

The restore destination must not exist. The tool verifies all archive members
before creating it, preserves executable permissions and symbolic links, and
does not overwrite an existing workspace. The archive creates `rom-test/` within
the chosen directory. Git credentials and metadata are not archived.

The restored snapshot includes its original source. Keep the latest source
checkout and compare versions before moving restored private assets into it.
For the current checkpoint those assets live under ignored `local/`.

Follow `RESUME.md` for the current catalogs, native save and emulator setup.
Run `python -m tools.check_workspace --require-save` on the current source plus
restored assets, and `python -m unittest discover -s tests -q`.
Add `--check-remote` when Git metadata and network access are available.

Recovery is tested in a separate empty directory, including executable modes
and the emulator library symlink. The current source has 164 tests and verifies
the parts-graphics-alpha ROM/BPS and reference EEPROM against the recorded hashes.
The earlier shop snapshot remains a historical backup with 238 payload files
and its original 71-test source suite.

A space-limited Git checkout may omit historical encrypted backup working
copies with non-cone sparse checkout. All older snapshots remain in local Git
and on the canonical GitHub branch. The current/preceding parts are present;
backups/README.md gives exact patterns and commands to retrieve an older file
or restore the full tracked tree. Original/private assets are not removed by
these patterns. The ZIP excludes Git metadata, so a plain restored directory
does not inherit the checkout configuration.
