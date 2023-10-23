# Safe Opener 2 - picoCTF

Reverse Engeneering
{: .badge .text-bg-danger}

Para esse desafios, só precisamos ligar a categoria dele
ao arquivo passado. `SafeOpener.class` é um arquivo java
compilado, portanto, focando em engenharia reversa, podemos
usar um decompilador e conseguir o arquivo java que originou
esse `.class`.

Usando o **java decompiler**, podemos facilmente encontrar a flag:

![](../static/markdown/src/java.png)

---
> ### **FLAG:**
>
> picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_b427942b}

