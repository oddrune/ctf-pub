# Credential Custodian

Python-scriptet som genererer passord gjør int(time.time()), og det reduserer mulige passord til ett per sekund. Loopet igjennom og prøvde alle mulige kombinasjoner til noe ble forholdsvis printbart.

```python
def percentage_printable(s):
    printable = len([ch for ch in s if ch in string.digits + string.ascii_letters + " "])
    return int((printable/len(s))*100)

def bruteforce_from_date(datestr, days):
    flag = base64.b64decode("OTskUhcDAWQuBy50AQgJExRVHh1uFgomAm4VEwoQLDAfFkQSHxkDB1AKcAYIAmM9MBw=")
    seedstart = int(time.mktime(time.strptime(datestr, "%Y-%m-%d")))
    seedstop = seedstart + int(days)*(86400)+1
    for seed in range(seedstart, seedstop):
        pwd = generate_password(50, seed)
        decrypted = xor(flag, bytes(pwd, 'utf-8')).decode()
        if percentage_printable(decrypted)>90:
            print("{} {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(seed)), decrypted))

```

Scriptet skriver hashen til seg selv, og scriptet var sist endret 2022-08-29, så jeg prøvde lenge å finne et passord i 2022.

Utfordringen var å lese teksten øverst i det opprinnelige scriptet:
```
2010-05-04: Here is the password manager you wanted; Start using it TODDAY!
2010-05-03: Implemented OWN generate_password function. Probably secure.
2010-05-02: Started development. Stole most of the code from hackexchange.
```

Doh. Justerte tidsrammen litt, så kom passordet ganske raskt:
```
2010-05-04 13:37:00 van use aim leg wall deal sad air put wide act pen
```
