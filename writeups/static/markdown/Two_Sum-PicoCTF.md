# Two Sum - PicoCTF

A princípio parece um desafio matemático, mas se trata mais de
um conhecimento básico sobre inteiros nas linguagens de programação.
Ele pede os dois números positivos que possibilitam a veracidade dessa condição:
`n1 > n1 + n2 OR n2 > n1 + n2`. Matematicamente, ela não faz mutio sentido,
viso que qualquer soma de dois naturais é maior que os naturais que foram somados 
(tendo em mente as propriedades dos naturais e a função sucessora).

Contudo, algumas coisas impossíveis se tornam possíveis quando a memória não é infinita.
Basta pegar qualquer número e somar ao maior inteiro possível (**INT_MAX** = 2147483647) e teremos um overflow
de modo que o resultado será o **INT_MIN**, que é negativo e portanto menor que os positivos.

```bash
nc saturn.picoctf.net 51124

n1 > n1 + n2 OR n2 > n1 + n2 
What two positive numbers can make this possible: 
2147483647 1
You entered 2147483647 and 1
You have an integer overflow
YOUR FLAG IS: picoCTF{Tw0_Sum_Integer_Bu773R_0v3rfl0w_e06700c0}
```

*Obviamente não precisavam ser esses números, qualquer soma que passasse do INT_MAX resultaria em overflow*

---
> ### **FLAG:**
>
> picoCTF{3lf_r3v3r5ing_succe55ful_7851ef7d}