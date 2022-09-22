# Android

## Hidden Functionality

Finner denne i koden.

```java
    private static final byte[] H = {72, 66, 77, 65, 69, 48, 107, 76, 76, 82, 89, 65, 83, 120, 119, 84, 65, 66, 78, 74, 67, 121, 48, 87, 65, 69, 115, 99, 69, 119, 65, 84, 83, 82, 99, 112, 69, 82, 73, 65, 83, 81, 81, 70, 65, 66, 65, 86, 99, 119, 65, 82, 69, 120, 65, 71, 88, 119, 48, 88, 65, 84, 104, 74, 72, 104, 85, 87, 66, 108, 56, 78, 70, 119, 69, 52, 83, 82, 52, 86, 70, 103, 90, 102, 69, 82, 77, 71, 75, 103, 73, 61};
    private static final int[] I = {202, 194, 230, 232, 202, 229, 190, 202, 206, 206};

    public static final String n0() {
        byte[] decode = Base64.getDecoder().decode(H);
        byte[] bArr = new byte[decode.length];
        for (int i2 = 0; i2 < decode.length; i2++) {
            byte b2 = decode[i2];
            int[] iArr = I;
            bArr[i2] = (byte) (b2 ^ (iArr[i2 % iArr.length] / 2));
        }
        return RSA8092BitDecrypt(new String(bArr, StandardCharsets.UTF_8));
    }

```

Den RSA8092-greia er klin bambus. Printer før return og får noe som med rot13 blir 
> left,left,left,left,left,right,right,right,left,left,left,left,right

Det er tastekomboen for å åpne opp en slider i appen, men den sjekker om det er CrimePhone420 og her gikk vi tom for tid.

