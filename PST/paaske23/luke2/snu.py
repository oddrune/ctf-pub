#!/usr/bin/env python3

from collections import defaultdict

out = defaultdict(list)

for line in open("Ook.txt").readlines():
    sp = line.strip().split()
    for i in range(len(sp)):
        out[i].append(sp[i])

for i in sorted(out.keys()):
    print(" ".join(out[i]))