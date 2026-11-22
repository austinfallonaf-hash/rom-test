"""Small resource-local MIPS programs for copy and caption-only HVQ patches.

Programs execute from the uncached RDRAM alias of the freshly loaded resource.
The original HVQ decoder and the existing image allocation/tile/cache path stay
in use. No general code or data relocation is supported.
"""
import struct

EXEC_HEADER = bytes.fromhex('1000001800000000')  # beq zero,zero,+24; nop -> +100
EXEC_DISPATCHER = bytes.fromhex('9488000024094856110900043c0820000088c82503200008000000000801a40a00000000')
COPY_PROGRAM = bytes.fromhex('8c8600100801efb024840070')


class _Code:
    def __init__(self): self.words=[]; self.labels={}; self.fixups=[]
    def word(self, value): self.words.append(value)
    def i(self, op, rt, rs, imm): self.word(op<<26 | rs<<21 | rt<<16 | (imm&65535))
    def r(self, fn, rd, rs, rt, shift=0): self.word(rs<<21 | rt<<16 | rd<<11 | shift<<6 | fn)
    def label(self, name): self.labels[name]=len(self.words)
    def bne(self, rs, rt, label):
        self.fixups.append((len(self.words),label));self.i(5,rt,rs,0)
    def done(self):
        for pos,label in self.fixups:
            delta=self.labels[label]-pos-1
            if not -32768<=delta<32768:raise ValueError('Sprite branch exceeds range')
            self.words[pos]|=delta&65535
        return b''.join(struct.pack('>I',w) for w in self.words)


def patch_code(hvq_offset, patch_offset, width, *, palette=False):
    if not 100<=hvq_offset<=32767 or not hvq_offset<=patch_offset<=32767 or not 1<=width<=16383:
        raise ValueError('Sprite program offsets/stride exceed immediate range')
    c=_Code();c.i(9,29,29,-40)
    for reg,off in [(31,36),(16,32),(17,28),(18,24),(19,20),(20,16)]:c.i(43,reg,29,off)
    c.r(33,16,4,0);c.r(33,17,5,0)  # s0=input header, s1=output
    c.i(15,25,0,0x8006);c.i(13,25,25,0x9028)  # cached original HVQ decoder
    c.r(9,31,25,0);c.i(9,4,16,hvq_offset)  # jalr t9; delay: a0=embedded HVQ
    c.i(9,18,16,patch_offset);c.i(35,19,18,0);c.i(9,18,18,4)
    c.label('rect');c.i(35,8,18,0);c.r(33,20,17,8)
    c.i(37,9,18,4);c.i(37,10,18,6)
    if palette:
        # The HVQ call has returned; the frame's argument area holds row colors.
        c.i(37,14,18,8);c.i(41,14,29,2);c.i(37,14,18,10);c.i(41,14,29,4)
    c.i(9,18,18,12 if palette else 8)
    c.label('row')
    if palette:
        # Run counts can leave the next background word at an odd input address.
        c.i(36,14,18,0);c.i(36,15,18,1);c.r(0,14,0,14,8);c.r(37,14,14,15)
        c.i(41,14,29,0);c.i(9,18,18,2)
    c.r(33,11,20,0);c.r(33,12,9,0)
    c.label('run');c.i(36,13,18,0)
    if palette:
        c.r(2,14,0,13,6);c.r(0,14,0,14,1);c.r(33,14,29,14)
        c.i(37,14,14,0);c.i(12,13,13,63);c.i(9,18,18,1)
    else:
        c.i(36,14,18,1);c.i(36,15,18,2)
        c.r(0,14,0,14,8);c.r(37,14,14,15);c.i(9,18,18,3)
    c.r(35,12,12,13)
    c.label('pixel');c.i(41,14,11,0);c.i(9,11,11,2);c.i(9,13,13,-1)
    c.bne(13,0,'pixel');c.word(0);c.bne(12,0,'run');c.word(0)
    c.i(9,20,20,width*2);c.i(9,10,10,-1);c.bne(10,0,'row');c.word(0)
    c.i(9,18,18,3);c.i(9,8,0,-4);c.r(36,18,18,8)  # align next rect to four bytes
    c.i(9,19,19,-1);c.bne(19,0,'rect');c.word(0)
    for reg,off in [(20,16),(19,20),(18,24),(17,28),(16,32),(31,36)]:c.i(35,reg,29,off)
    c.r(8,0,31,0);c.i(9,29,29,40)
    return c.done()


def caption_runs(pixels, width, height, captions):
    if not captions or len(pixels)!=width*height*2:raise ValueError('Sprite patch needs pixels and captions')
    data=bytearray(struct.pack('>I',len(captions)))
    for row in captions:
        x0,y0,x1,y1=row['rect']
        if not 0<=x0<x1<=width or not 0<=y0<y1<=height or x1-x0>255:
            raise ValueError('Caption run rectangle outside image')
        while len(data)%4:data.append(0)
        data+=struct.pack('>IHH',2*(y0*width+x0),x1-x0,y1-y0)
        for y in range(y0,y1):
            x=x0
            while x<x1:
                color=pixels[2*(y*width+x):2*(y*width+x)+2];n=1
                while x+n<x1 and pixels[2*(y*width+x+n):2*(y*width+x+n)+2]==color:n+=1
                data.append(n);data+=color;x+=n
    while len(data)%4:data.append(0)
    return bytes(data)


