# Find and Open - PicoCTF

Forensics
{: .badge .text-bg-danger}

Outro desafio envolvendo **wireshark**, mas um pouco mais desafiador. Ele
entrega um arquivo `flag.zip` e um `dump.pcap` e pede para descobrir a chave do arquivo
compactado buscando na captura das transmissões. Abrindo o `dump.pcap`, vemos 
uma série de capturas de Ethernet II, onde as primeiras indicam que devemos navegar
por elas para encontrar respostas. Buscando a fundo, encontramos uma captura que 
se diferencia, claramente com um conteúdo criptografado com **base64**.

![](../static/markdown/src/dump.png)

Decodificando a informação, encontramos um pedaço da flag:

```bash
echo "VGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=" | base64 -d
This is the secret: picoCTF{R34DING_LOKd_
```

Nesse ponto do desafio, você pode pensar que deve continuar buscando algo nas
capturas, perdendo um bom tempo com nada de útil ou se lembrar do arquivo zipado
que precisa de uma chave para ser descompactado. Ao usar o pedaço da flag como chave,
conseguimos descompactar o arquivo e finalmente encontrar a flag completa.

---
> ### **FLAG:**
>
> picoCTF{R34DING_LOKd_fil56_succ3ss_cbf2ebf6}