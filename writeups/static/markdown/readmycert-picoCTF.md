# Read My Cert - PicoCTF

Criptography 
{: .badge .text-bg-danger}

Esse desafio é bastantes simples desde que se saiba o que fazer com e
como decodificar arquivos **.csr**. O que é trivial se você já tiver
feito a room de introdução a [Criptografia](https://tryhackme.com/room/cryptographyintro)
do TryHackMe.

Podemos fazer isso utilizando o `openssl` da seguinte maneira:

```bash
openssl req -in readmycert.csr -out decoded.txt -text
cat decoded.txt

Certificate Request:
    Data:
        Version: 1 (0x0)
        Subject: CN = picoCTF{read_mycert_a7163be8}, name = ctfPlayer
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (2048 bit)
                Modulus:
...
```

---
> ### **FLAG:**
>
> picoCTF{read_mycert_a7163be8}

