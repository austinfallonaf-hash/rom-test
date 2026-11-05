#!/usr/bin/env python3
"""Send a key or capture the research X display (python-xlib and Pillow)."""
import argparse
import time
from pathlib import Path
from Xlib import X, XK, display
from Xlib.ext import xtest
from PIL import Image

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--key', help='X keysym, e.g. Return, x, z, Down, F5')
p.add_argument('--capture', type=Path)
p.add_argument('--hold', type=float, default=.15, help='Key hold in seconds (0.01 to 1)')
a = p.parse_args()
if not .01 <= a.hold <= 1:
    p.error('--hold must be between 0.01 and 1 second')
d = display.Display()
root = d.screen().root
if a.key:
    windows = [w for w in root.query_tree().children
               if 'Mupen64Plus' in (w.get_wm_name() or '') or
               any('mupen64plus' in name.lower() for name in (w.get_wm_class() or ()))]
    if not windows:
        raise SystemExit('No Mupen64Plus window found')
    windows[-1].set_input_focus(X.RevertToParent, X.CurrentTime)
    code = d.keysym_to_keycode(XK.string_to_keysym(a.key))
    if not code:
        raise SystemExit('Unknown key')
    xtest.fake_input(d, X.KeyPress, code)
    d.sync()
    time.sleep(a.hold)
    xtest.fake_input(d, X.KeyRelease, code)
    d.sync()
if a.capture:
    g = root.get_geometry()
    raw = root.get_image(0, 0, g.width, g.height, X.ZPixmap, 0xffffffff)
    if raw.depth != 24:
        raise SystemExit('Capture currently requires the documented 24-bit X display')
    a.capture.parent.mkdir(parents=True, exist_ok=True)
    Image.frombytes('RGB', (g.width, g.height), raw.data, 'raw', 'BGRX').save(a.capture)
d.close()
