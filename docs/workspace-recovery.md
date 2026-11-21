# Verified cloud-workspace recovery

The cloud filesystem resumed at bed/save commit `ea7c7d3`, but the repository's
main branch was at shop commit `b6b2202`. Its newer care, battle, Moon Blue and
shop work had not reached the local checkout. Recovery checked the remote before
publishing any changes and continued from the newer source. Experimental work
against the older milestone remains on a separate local branch and was not
merged into the current translation.

The latest encrypted backup's checksum verified. The existing recovery key
decrypted it without exposing the key or adding it to Git. The decrypted ZIP
checksum, ZIP CRCs and all 238 payload hashes verified. Private assets were
restored into ignored `local/`; the source is based on current main. The current
shop ROM and BPS rebuilt byte-for-byte, and the preserved day-2 EEPROM is
unchanged. All 71 tests provided by the shop snapshot passed.

A second restore into a new empty directory verified preservation of the
emulator's executable permissions and library symlink. The restored ROM, patch
and EEPROM matched the current files. Rebuilding with the restored tools and
catalogs reproduced the release.

The new recovery tools address the failure modes observed here:

- `PROJECT_STATE.json` records the current release, catalogs, private assets and
  source checkpoint; `RESUME.md` supplies the human-readable handoff.
- `tools.check_workspace --check-remote` rejects an upstream commit that is not
  included in local HEAD, including after the commit has merely been fetched.
  It verifies the in-memory rebuild and shipped patch against the release
  manifest and can require the preserved EEPROM.
- `tools/verify_backup.py` rejects corrupt, duplicate, unlisted or unsafe archive
  members and checks every payload size and SHA-256 without extracting it.
- `tools.restore_backup` verifies first, requires a new destination and preserves
  executable permissions and safe relative symbolic links.
- The emulator launcher keeps native saves and states under ignored project
  directories instead of the default home-directory location. Existing home
  saves are not automatically migrated.

Eight new tests exercise real failure cases: a newer upstream commit absent
from the checkout, preservation of existing destination data, corrupted payload,
unlisted and duplicate members, unsafe paths/links, and restored permissions and
symlinks. The complete current suite has 79 passing tests.

This iteration does not change the shop translation, release ROM, save format
or game logic. Runtime coverage and outstanding translation work remain those
documented in `shop-alpha.md`. The next concrete issue is the sell-category
panel's Parts label extending beyond its frame.
