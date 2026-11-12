"""Verify and restore a decrypted recovery ZIP into a new directory."""
import argparse
import json
import zipfile
from pathlib import Path, PurePosixPath

from tools.verify_backup import verify


def restore(archive_path, destination):
    count = verify(archive_path)
    destination = Path(destination)
    if destination.exists() or destination.is_symlink():
        raise ValueError('Restore destination must not exist; existing work will not be overwritten')
    with zipfile.ZipFile(archive_path) as archive:
        manifest = json.loads(archive.read('rom-test/BACKUP_MANIFEST.json'))
        for name, meta in manifest['files'].items():
            if meta.get('type', 'file') not in ('file', 'symlink'):
                raise ValueError(f'Unsupported archive entry type: {name}')
            if meta.get('type') == 'symlink':
                link = archive.read(name).decode('utf-8')
                parts = PurePosixPath(link)
                if parts.is_absolute() or '..' in parts.parts or '\\' in link:
                    raise ValueError(f'Unsafe symbolic link: {name}')
        destination.mkdir(parents=True)
        for entry in archive.infolist():
            target = destination / entry.filename
            target.parent.mkdir(parents=True, exist_ok=True)
            data = archive.read(entry)
            meta = manifest['files'].get(entry.filename, {})
            if meta.get('type') == 'symlink':
                target.symlink_to(data.decode('utf-8'))
            else:
                with target.open('xb') as stream:
                    stream.write(data)
                target.chmod((entry.external_attr >> 16) & 0o777 or 0o600)
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive', type=Path)
    parser.add_argument('destination', type=Path, help='A new directory; rom-test/ will be created inside it')
    args = parser.parse_args()
    try:
        count = restore(args.archive, args.destination)
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as error:
        parser.exit(1, f'Restore failed: {error}\n')
    print(f'PASS: verified and restored {count} files into {args.destination}')


if __name__ == '__main__':
    main()
