from base64 import b64decode

def to_chr(p):
    return "".join([chr(int(x)) for x in str(p).rsplit("000")])

def solveit(jx):
    p1, p2, p3 = map(int, b64decode(jx).decode('ascii').split('123456789'))
    flagg1 = p3
    flagg3 = p1^p3
    spechul_3 = int("000".join([str(ord(c) << 2) for c in to_chr(flagg3)]))
    flagg2 = p2^spechul_3
    return("".join(map(to_chr, (flagg1, flagg2, flagg3))))

jx = "MjA1NjA0NDQwOTE4NjY4NzYxNzk3NDI5NzA5OTEzNzg4Njc3MzQ0MDAzMDAzNTIzNTQ3NzIwNTQ4NTc0MjYwMDkzNzQ0MjE0OTA0ODU0MTIzNDU2Nzg5MTIyOTY4NTAzNDc5OTc2MTk1Mjc4MzA4NjA4NDI2MzUyNzIxMDYwOTI4ODE5MDYwOTQ3MzYyODY0MDA5NTk3ODI0MjI5MTAxNDQyNjczMDg4MzIxMjM0NTY3ODk5MDAwMDEwNTAwMDEwMzAwMDkwMDAwOTcwMDAxMDMwMDAzMjAwMDgwMDAwODIwMDA5NTAwMDk5MDAwMTE0MDAwOTUwMDA5NTAwMDEwMQ=="

print(solveit(jx))