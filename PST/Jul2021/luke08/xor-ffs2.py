#!/usr/bin/env python3

from pwn import xor
#open("hailmary.png", "wb").write( xor(open("b0-hex-frimerke.png", "rb").read(), open("s8-runner.out", "rb").read()))

b0 = open("b0-hex-frimerke.png", "rb").read()
s8 = open("keke2.out", "rb").read()

out = open("hailmary3.png", 'wb')
for i in range(len(b0)):
  print(type(b0[i]))
  out.write(xor(b0[i], s8[i]))

out.close()
