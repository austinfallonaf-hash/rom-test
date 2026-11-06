# Restore this project

The latest private asset snapshot is the shop-alpha encrypted ZIP named in
`backups/README.md`. Verify its encrypted checksum, decrypt it with the existing
recovery passphrase, then verify the decrypted ZIP checksum as documented there.

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

The recovery was tested in a separate empty directory: all 238 archived payload
hashes verified, all 71 tests supplied by that snapshot passed, and its rebuilt
ROM and BPS matched the release exactly. The current source adds eight recovery
tests for a total of 79.
