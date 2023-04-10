#!/usr/bin/env python3

data = eval(open("huskelapp_til_2021.txt").read())
print("latitude,longitude")
for elem in data:
    if elem:
      print("{},{}".format(elem[0],elem[1]))

