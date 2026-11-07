"""Verify every file in a project recovery ZIP without extracting or executing it."""
import argparse
import hashlib
import json
import zipfile
from pathlib import PurePosixPath


def verify(path):
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)):
            raise ValueError('Duplicate archive members')
        for name in names:
            parts = PurePosixPath(name)
            if parts.is_absolute() or '..' in parts.parts or '\\' in name:
                raise ValueError(f'Unsafe archive path: {name}')
        manifest_name = 'rom-test/BACKUP_MANIFEST.json'
        manifest = json.loads(archive.read(manifest_name))
        if manifest['format_version'] != 1:
            raise ValueError('Unsupported manifest version')
        expected = manifest['files']
        if set(names) != set(expected) | {manifest_name}:
            raise ValueError('Archive members differ from the manifest')
        for name, meta in expected.items():
            data = archive.read(name)
            if len(data) != meta['bytes'] or hashlib.sha256(data).hexdigest() != meta['sha256']:
                raise ValueError(f'Hash or size mismatch: {name}')
        return len(expected)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive')
    args = parser.parse_args()
    try:
        count = verify(args.archive)
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as error:
        parser.exit(1, f'Backup verification failed: {error}\n')
    print(f'PASS: {count} archived files match their SHA-256 hashes and sizes')


if __name__ == '__main__':
    main()