def apply_runs(source,width,height,stream):
    """Independent checked stream decoder, also used to verify generated payloads."""
    output=bytearray(source)
    if len(source)!=width*height*2 or len(stream)<4:raise ValueError('Invalid patch image/stream')
    count=struct.unpack_from('>I',stream)[0];p=4
    if not 1<=count<=64:raise ValueError('Invalid patch rectangle count')
    for _ in range(count):
        p=(p+3)&~3
        if p+8>len(stream):raise ValueError('Truncated patch rectangle')
        off,w,h=struct.unpack_from('>IHH',stream,p);p+=8
        if off%2 or not 1<=w<=255 or h<1 or (off//2)%width+w>width or off+2*((h-1)*width+w)>len(output):raise ValueError('Patch rectangle outside output')
        for y in range(h):
            left=w;dst=off+2*y*width
            while left:
                if p+3>len(stream):raise ValueError('Truncated patch run')
                n=stream[p];color=stream[p+1:p+3];p+=3
                if n<1 or n>left:raise ValueError('Invalid patch run length')
                output[dst:dst+n*2]=color*n;dst+=n*2;left-=n
    if any(stream[p:]) or len(stream)-p>3:raise ValueError('Unexpected patch trailing data')
    return bytes(output)


def caption_palette(source, pixels, width, height, captions):
    """One-byte runs: two-bit row-palette index and a 1..63 pixel length."""
    if not 1<=len(captions)<=64 or len(source)!=width*height*2 or len(pixels)!=len(source):
        raise ValueError('Palette patch needs source, pixels and captions')
    data=bytearray(struct.pack('>I',len(captions)))
    for row in captions:
        x0,y0,x1,y1=row['rect'];sample=row['sample_x']
        if not 0<=x0<x1<=width or not 0<=y0<y1<=height or x1-x0>255 or not 0<=sample<width or x0<=sample<x1:
            raise ValueError('Palette rectangle/sample outside image')
        ink=bytes.fromhex(row.get('ink_hex','fffe'));shadow=bytes.fromhex(row.get('shadow_hex','0000'))
        if len(ink)!=2 or len(shadow)!=2:raise ValueError('Palette colors require RGBA16 words')
        while len(data)%4:data.append(0)
        data+=struct.pack('>IHH',2*(y0*width+x0),x1-x0,y1-y0)+ink+shadow
        for y in range(y0,y1):
            background=source[2*(y*width+sample):2*(y*width+sample)+2]
            colors=[background,ink,shadow];data+=background;x=x0
            while x<x1:
                color=pixels[2*(y*width+x):2*(y*width+x)+2]
                if color not in colors:raise ValueError('Pixel outside row palette')
                n=1
                while n<63 and x+n<x1 and pixels[2*(y*width+x+n):2*(y*width+x+n)+2]==color:n+=1
                data.append(colors.index(color)*64+n);x+=n
    while len(data)%4:data.append(0)
    return bytes(data)


def apply_palette(source,width,height,stream):
    """Checked independent decoder for the generated three-color row stream."""
    output=bytearray(source)
    if len(source)!=width*height*2 or len(stream)<4:raise ValueError('Invalid palette image/stream')
    count=struct.unpack_from('>I',stream)[0];p=4
    if not 1<=count<=64:raise ValueError('Invalid palette rectangle count')
    for _ in range(count):
        aligned=(p+3)&~3
        if any(stream[p:aligned]):raise ValueError('Nonzero palette alignment')
        p=aligned
        if p+12>len(stream):raise ValueError('Truncated palette rectangle')
        off,w,h=struct.unpack_from('>IHH',stream,p);ink,shadow=stream[p+8:p+10],stream[p+10:p+12];p+=12
        if off%2 or not 1<=w<=255 or h<1 or (off//2)%width+w>width or off+2*((h-1)*width+w)>len(output):raise ValueError('Palette rectangle outside output')
        for y in range(h):
            if p+2>len(stream):raise ValueError('Truncated palette background')
            colors=[stream[p:p+2],ink,shadow];p+=2;left=w;dst=off+2*y*width
            while left:
                if p>=len(stream):raise ValueError('Truncated palette run')
                code=stream[p];p+=1;n=code&63;index=code>>6
                if n<1 or n>left or index>=3:raise ValueError('Invalid palette run')
                output[dst:dst+n*2]=colors[index]*n;dst+=n*2;left-=n
    if any(stream[p:]) or len(stream)-p>3:raise ValueError('Unexpected palette trailing data')
    return bytes(output)


def payload(blob, pixels, width, height, captions, *, copy=False, palette_source=None):
    header=bytearray(blob[:100]);header[:8]=EXEC_HEADER
    if copy:
        struct.pack_into('>I',header,0x10,len(pixels))
        return bytes(header)+COPY_PROGRAM+pixels
    palette=palette_source is not None
    code=patch_code(100,100,width,palette=palette)
    hvq_offset=(100+len(code)+15)&~15
    patch_offset=(hvq_offset+len(blob)+3)&~3
    stream=caption_palette(palette_source,pixels,width,height,captions) if palette else caption_runs(pixels,width,height,captions)
    program=patch_code(hvq_offset,patch_offset,width,palette=palette)
    data=bytes(header)+program
    data=data.ljust(hvq_offset,b'\0')+blob
    return data.ljust(patch_offset,b'\0')+stream
