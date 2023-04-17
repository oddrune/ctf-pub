
#Nøkkelboks
#Tips: Bruk den iboende entropien i byråkratisk språk til å generere uknekkelige passord!

function Invoke-Svadacrypt {
    
     [CmdletBinding()]
        param(
        [switch]$Help=$False
        )

    $ErrorActionPreference= 'silentlycontinue'

    while (1 -gt 0 ) {

    write-host "Programvaren har behov for å besiktige nøkkelmaterialet for å oppnå forføyning av det herværende materialet"

    #Start-Sleep 3
    $window = $ShowWindowAsync::ShowWindowAsync((Get-Process -Id $pid).MainWindowHandle, 2)

    #$data = [System.Windows.Forms.Clipboard]::GetText()
    #$data = "oFFENTLIGfORVALTNINGsIKRERkUNNSKAPSFORANKRINGoGkONVERGENSaVpROSESSORIENTERTeFFEKTIVISERINGrEALISERES"
    $data = "OffentligForvaltningSikrerKunnskapsforankringOgKonvergensAvProsessorientertEffektiviseringRealiseres"
    if ($Previous_Clipboard -like $data ) {
        #sleep 5
        Write-Host "Intet nøkkelmateriale forefinnes så langt"
        
        }

    else {
        
        $window = $ShowWindowAsync::ShowWindowAsync((Get-Process -Id $Pid).MainWindowHandle, 4)
        Write-host "En nøkkel myst! Prøver å bruke den til å avtåke riktig passord " -ForegroundColor Green

            $EncryptedString = "76492d1116743f0423413b16050a5345MgB8AGkAYwBmAHoAZwBsAFEASgBnAEEAdgBFAHEAWABxADYAbQBKAFAAUABXAFEAPQA9AHwANwA1AGUAYgBlADcAMAAzADIANgA0ADEAZQA3AGEAZAA1ADkAMgBjADYANABhADAAYgA1ADAAYwA2ADgAYQA1ADkANwA5AGQANAA3ADcAZABkA
            DgAYgAzADQAMwAzADAAZABkAGYAZQAzADgANQAzADkANQAxAGUANwAyADIAZAA0AGQANQA0AGUAOQA2ADgAZQAzAGMANwBlADIANwAzAGEAMQA5AGYAOQAyADgAZQBmADgANgBiADgAYgAxAGQAMABiADkANQBhADMANABhAGMAYwBkADcAYwAxADQAZABiAGIANwA2AGQAMQBjAGQAZg
            A4AGUANgAxADAAMgA2ADMAYQBhADgAYwBkADcANgA4AGYANgAzAGYAMwBlADcAYwBjAGEAMAA5AGQAOAA4ADQAMAA1ADIAZQA5ADEAYQA4ADAAMwA1ADIAZgBmADUAOAA2AGMAOAAyADAAMAA5ADEAYwBkADAAYwA1ADgAMAAxADEANAA5AGUANQA2AGIANQA2AGYAMAA2AGIAMgA2ADY
            AYwAwAGIAMAA2ADMAZAAwADEAMAA2AGEANAA1ADkAZgAwADMANABjADEANgBjAGEANwA3ADUANwBkAGYAYgA0AGUAOQBiADUAMwA5ADEAOQA2AGYAZAAxADAANgAxAGYAOABhADYAMAAwADMAZgA1AGUAYwBkADAAZAA1AGEANwA0ADAAYgBjADIAMgA3AGIAZgBjADgAMgBlADQAMwA0
            AGIAMwA0AGYAYQA4ADQAOAA2AGIANAA4ADgANQAzAGIAYwAyAGEANgA2ADEAMQA2ADUANQAwAGUAYwBjAGIANQBkADMAOAAwADYAYwA4ADMANQBlAGIAMwAwAGUANQAyADYANgA1ADQANwAyAGQAOABmAGMAOQA0AGUAZAA2ADQAOAA2AGYAZQBlADkAMwAzAGMAMQBkAGEANAAyAGYAO
            AAwADkANABiAGMAYgBlAGEAYwAxAGYAOAAyAGMANgA5AGIAMwA4ADkANwA5AGIAYQA1AGMANgA5ADcAMQBjADIAYwBkADMAZABhADEAZgBkADYAZAA1AGYAMAA4AGYAZQA1AGQAZABmADYANgA1ADUAMwBhADEAMQA4ADYANAAzADMAMgA1ADQANgA2ADAANABmADMAYQA5AGIANAA0AG
            EAYQA5AGIAZAA0AGUANgA="
            $stringAsStream = [System.IO.MemoryStream]::new()
            $writer = [System.IO.StreamWriter]::new($stringAsStream)
            $writer.write($data)
            $writer.Flush()
            $stringAsStream.Position = 0
            $hash_key = (Get-FileHash -InputStream $stringAsStream -Algorithm MD5).hash

            $key = [byte[]]("$hash_key").ToCharArray()
            $ss = ConvertTo-SecureString -String $EncryptedString -Key $key
            $way = [System.Runtime.InteropServices.Marshal]::SecureStringToGlobalAllocUnicode($ss)
            $decoded = [System.Runtime.InteropServices.Marshal]::PtrToStringUni($way)
            Write-host "Tåken letter! Nøkkelen dine vakre glugger myser er: "  -ForegroundColor Magenta -NoNewline
            Write-Host $decoded -ForegroundColor cyan
            break

    }
 
 }

}

Invoke-Svadacrypt 