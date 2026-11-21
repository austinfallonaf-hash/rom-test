"""Read-only verification of the current translation and optional native save."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

from tools.build_story import build_story

ROOT = Path(__file__).resolve().parents[1]


def check_bytes(data, expected, label):
    if len(data) != expected['bytes'] or hashlib.sha256(data).hexdigest() != expected['sha256']:
        raise ValueError(f'{label}: size or SHA-256 mismatch')


def check_upstream(root, remote, branch):
    result = subprocess.run(['git', 'ls-remote', '--exit-code', remote, f'refs/heads/{branch}'],
                            cwd=root, capture_output=True, text=True)
    if result.returncode or not result.stdout.strip():
        raise ValueError('Could not verify upstream freshness; fetch and compare before continuing')
    head = result.stdout.split()[0]
    included = subprocess.run(['git', 'merge-base', '--is-ancestor', head, 'HEAD'],
                              cwd=root, capture_output=True)
    if included.returncode:
        raise ValueError(f'Upstream {branch} at {head[:12]} is absent from this checkout. '
                         f'Fetch {remote} {branch} and compare before continuing')
    return head


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--require-save', action='store_true', help='Also require the preserved day-2 EEPROM')
    parser.add_argument('--check-remote', action='store_true', help='Fail if upstream has changes absent from this checkout')
    args = parser.parse_args()
    try:
        state = json.loads((ROOT / 'PROJECT_STATE.json').read_text())
        if args.check_remote:
            remote = state['upstream']['remote']
            branch = state['upstream']['branch']
            head = check_upstream(ROOT, remote, branch)
            print(f'PASS: upstream {branch} at {head[:12]} is included in this checkout')
        manifest = json.loads((ROOT / state['release_manifest']).read_text())
        original = (ROOT / 'local/original.z64').read_bytes()
        check_bytes(original, manifest['files']['source'], 'Original ROM')
        catalogs = state['catalogs']
        menu = json.loads((ROOT / catalogs['menu']).read_text())['entries']
        story = json.loads((ROOT / catalogs['story']).read_text())['records']
        choices = json.loads((ROOT / catalogs['choices']).read_text())['entries']
        layout = json.loads((ROOT / catalogs['layout']).read_text())['entries'] if catalogs.get('layout') else []
        graphics = json.loads((ROOT/catalogs['graphics']).read_text())['entries'] if catalogs.get('graphics') else []
        images = {e['image_path']:(ROOT/e['image_path']).read_bytes() for e in graphics}
        target, patch = build_story(original, menu, story, choices, layout,
                                    update_checksum=state.get('update_checksum', False),
                                    validate_moves=state.get('validate_move_names', False),
                                    graphics=graphics, graphic_images=images)
        check_bytes(target, manifest['files']['target'], 'Rebuilt ROM')
        check_bytes(patch, manifest['files']['patch'], 'Rebuilt patch')
        if patch != (ROOT / state['release_patch']).read_bytes():
            raise ValueError('Release patch differs from rebuilt patch')
        current = ROOT / state['playable_rom']
        if current.exists():
            check_bytes(current.read_bytes(), manifest['files']['target'], 'Local playable ROM')
        print(f'PASS: exact source, {len(story)} native records, {len(menu)} UI strings, {len(choices)} choice blocks')
        if graphics:
            print(f'PASS: {len(graphics)} guarded sprite replacement(s), '
                  f"{sum(len(e['captions']) for e in graphics)} bitmap captions")
        print('PASS: reproducible target and shipped BPS patch; original unchanged')
        save = state['native_save']
        save_path = ROOT / save['path']
        if save_path.exists():
            check_bytes(save_path.read_bytes(), save, 'Preserved day-2 EEPROM')
            print('PASS: preserved day-2 EEPROM hash')
        elif args.require_save:
            raise FileNotFoundError(f'Missing preserved save: {save_path}')
        else:
            print('Native save absent; use --require-save when verifying a full recovery archive')
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f'Workspace verification failed: {error}\n')


if __name__ == '__main__':
    main()
