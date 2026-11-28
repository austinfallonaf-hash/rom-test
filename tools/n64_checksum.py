"""CIC-6102 header checksums for big-endian ROMs; repair only the known bootcode."""
import struct
import zlib

START = 0x1000
END = 0x101000
BOOT_CRC32 = 0x90BB6CB5
MASK = 0xFFFFFFFF


def calculate6102(rom):
    """Compute CRC1/CRC2 over [0x1000, 0x101000) using the 6102 seed."""
    if len(rom) < END or rom[:4] != bytes.fromhex('80371240'):
        raise ValueError('CIC-6102 checksum requires a complete big-endian ROM')
    running = carry = xor_words = rotated_sum = mixed = accumulated = 0xF8CA4DDC
    for (word,) in struct.iter_unpack('>I', rom[START:END]):
        total = (running + word) & MASK
        if total < running:
            carry = (carry + 1) & MASK
        running = total
        xor_words ^= word
        shift = word & 31
        rotated = ((word << shift) | (word >> ((32 - shift) & 31))) & MASK
        rotated_sum = (rotated_sum + rotated) & MASK
        mixed ^= rotated if mixed > word else running ^ word
        accumulated = (accumulated + (rotated_sum ^ word)) & MASK
    return running ^ carry ^ xor_words, rotated_sum ^ mixed ^ accumulated


def repair6102(rom):
    """Return a copy with just header CRC1/CRC2 repaired; reject other bootcodes."""
    if zlib.crc32(rom[0x40:START]) != BOOT_CRC32:
        raise ValueError('Unsupported bootcode for CIC-6102 checksum repair')
    crc = calculate6102(rom)
    result = bytearray(rom)
    struct.pack_into('>II', result, 0x10, *crc)
    return bytes(result)
