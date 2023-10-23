# Timer - PicoCTF

Reverse Engeneering
{: .badge .text-bg-danger}

Android
{: .badge .text-bg-black}

Mais um desafio de engenharia reversa que envolve a decompilação
de arquivos. Dessa vez, com um arquivo `.apk`, sendo um aplicativo
de timer. Basta decompilar com o `apktool` e procurar a flag:

```bash
apktool d timer.apk
```

Abrindo a pasta do projeto no vscode e buscando o termo `picoCTF` nos
arquivos, encontramos facilmente a flag:

![](../static/markdown/src/apk.png)

---
> ### **FLAG:**
>
> picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}