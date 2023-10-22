# Who is it - PicoCTF

Segundo o desafio, alguém enviou um email alegando ser o co-fundador
do Google Larry Page, mas há suspeitas de ser scam. O trabalho é encontrar
de quem originalmente veio esse email.
O título da questão novamente entrega o que podemos usar. Nesse caso, o
comando **whois** do linux para obter informações sobre algum dado obitdo no email.

```bash
cat email-export.eml

... (google.com: domain of lpage@onionmail.org designates 173.249.33.206 as permitted sender) ...
```

Usando o **cat** para visualizar o conteúdo do arquivo, podemos encontrar com uma certa facilidade
o dominio e o IP do remetente e podemos tentar usar o `whois` para eles:

```bash
whois lpage@onionmail.org

No whois server is known for this kind of object.
```

```bash
whois 173.249.33.206

...
person:         Wilhelm Zwalina
address:        Contabo GmbH
address:        Aschauer Str. 32a
address:        81549 Muenchen
phone:          +49 89 21268372
fax-no:         +49 89 21665862
nic-hdl:        MH7476-RIPE
mnt-by:         MNT-CONTABO
mnt-by:         MNT-GIGA-HOSTING
created:        2010-01-04T10:41:37Z
last-modified:  2020-04-24T16:09:30Z
source:         RIPE
...
```

Sendo assim, vemos que o nome real do remetente é **Wilhelm Zwalina**

---
> ### **FLAG:**
>
> picoCTF{WilhelmZwalina}