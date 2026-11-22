"""Guarded sprite sources, caption rasterization and program/legacy RAW2 storage."""
import hashlib
import struct
import zlib

TABLE = 0x1980810
FIRST_ID = 0x3F0
DISPATCHER = bytes.fromhex("948800002409524115090004000000008c8600100801efb0248400640801a40a00000000")


def validate_loader(output, entries=()):
    from tools.sprite_program import EXEC_DISPATCHER
    use_program=any(e.get("program") for e in entries)
    if use_program and any(e.get("program") not in ("copy", "hvq_patch") for e in entries):
        raise ValueError("Program and legacy RAW2 sprites cannot share a dispatcher")
    expected=EXEC_DISPATCHER if use_program else DISPATCHER
    if output[0x103C:0x1060] != expected or output[0x56270:0x56274] != bytes.fromhex("0c00010f"):
        raise ValueError("Sprite requires the exact guarded loader dispatcher")

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
        scale = row.get('scale', 1)
        if (type(scale) is not int or scale not in (1, 2) or
                not text or any(c not in FONT for c in text) or
                not 0 <= x0 < x1 <= width or not 0 <= y0 < y1 <= height or
                not 0 <= sample < width or x0 <= sample < x1 or
                len(text)*6*scale > x1-x0 or y1-y0 < 8*scale):
            raise ValueError('Invalid or oversized bitmap caption')
        if any(x0 < b and a < x1 and y0 < d and c < y1 for a,c,b,d in occupied):
            raise ValueError('Overlapping caption rectangles')
        occupied.append((x0,y0,x1,y1))
        for y in range(y0,y1):
            pixel = source[(y*width+sample)*2:(y*width+sample)*2+2]
            output[(y*width+x0)*2:(y*width+x1)*2] = pixel*(x1-x0)
        x = x0+(x1-x0-(len(text)*6-1)*scale)//2
        y = y0+(y1-y0-8*scale)//2
        ink=bytes.fromhex(row.get('ink_hex','fffe'));shadow=bytes.fromhex(row.get('shadow_hex','0000'))
        if len(ink)!=2 or len(shadow)!=2:raise ValueError('Caption colors require RGBA16 words')
        for dy,dx,color in [(1,1,shadow),(0,0,ink)]:
            for index,char in enumerate(text):
                for gy,bits in enumerate(FONT[char]):
                    for gx in range(5):
                        if bits & (16>>gx):
                            for sy in range(scale):
                                for sx in range(scale):
                                    position=((y+(gy+dy)*scale+sy)*width+x+(index*6+gx+dx)*scale+sx)*2
                                    output[position:position+2] = color
    return bytes(output)


def replacement(original, entry, image, entries=()):
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
    if entry.get('program'):
        from tools.sprite_program import payload as program_payload, caption_runs, apply_runs
        if entry['program'] not in ('copy','hvq_patch'):raise ValueError('Unknown sprite program')
        if entry['program']=='hvq_patch' and apply_runs(image,width,height,caption_runs(pixels,width,height,entry['captions']))!=pixels:
            raise ValueError('Sprite caption run proof differs')
        payload=program_payload(blob,pixels,width,height,entry['captions'],copy=entry['program']=='copy')
        destination=int(entry['destination'],0)
        if entry['program']=='hvq_patch':
            owner_id=entry.get('reclaim_resource_id');owners=[e for e in entries if e.get('resource_id')==owner_id]
            # Either program format makes the owner independent of its old blob.
            # The builder validates that owner's replacement and all final overlaps.
            if len(owners)!=1 or owners[0].get('program') not in ('copy','hvq_patch') or owner_id==resource:
                raise ValueError('Reclaimed sprite requires its relocated program owner')
            oi=owner_id-FIRST_ID
            if not 0<=oi<count:raise ValueError('Invalid reclaimed sprite owner')
            oo,osize=struct.unpack_from('>II',original,TABLE+8+8*oi);start=TABLE+relative+oo
            if destination!=start or len(payload)>osize or start%4:
                raise ValueError('Sprite program exceeds reclaimed source allocation')
            if hashlib.sha256(original[start:start+osize]).hexdigest()!=owners[0]['source_blob_sha256']:
                raise ValueError('Reclaimed source hash differs')
            od=int(owners[0]['destination'],0)
            if start<=od<start+osize:raise ValueError('Reclaimed owner was not relocated')
            for ri in range(count):
                ro,rs=struct.unpack_from('>II',original,TABLE+8+8*ri);a=TABLE+relative+ro
                if ri!=oi and start<a+rs and a<start+osize:
                    raise ValueError('Reclaimed sprite source has an alias or overlap')
        elif (destination%16 or destination<0x101000 or destination+len(payload)>len(original) or original[destination:destination+len(payload)]!=b'\xff'*len(payload)):
            raise ValueError('Sprite program copy destination is not unused ROM tail')
        record=struct.pack('>II',destination-TABLE-relative,len(payload))
        return [(descriptor,record),(destination,payload)]
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
