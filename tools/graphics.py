"""Guarded RAW2 sprite replacement and small bitmap captions for the known loader."""
import hashlib
import struct
import zlib

TABLE = 0x1980810
FIRST_ID = 0x3F0
DISPATCHER = bytes.fromhex("948800002409524115090004000000008c8600100801efb0248400640801a40a00000000")


def validate_loader(output):
    if output[0x103C:0x1060] != DISPATCHER or output[0x56270:0x56274] != bytes.fromhex("0c00010f"):
        raise ValueError("RAW2 sprite requires the exact guarded loader dispatcher")

# Original five-by-seven capital letters, stored as rows of five bits.
FONT = dict(zip(' ABCDEFGHIJKLMNOPQRSTUVWXYZ', [
[0,0,0,0,0,0,0], [14,17,17,31,17,17,17], [30,17,17,30,17,17,30],
[14,17,16,16,16,17,14], [30,17,17,17,17,17,30], [31,16,16,30,16,16,31],
[31,16,16,30,16,16,16], [14,17,16,23,17,17,15], [17,17,17,31,17,17,17],
[14,4,4,4,4,4,14], [7,2,2,2,18,18,12], [17,18,20,24,20,18,17],
[16,16,16,16,16,16,31], [17,27,21,21,17,17,17], [17,25,21,19,17,17,17],
[14,17,17,17,17,17,14], [30,17,17,30,16,16,16], [14,17,17,17,21,18,13],
[30,17,17,30,20,18,17], [15,16,16,14,1,1,30], [31,4,4,4,4,4,4],
[17,17,17,17,17,17,14], [17,17,17,17,17,10,4], [17,17,17,21,21,21,10],
[17,17,10,4,10,17,17], [17,17,10,4,4,4,4], [31,1,2,4,8,16,31]]))


def caption_image(source, width, height, captions):
    if len(source) != width*height*2:
        raise ValueError('RGBA16 sprite size differs from dimensions')
    output = bytearray(source)
    occupied = []
    for row in captions:
        x0,y0,x1,y1 = row['rect']
        sample = row['sample_x']
        text = row['translation']
        if (not text or any(c not in FONT for c in text) or
                not 0 <= x0 < x1 <= width or not 0 <= y0 < y1 <= height or
                not 0 <= sample < width or x0 <= sample < x1 or
                len(text)*6 > x1-x0 or y1-y0 < 8):
            raise ValueError('Invalid or oversized bitmap caption')
        if any(x0 < b and a < x1 and y0 < d and c < y1 for a,c,b,d in occupied):
            raise ValueError('Overlapping caption rectangles')
        occupied.append((x0,y0,x1,y1))
        for y in range(y0,y1):
            pixel = source[(y*width+sample)*2:(y*width+sample)*2+2]
            output[(y*width+x0)*2:(y*width+x1)*2] = pixel*(x1-x0)
        x = x0+(x1-x0-(len(text)*6-1))//2
        y = y0+(y1-y0-8)//2
        for dy,dx,color in [(1,1,b'\0\0'),(0,0,b'\xff\xfe')]:
            for index,char in enumerate(text):
                for gy,bits in enumerate(FONT[char]):
                    for gx in range(5):
                        if bits & (16>>gx):
                            position=((y+gy+dy)*width+x+index*6+gx+dx)*2
                            output[position:position+2] = color
    return bytes(output)


def replacement(original, entry, image):
    resource = entry['resource_id']
    count, relative = struct.unpack_from('>II',original,TABLE)
    index = resource-FIRST_ID
    if not 0 <= index < count:
        raise ValueError('Sprite resource outside original directory')
    descriptor = TABLE+8+8*index
    offset,size = struct.unpack_from('>II',original,descriptor)
    source_offset = TABLE+relative+offset
    blob = original[source_offset:source_offset+size]
    if (len(blob) != size or hashlib.sha256(blob).hexdigest() != entry['source_blob_sha256']
            or blob[:8] != b'HVQ2 1.0'):
        raise ValueError('Compressed sprite source differs')
    width,height = struct.unpack_from('>HH',blob,0x16)
    if ([width,height] != entry['dimensions'] or not width or not height or
            width % 64 or height % 32 or blob[0x14:0x16] != b'\x02\x02'):
        raise ValueError('Unexpected sprite dimensions or format')
    encoding = entry.get('image_encoding','raw')
    if encoding == 'zlib':
        try:
            decoder = zlib.decompressobj()
            image = decoder.decompress(image,width*height*2+1)
        except zlib.error as error:
            raise ValueError('Invalid compressed sprite input') from error
        if (not decoder.eof or decoder.unused_data or decoder.unconsumed_tail or
                len(image) != width*height*2):
            raise ValueError('Compressed sprite dimensions or stream differ')
    elif encoding != 'raw':
        raise ValueError('Unknown recovered sprite encoding')
    if hashlib.sha256(image).hexdigest() != entry['image_sha256']:
        raise ValueError('Recovered sprite SHA-256 differs')
    pixels = caption_image(image,width,height,entry['captions'])
    header = bytearray(blob[:100]);header[:4]=b'RAW2'
    struct.pack_into('>I',header,0x10,len(pixels))
    payload = bytes(header)+pixels
    destination = int(entry['destination'],0)
    if (destination % 16 or destination < 0x101000 or
            destination+len(payload)>len(original) or
            original[destination:destination+len(payload)] != b'\xff'*len(payload)):
        raise ValueError('Sprite destination is not the guarded unused ROM tail')
    record = struct.pack('>II',destination-TABLE-relative,len(payload))
    return [(descriptor,record),(destination,payload)]
