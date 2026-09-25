#!/usr/bin/env python3
"""
lisaicon2.py -- build a Lisa Office System tool-icon file ({T<num>}ICON)
by cloning the structure of a file that is PROVEN to render on hardware
(T419307ICON.bin, the LisaSlideshow icon), and replacing the artwork.

The file is a Lisa FONT record:
    26-byte header  fontType 3, firstChar 0, lastChar 2, widMax 48,
                    kernMax 0, nDescent -32, fRectWidth 48, fRectHeight 32,
                    owTLoc 394, ascent 0, descent 32, leading 0, rowWords 12
    768-byte strike 12 words (24 bytes) per row x 32 rows = 4 cells of 48x32
        cell 0  char 0   document icon    (the art again -- no documents)
        cell 1  char 1   THE TOOL ICON
        cell 2  char 2   THE MASK         (filled silhouette of the art)
        cell 3  missing  checkerboard
    locTable  5 words  0, 48, 96, 144, 192
    owTable   5 words  0x0030 x4, 0xFFFF
    padding to 1,024 bytes (2 blocks) -- copied from the proven file.

Usage:  python3 lisaicon2.py art.png reference.bin out.bin [--show]
art.png = 48x32, dark = ink.
"""
import sys
from PIL import Image

W, H, CELLS = 48, 32, 4
ROWBYTES = W * CELLS // 8       # 24
HDR, STRIKE = 26, ROWBYTES * H  # 768

def load_art(path):
    im = Image.open(path).convert('L')
    assert im.size == (W, H), im.size
    return [[1 if im.getpixel((x, y)) < 128 else 0 for x in range(W)] for y in range(H)]

def silhouette(art):
    """Filled silhouette: everything not reachable from the outside background."""
    outside = [[0]*W for _ in range(H)]
    stack = [(x, y) for x in range(W) for y in (0, H-1)] + [(x, y) for y in range(H) for x in (0, W-1)]
    while stack:
        x, y = stack.pop()
        if not (0 <= x < W and 0 <= y < H) or outside[y][x] or art[y][x]:
            continue
        outside[y][x] = 1
        stack += [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    return [[0 if outside[y][x] else 1 for x in range(W)] for y in range(H)]

def pack(row):
    out = bytearray()
    for i in range(0, len(row), 8):
        v = 0
        for b in row[i:i+8]:
            v = (v << 1) | b
        out.append(v)
    return bytes(out)

def build(art, ref):
    mask = silhouette(art)
    checker = [[(x + y + 1) & 1 for x in range(W)] for y in range(H)]  # row 0 starts '#.'
    strike = b''.join(pack(art[y] + art[y] + mask[y] + checker[y]) for y in range(H))
    assert len(strike) == STRIKE
    out = ref[:HDR] + strike + ref[HDR+STRIKE:]
    assert len(out) == len(ref) == 1024
    return out

def show(data):
    for c in range(CELLS):
        print('cell', c)
        for y in range(H):
            row = data[HDR + y*ROWBYTES + c*6: HDR + y*ROWBYTES + c*6 + 6]
            print(''.join(f'{b:08b}' for b in row).replace('0', '.').replace('1', '#'))

if __name__ == '__main__':
    a, r, o = sys.argv[1:4]
    ref = open(r, 'rb').read()
    out = build(load_art(a), ref)
    open(o, 'wb').write(out)
    print(f'wrote {o}: {len(out)} bytes')
    if '--show' in sys.argv:
        show(out)
