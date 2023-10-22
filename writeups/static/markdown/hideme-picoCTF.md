# Hideme - PicoCTF 2023

forense 
{: .badge .text-bg-danger}

esteganografia 
{: .badge .text-bg-dark}

O desafio apresenta um arquivo `flag.png` e diz que um analista SOC viu esse arquivo transitando
entre duas pessoas e percebeu algo escondido. Usando **binwalk** no arquivo, podemos encontrar
conteúdos escondidos dentro dele:

```bash
binwalk flag.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 512 x 504, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed
39739         0x9B3B          Zip archive data, at least v1.0 to extract, name: secret/
39804         0x9B7C          Zip archive data, at least v2.0 to extract, compressed size: 2997, uncompressed size: 3152, name: secret/flag.png
43036         0xA81C          End of Zip archive, footer length: 22
```

Podemos, então, extrair os arquivos escondidos para uma pasta, nomeada como *_{nomearquivo}.extracted*

```bash
binwalk -e flag.png
```

Indo até a pasta, vemos uma pasta chamada *secret* e nela tem uma imagem que guarda a flag.

```bash
cd _flag.extracted
ls
29  29.zlib  9B3B  9B3B.zip  secret
```

![](../static/markdown/src/flag.png)

---
> ## **FLAG:**
>
> picoCTF{Hiddinng_An_imag3_within_@n_ima9e_85e04ab8}
