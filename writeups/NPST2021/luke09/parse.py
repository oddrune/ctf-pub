#!/usr/bin/env python3
import json

def tap(s):
    alphabet = ["A","B","K","D","E","F","G","H","I","J","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    tap = ["11", "12", "13", "14", "15", "21", "22", "23", "24", "25", "31", "32", "33", "34", "35", "41", "42", "43", "44", "45", "51", "52", "53", "54", "55"]

    out = []
    for words in s.split("  "):
        out.append("".join([alphabet[tap.index(ch)] for ch in words.split()]))
    return " ".join(out)

for p in json.load(open("pcap-export.json")):
   ip = p["_source"]['layers']['ip']['ip.src']
   try:
      # Konverter fra kolon-separert hex av rådata til ascii
      data = "".join([chr(int(a, 16)) for a in p["_source"]['layers']['data']['data.data'].split(":")]) 
   except:
      # ikke alle har data-keyen.
      continue

   untapped = tap(data)
   if untapped.startswith("PST"):
      print("Source IP: ", tap(ip.replace(".", " ")))
      print("Data:      ", untapped)
