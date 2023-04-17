#!/usr/bin/env python3

import sys

from binascii import unhexlify, hexlify
from PIL import Image
from pwn import *

im = Image.open("bilde.png")
px = im.load()


for y in range(im.size[1]):
    r = g = b = []
    for x in range(im.size[0]):
        c = px[x,y]
        r.append(c[0])
        g.append(c[1])
        b.append(c[2])
    
    xr = xor(r, b"STEREOGRAM")
    xg = xor(g, b"STEREOGRAM")
    xb = xor(b, b"STEREOGRAM")
    hx = hexlify(bytes(xr+xg+xb)).decode("utf-8")

    if hx.find("4547477b") > -1:
        print(hx)
        print(x,y)



