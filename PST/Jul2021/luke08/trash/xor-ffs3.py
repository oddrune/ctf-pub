#!/usr/bin/env python3

from pwn import xor
open("hailmary4.png", "wb").write( xor(open("b0-hex-frimerke.png", "rb").read(), open("keke2.out", "rb").read()))

