"""Generate an isolated Mupen data directory preserving the original save profile."""
import argparse
import hashlib
import re
import shutil
import struct
from pathlib import Path

from tools.rom_text import EXPECTED_SHA256


def prepare(rom_path, original_path, bundle, output):
    rom_path, original_path, bundle, output = map(Path, (rom_path, original_path, bundle, output))
    source, target = original_path.read_bytes(), rom_path.read_bytes()
    if hashlib.sha256(source).hexdigest() != EXPECTED_SHA256:
        raise ValueError('Emulator profile requires the exact original ROM')
    if (len(source) != len(target) or source[:0x10] != target[:0x10]
            or source[0x18:0x1000] != target[0x18:0x1000]):
        raise ValueError('ROM header/bootcode does not belong to this project')
    source_md5, target_md5 = (hashlib.md5(data).hexdigest().upper() for data in (source, target))
    if source_md5 == target_md5:
        return bundle.resolve()
    database = (bundle/'mupen64plus.ini').read_text()
    section = re.search(r'(?ms)^\['+source_md5+r'\]\s*\n(.*?)(?=^\[|\Z)', database)
    if section is None:
        raise ValueError('Original game metadata is absent from the supplied emulator database')
    body = section[1]
    if not re.search(r'(?m)^SaveType=Eeprom 16KB\s*$', body):
        raise ValueError('Original 16Kbit EEPROM profile was not found')
    crc1, crc2 = struct.unpack_from('>II', target, 0x10)
    body, replacements = re.subn(r'(?m)^CRC=.*$', f'CRC={crc1:08X} {crc2:08X}', body)
    if replacements != 1:
        raise ValueError('Original game profile has no unique CRC entry')
    # Avoid duplicate records if a generated or previously recognized MD5 is present.
    database = re.sub(r'(?ms)^\['+target_md5+r'\]\s*\n.*?(?=^\[|\Z)', '', database)
    directory = output/target_md5
    directory.mkdir(parents=True, exist_ok=True)
    for path in bundle.iterdir():
        if path.is_file() and path.suffix.lower() in ('.ini', '.ttf', '.txt') and path.name != 'mupen64plus.ini':
            shutil.copyfile(path, directory/path.name)
    (directory/'mupen64plus.ini').write_text(f'[{target_md5}]\n{body.rstrip()}\n\n'+database)
    return directory.resolve()


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('rom', type=Path)
    parser.add_argument('--original', type=Path, default=root/'local/original.z64')
    parser.add_argument('--bundle', type=Path, default=root/'local/mupen64plus-bundle-linux64-2.6.0')
    parser.add_argument('--output', type=Path, default=root/'local/emulator-profiles')
    args = parser.parse_args()
    try:
        directory = prepare(args.rom, args.original, args.bundle, args.output)
    except (OSError, ValueError) as error:
        parser.exit(1, f'Could not prepare emulator data: {error}\n')
    print(directory)


if __name__ == '__main__':
    main()
