#!/usr/bin/env python3

from base64 import b64decode, b64encode
from binascii import hexlify, unhexlify

cookie = "4e5459354e6a673d3173774d68626464"

cookie = unhexlify(cookie).decode("utf-8")
plain = b64decode(cookie[:8]).decode("utf-8")
foo = cookie[8:]
print(cookie)
print(plain)
print(foo)


def out(s):
    return hexlify(b64encode(s.encode("utf-8"))).decode("utf-8")

print(out("00001") + out("11111"))