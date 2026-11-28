import hashlib
import json
import os
import subprocess
import tempfile
import unittest
import zipfile
from pathlib import Path

from tools.check_workspace import check_upstream
from tools.restore_backup import restore
from tools.verify_backup import verify


class RecoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.archive = self.root / 'checkpoint.zip'

    def write_archive(self, *, changed=False, extra=False, unsafe=False, bad_link=False, duplicate=False):
        payload = {'rom-test/README.md': (b'recovery proof', 'file', 0o644),
                   'rom-test/tool': (b'#!/bin/sh\nexit 0\n', 'file', 0o755),
                   'rom-test/alias': (b'../outside' if bad_link else b'tool', 'symlink', 0o777)}
        if unsafe:
            payload['../outside'] = (b'bad', 'file', 0o644)
        manifest = {'format_version': 1, 'files': {
            name: {'type': kind, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
            for name, (data, kind, mode) in payload.items()}}
        with zipfile.ZipFile(self.archive, 'w') as archive:
            for name, (data, kind, mode) in payload.items():
                entry = zipfile.ZipInfo(name)
                entry.create_system = 3
                entry.external_attr = ((0o120000 if kind == 'symlink' else 0o100000) | mode) << 16
                archive.writestr(entry, b'changed data' if changed and name.endswith('README.md') else data)
            archive.writestr('rom-test/BACKUP_MANIFEST.json', json.dumps(manifest))
            if extra:
                archive.writestr('rom-test/unlisted', b'bad')
            if duplicate:
                import warnings
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore', UserWarning)
                    archive.writestr('rom-test/README.md', b'duplicate')

    def test_restores_files_execute_permission_and_library_style_symlink(self):
        self.write_archive()
        destination = self.root / 'restored'
        self.assertEqual(restore(self.archive, destination), 3)
        self.assertEqual((destination / 'rom-test/README.md').read_bytes(), b'recovery proof')
        self.assertTrue((destination / 'rom-test/tool').stat().st_mode & 0o111)
        self.assertTrue((destination / 'rom-test/alias').is_symlink())
        self.assertEqual((destination / 'rom-test/alias').read_bytes(), (destination / 'rom-test/tool').read_bytes())

    def test_existing_destination_is_preserved(self):
        self.write_archive()
        destination = self.root / 'existing'
        destination.mkdir()
        marker = destination / 'work.txt'
        marker.write_bytes(b'keep my work')
        with self.assertRaisesRegex(ValueError, 'must not exist'):
            restore(self.archive, destination)
        self.assertEqual(marker.read_bytes(), b'keep my work')
        self.assertEqual(list(destination.iterdir()), [marker])

    def test_corrupt_payload_rejected_before_destination_created(self):
        self.write_archive(changed=True)
        destination = self.root / 'restored'
        with self.assertRaisesRegex(ValueError, 'mismatch'):
            restore(self.archive, destination)
        self.assertFalse(destination.exists())

    def test_unlisted_payload_rejected(self):
        self.write_archive(extra=True)
        with self.assertRaisesRegex(ValueError, 'differ'):
            verify(self.archive)

    def test_parent_path_rejected(self):
        self.write_archive(unsafe=True)
        with self.assertRaisesRegex(ValueError, 'Unsafe archive path'):
            verify(self.archive)

    def test_escaping_symlink_rejected_before_destination_created(self):
        self.write_archive(bad_link=True)
        destination = self.root / 'restored'
        with self.assertRaisesRegex(ValueError, 'Unsafe symbolic link'):
            restore(self.archive, destination)
        self.assertFalse(destination.exists())

    def test_duplicate_member_rejected(self):
        self.write_archive(duplicate=True)
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            verify(self.archive)

    def test_new_upstream_commit_requires_checkout_update_not_only_fetch(self):
        upstream, checkout = self.root / 'upstream', self.root / 'checkout'
        env = dict(os.environ, GIT_AUTHOR_NAME='Recovery Test', GIT_AUTHOR_EMAIL='test@example.invalid',
                   GIT_COMMITTER_NAME='Recovery Test', GIT_COMMITTER_EMAIL='test@example.invalid')
        def git(*args, cwd=None):
            return subprocess.run(['git', *args], cwd=cwd, env=env, check=True,
                                  capture_output=True, text=True).stdout.strip()
        git('init', '-b', 'main', str(upstream))
        (upstream / 'proof').write_text('baseline')
        git('add', 'proof', cwd=upstream)
        git('commit', '-m', 'baseline', cwd=upstream)
        git('clone', str(upstream), str(checkout))
        self.assertEqual(check_upstream(checkout, 'origin', 'main'), git('rev-parse', 'HEAD', cwd=upstream))
        (upstream / 'proof').write_text('newer milestone')
        git('commit', '-am', 'new milestone', cwd=upstream)
        with self.assertRaisesRegex(ValueError, 'absent from this checkout'):
            check_upstream(checkout, 'origin', 'main')
        git('fetch', 'origin', 'main', cwd=checkout)
        with self.assertRaisesRegex(ValueError, 'absent from this checkout'):
            check_upstream(checkout, 'origin', 'main')
        git('merge', '--ff-only', 'origin/main', cwd=checkout)
        self.assertEqual(check_upstream(checkout, 'origin', 'main'), git('rev-parse', 'HEAD', cwd=upstream))
