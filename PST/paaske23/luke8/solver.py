#!/usr/bin/env python3

last_y = "0"
for line in list(map(lambda x:x.strip(), open("innsamlet.csv").readlines()[1:])):
    x,y,ch = line.replace("'",'').split(",")
    if y != last_y:
        last_y = y
        print()
    print(ch == "1" and "█" or " ", end='')
print()

