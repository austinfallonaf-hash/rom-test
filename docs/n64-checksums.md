# Checksum-covered text

Battle strings near `0xC7000` lie in the CIC-6102 checksum input, unlike the
previous simulator milestone. `tools.n64_checksum` computes the two header
words over `[0x1000, 0x101000)`. Repair accepts only this project's big-endian
bootcode (CRC32 `90BB6CB5` over `[0x40, 0x1000)`). It changes only bytes
`0x10..0x17`; the bootcode and other header fields stay intact.

The builders continue to reject edits in that region by default. The cumulative
battle build explicitly requests `--update-checksum`. Each text edit still
requires the exact original ROM hash, source bytes, allocation and display-width
guards. Header/bootcode text edits remain forbidden. This is limited to the
known CIC variant, rather than a general N64 checksum fixer.

Algorithm references used for checking the original arithmetic implementation:

- [Project64 N64Rom.cpp](https://github.com/project64/project64/blob/develop/Source/Project64-core/N64System/N64Rom.cpp),
  `CalculateRomCrc` and `GetCicChipID`.
- [N64 development checksum documentation](https://n64dev.org/n64crc.html).
- [Andreas Sterbenz's chksum64, maintained by rasky](https://github.com/rasky/chksum64/blob/main/chksum64.c),
  used separately in read-only mode as an independent verifier. Its source and
  binary are research tools outside the project/recovery payload.

The calculation reproduces original CRC1/CRC2 `272B690F AD0A7A77`. Unit tests
also use zero, all-one and repeated-word vectors checked against chksum64.
The final battle ROM is checked with the independent utility, and Floating IPS
independently applies the shipped BPS and produces identical bytes.

## Preserve emulator metadata

Mupen normally finds this game's profile by MD5 or header CRC. Changing both
can lose the original EEPROM/Transfer Pak settings. `tools.prepare_emulator`
creates `local/emulator-profiles/<MD5>/` from the supplied bundle's data files,
adding one profile for the target MD5 with its new CRC. It preserves the source
GoodName, two-player setting, `SaveType=Eeprom 16KB` (a 2048-byte/16Kbit EEPROM)
and Transfer Pak flag. It never modifies the supplied database. The launcher
selects this generated directory automatically.

A new ROM still needs a copy of its native save under its own MD5-based filename.
Keep the reference EEPROM unchanged. Cold boot and native saves validate new
builds; an older build's emulator state does not.
