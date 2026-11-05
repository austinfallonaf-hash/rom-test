# Translation research

Latest iteration: [shop alpha](shop-alpha.md).
The first-proof evidence below is retained as the initial baseline.

## Verified input

- Size: 33,554,432 bytes (32 MiB)
- Byte order: big-endian z64 (`80 37 12 40`)
- Header title: `Robopon64`
- Cartridge ID/country: `NR7J`
- Header CRC words: `272B690F AD0A7A77` (read, not independently recalculated)
- SHA-256: `02cda6221c10cba0705f351227e2d6c77e071bdb4f7aa8b5cd3c7c047a2b1881`

## Text evidence

Readable, uncompressed Shift-JIS exists in the supplied ROM. Examples inspected:

| ROM offset | Japanese | Provisional English |
| --- | --- | --- |
| `0x10330C` | いいえ | No |
| `0x10332C` | ロボポンについて | About Robopon |

The surrounding menu region includes yes/no choices and topics relating to
battles, ships, and renaming. Other text contains literal backslash control
sequences including `\N` and `\C000`; their renderer semantics remain unconfirmed.
A first full-ROM scan produced **4,941 unverified candidates**. It is not a full
script dump. Some results include preceding binary bytes that happen to decode;
manual boundary validation and runtime references are essential.

## First translation proof

Graphical emulation works using Xorg's dummy driver on display `:7` and Mesa
llvmpipe with the Rice plugin. Keyboard controls were explicitly configured;
A is left Shift, not `x`. The save-file menu was reached interactively.

| ROM offset | Original | Replacement |
| --- | --- | --- |
| `0x2212D8` | しようする セーブデータを\\Nえらんでください | Select a\\Nsave file. |
| `0x221324` | あたらしいファイル | New File |

The initial ASCII experiment rendered correctly, proving this particular text
path supports English. The shared slot label changes both empty save slots.
The initial instruction auto-wrapped mid-word; an explicit `\\N` line break
was added and visually verified in the final proof. Letter spacing is fixed and fairly wide.

The two replacements fit their original byte budgets and keep their starting
addresses. No relocation or pointer edit was required. The original ROM hash
and all checksum-covered bytes were verified unchanged. The builder emits a
separate ROM copy and an IPS patch; no original ROM modification is performed.

Ten automated tests pass, including exact-source guards, wrong-ROM rejection,
byte-budget rejection, overlapping-edit rejection, and IPS replay. These do not
establish full-game compatibility. The graphical check covers the save menu,
not save creation, loading, gameplay, hardware, or other emulators.

## Next milestones

1. Translate remaining save-menu prompts, choices, and name-entry UI. Determine
   which labels are textures: title labels were not found as plain Shift-JIS.
2. Build a reviewed catalog with per-line width limits and validated control-code
   syntax. Current offsets and extraction candidates are not a complete script.
3. Trace pointers and font advances before expanding text beyond fixed budgets.
4. Test a complete new-game/save/load cycle and then translate the opening scene.
5. Add checksum handling if future edits affect the first MiB of boot-loaded data.

The previous conversation remains inaccessible; this is an independent restart.
