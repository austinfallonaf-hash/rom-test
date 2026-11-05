"""BPS1 writer using SourceRead and TargetRead; supports the full 32 MiB ROM."""
import struct
import zlib


def number(n):
    if n < 0:
        raise ValueError('BPS integers are unsigned')
    out = bytearray()
    while True:
        digit = n & 127
        n >>= 7
        if n == 0:
            out.append(digit | 128)
            return bytes(out)
        out.append(digit)
        n -= 1


def make_patch(source, target, spans):
    if len(source) != len(target):
        raise ValueError('This writer requires equal ROM sizes')
    patch = bytearray(b'BPS1' + number(len(source)) + number(len(target)) + number(0))
    position = 0
    for start, end in sorted(spans):
        if start < position or not start < end <= len(target):
            raise ValueError('Overlapping or invalid patch ranges')
        if start > position:
            if source[position:start] != target[position:start]:
                raise ValueError('Unrecorded changes outside patch ranges')
            patch.extend(number(((start-position-1) << 2) | 0))
        patch.extend(number(((end-start-1) << 2) | 1))
        patch.extend(target[start:end])
        position = end
    if position < len(target):
        if source[position:] != target[position:]:
            raise ValueError('Unrecorded changes after patch ranges')
        patch.extend(number(((len(target)-position-1) << 2) | 0))
    patch.extend(struct.pack('<II', zlib.crc32(source), zlib.crc32(target)))
    patch.extend(struct.pack('<I', zlib.crc32(patch)))
    return bytes(patch)
