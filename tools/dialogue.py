"""Conservative codec for the controls used by the first cabin conversation."""
import re
import struct

# Keep every control and argument in its original order. No unknown command is
# accepted. Glyph indices 0..271 are not command words.
ARGUMENTS = {0x2000: 0, 0x2001: 0, 0x2003: 1, 0x200A: 1, 0x200B: 1}
TOKEN = re.compile(r'\[([0-9A-F]{4})(?::([0-9A-F]{4}))?\]')


def controls(codes):
    result = []
    i = 0
    while i < len(codes):
        word = codes[i]
        i += 1
        if word < 272:
            continue
        if word not in ARGUMENTS:
            raise ValueError(f'Unsupported dialogue control {word:04X}')
        count = ARGUMENTS[word]
        if i+count > len(codes):
            raise ValueError('Truncated dialogue control argument')
        result.append((word, *codes[i:i+count]))
        i += count
    return result


def encode(source_codes, text, *, allow_layout_newlines=False):
    target = []
    position = 0
    cells = 0
    line = 0
    for match in TOKEN.finditer(text):
        chunk = text[position:match.start()]
        for c in chunk:
            if not 32 <= ord(c) <= 126 or c in '[]':
                raise ValueError('Dialogue requires ASCII text and explicit control tokens')
            if line > 2:
                raise ValueError('Dialogue page exceeds three lines')
            target.append(ord(c)-32)
            cells += 1
        if cells > 16:
            raise ValueError('Dialogue line exceeds 16 cells')
        word = int(match[1], 16)
        if word not in ARGUMENTS:
            raise ValueError('Unsupported dialogue control')
        args = [] if match[2] is None else [int(match[2], 16)]
        if len(args) != ARGUMENTS[word]:
            raise ValueError('Wrong dialogue control argument count')
        target.extend([word, *args])
        if word == 0x2000:
            line += 1
            if line > 3:
                raise ValueError('Dialogue page exceeds three lines')
            cells = 0
        elif word == 0x2001:
            line = cells = 0
        elif word == 0x200B:
            if line > 2:
                raise ValueError('Dialogue page exceeds three lines')
            cells += 5  # Original name-entry capacity; room for player name.
        position = match.end()
    for c in text[position:]:
        if not 32 <= ord(c) <= 126 or c in '[]':
            raise ValueError('Dialogue requires ASCII text and explicit control tokens')
        if line > 2:
            raise ValueError('Dialogue page exceeds three lines')
        target.append(ord(c)-32)
        cells += 1
    if cells > 16:
        raise ValueError('Dialogue line exceeds 16 cells')
    expected, actual = controls(source_codes), controls(target)
    if allow_layout_newlines:
        # Existing controls must form a subsequence. The only permitted extra
        # word is a line break; page, portrait, color and variable controls stay.
        index = 0
        for command in actual:
            if index < len(expected) and command == expected[index]:
                index += 1
            elif command != (0x2000,):
                raise ValueError('Dialogue control words or arguments changed')
        if index != len(expected):
            raise ValueError('Dialogue control words or arguments changed')
    elif actual != expected:
        raise ValueError('Dialogue control words or arguments changed')
    if len(target) > len(source_codes):
        raise ValueError('Dialogue exceeds original record budget')
    return struct.pack('>'+'H'*len(target), *target)


def render(codes, glyphs):
    out = []
    i = 0
    while i < len(codes):
        c = codes[i]
        i += 1
        if c < len(glyphs):
            out.append(glyphs[c])
        else:
            if c not in ARGUMENTS:
                raise ValueError('Unsupported control in render')
            n = ARGUMENTS[c]
            args = codes[i:i+n]
            if len(args) != n:
                raise ValueError('Truncated control')
            out.append('[' + ':'.join(f'{v:04X}' for v in [c, *args]) + ']')
            i += n
    return ''.join(out)
