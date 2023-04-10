#!/usr/bin/env python3

def load():
  out = []
  for line in open('verksted_npst.txt').readlines():
    e = line.strip().split(";")
    if e[0] == "Indeks": continue
    if int(e[1], 16) > 127: continue
    out.append([chr(int(e[1], 16)), e[2]])
  return out


for l in sorted(load(), key=lambda d: d[1]):
    print(l[0], end='')

print()
