# Reverse - PicoCTF

Mais uma questão de engenharia reversa, o que implica que o
primeiro passo é sempre analisar o tipo de arquivo e tentar
decompilar ele. O arquivo em questão é um binário chamado `ret`.

Para decompilar binários podemos usar uma das ferramentas mais
famosas do ramo: o **Ghidra**. Basta criar um novo projeto, importar
o arquivo binário e executar a auto análise do Ghidra. O proxímo passo
sempre é tentar buscar a flag em algum lugar do resultado da decompilação:

- Andando nas funções encontradas, vemos a flag na main:

![](../static/markdown/src/reverse.png)

> ### **FLAG:**
>
> picoCTF{3lf_r3v3r5ing_succe55ful_7851ef7d}