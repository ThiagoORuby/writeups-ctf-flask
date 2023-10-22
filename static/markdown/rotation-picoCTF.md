# Rotation - picoCTF

Criptography 
{: .badge .text-bg-danger}

Esse é um outro desafio consideravelmente simples, que demorei um pouco
por não ligar o nome do desafio ao tipo de criptografia a ser utilizada.
O arquivo baixado se chama **encrypted.txt** e contem a flag criptografada
`xqkwKBN{z0bib1wv_l3kzgxb3l_25l7k61j}`.

Os números, de inicio, podem confundir na identificação do tipo de criptografia,
mas a ideia de rotações está ligada a cifra de césar. Utilizando um [site](https://www.dcode.fr/caesar-cipher)
para decodificação, logo de cara nos deparamos com a resposta:

![](../static/markdown/src/caesar_cipher.png)

---
> ### **FLAG:**
>
> picoCTF{r0tat1on_d3crypt3d_25d7c61b}