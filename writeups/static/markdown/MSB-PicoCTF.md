# MSB - PicoCTF

Forensics
{: .badge .text-bg-danger}

Steganography
{: .badge .text-bg-black}

Esse com certeza foi o mais desafiador de todos, fazendo jus a sua pontuação.
O desafio entrega uma imagem, afirma que ela passa na análise estatística LSB,
mas que há algo bem presente na imagem para ser descoberto.

Fui primeiramente entender o que é análise LSB (Low Significant Bit) e compreendi
que se trata de extrair os bits menos significativos de uma imagem, onde normalmente
podem estar escondidas mensagens ou textos.

Observando a imagem, é visivel que existem pixels a mais e que, de certa forma, corrompem
a imagem. Mas a ideia do LSB é que os bits estejam escondidos. Como esses estão aparentes,
então muito claramente se tratam de MSBs (Most Significant Bits).

Busquei por códigos de LSB ou MSB em python, fiz algumas adaptações e consegui extrair um texto
consideravelmente grande e lá, finalmente, estava a flag.

```python
import os
import binascii
import sys
from PIL import Image

def MSB(file, outputFile):
  databin = []
  with Image.open(file) as img:
    w, h = img.size

    for x in range(0, h):
      for y in range(0, w):
        pixel = list(img.getpixel((y,x)))

        R = str((pixel[0] >> 7) & 1)
        G = str((pixel[1] >> 7) & 1)
        B = str((pixel[2] >> 7) & 1)

        databin.extend([R, G, B])

  resultFile = open(outputFile + ".txt", "w")
  size = len(databin)
  for i in range(0,size,8):
      # Each 8 bits convert into a int value
      value = int("".join(databin[i:i+8]),2)
      # Check if it is in the printable range
      if value >= 32 and value <= 126:
          resultFile.write(chr(value))
  resultFile.write("\n")
  resultFile.close()
```

![](../static/markdown/src/msb.png)



---
> ### **FLAG:**
>
> picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_06326238}