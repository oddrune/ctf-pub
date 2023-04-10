#!/usr/bin/env python3
import base64
from Crypto.Cipher import AES

data = base64.b64decode('Y2MPyYU4kblEXrEfExry4AIRAjqdke+JyQQN50Uj5GuCu5rE66lEzQXB5bEVOlNGRoU06Ny4vh/gzSPFV0mHUrxaaAVt1BwN1WN1HFT7baIejtR5KyG6JK8yC70CpuPZV610coCiWzdFICcgEtAdQaesScLrg495kxofzG3EGvA=')
print(AES.new('julenissenerteit', AES.MODE_ECB).decrypt(data))


