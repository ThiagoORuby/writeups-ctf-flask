# Match the Regex - PicoCTF

Esse é um dos desafios mais simples entre todos (desde
que você saiba o básico de Regex). A principio, é pedido
apenas que tente enviar expressões regulares através daquele
formulário.

O que pode-se rapidamente pensar quando se conhece Regex é que
o desafio gostaria de um RegEx que identificasse a flag. Algo como
sempre começar com `picoCTF` seguido de `{` e uma sequência arbitrária
de caracteres e um `}`

Segue então os seguintes comandos de regex:

- [^] : indica o conjunto de caracteres que NÃO pode ter no texto
- \+ : indica que deseja-se obter 1 ou mais caracteres
- { e } são caracteres especiais, então para serem usados, devem ser antecedidos por `\`

Como queremos uma sequência de caracteres entre chaves, podemos pedir 1 ou mais caracteres
diferentes de `}` e então fechar com `}`:

Portanto , teriamos `PicoCTF\{[^}]+\}`. E com isso:

![](../static/markdown/src/regex.png)


*Posteriormente eu percebi que era só mandar um `PicoCTF` que funcionava, nada muito
elaborado ;-;*

---
> ### **FLAG:**
>
> picoCTF{succ3ssfully_matchtheregex_08c310c6}