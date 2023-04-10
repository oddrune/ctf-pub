import rsa
import openssh_key.private_key_list as pkl
from Crypto.Util.number import inverse

partialkey = pkl.PrivateKeyList.from_string(open('id_rsa').read())[0]
(n,e,d,iqmp,p,q) = partialkey.private.params.values()

e = inverse(d, (p-1)*(q-1))

ciphertext = open("flag.encrypted", "rb").read()

priv = rsa.PrivateKey(p*q, e, d, p, q)
print(rsa.decrypt(ciphertext, priv).decode("utf-8"))