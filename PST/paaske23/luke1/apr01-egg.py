import string

s = "pBrpnRrB/nPpbrBPP/rRbnpNBR/pBNBPrPP/pNrnNpPR/rPRBbNrB/bBPpNPpn/rPRbpRrN/" + \
    "nRrBBRPN/bBPNnrPP/rRPnRpNr/rNPbnprB/pPNbPbRP/rBRpNrBP/rNBRrPRp/nPBrbnrN/" + \
    "pPNBrbPp/bNBnPnrP/rNRbbprB/bPBrBPBr/pBNRrNnp/pPBnpPpP/rNBRnrBn/bNPBRRnN/"

egg = []
tmp = ""
for ch in s:
    if ch == "/": 
        egg.append(chr(int(tmp, 2)))
        tmp = ""
        continue
    tmp += ch in string.ascii_lowercase and "0" or "1"

print("".join(egg))
