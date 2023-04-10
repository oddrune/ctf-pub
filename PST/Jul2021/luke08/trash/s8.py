#!/usr/bin/python3

import sys
import argparse
import itertools

from pwn import *

#cipher = open("b0.png", "rb").read()
cipher = open("b0-hex-frimerke.png", "rb").read()

out = open("b0-xor.png", "wb")
out.write(cipher[:5])
#out.write(xor(cipher[5:], b"Frimerke".ljust(len(cipher)-5, b"\0")))
out.write(xor(cipher[5:], b"Frimerke"))


print(xor(cipher[5:], b"Frimerke")[:30])
