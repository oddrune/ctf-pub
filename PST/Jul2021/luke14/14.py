#!/usr/bin/env python3
import collections
from pwn import xor

points = {}
in_coord = False
name = None
all_points = []
for line in open("Reindeer_tracker.kml").readlines():
    if line.find("</coordinates>") > 0:
        in_coord = False
    if line.find("<name>") > 0:
        name = line.split(">")[1].split("</")[0]

    if in_coord:
        coords = line.strip().split(" ")
        points[name] = set(coords)
        all_points += coords

    if line.find("<coordinates>") > 0:
        in_coord = True        

print(points.keys())
#print([item for item, count in collections.Counter(all_points).items() if count > 1])

all_z = [p.split(',')[-1].split('.')[0] for p in all_points if p[0] in '0123456789']

print("".join([chr(int(c) ^493) for c in all_z]))

#print(xor(all_z,493))
