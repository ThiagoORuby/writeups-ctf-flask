# Pcap Poisoning - PicoCTF

Forensics
{: .badge .text-bg-danger}

Pcap
{: .badge .text-bg-black}

Esse desafio consegue ser extremamente simples, desde que você não
pense em soluções mirabolantes. Basta baixar o arquivo `trace.pcap`
e abrir no **wireshark**.

Trata-se de um conjunto consideravelmente grande de capturas, onde boa
parte envolve transferências de dados por FTP. Mas próximo ao final, há
uma série de retransmissões TCP e exatamente na primeira se encontra a 
flag do desafio:

![](../static/markdown/src/trace.png)

---
> ### **FLAG:**
>
> picoCTF{P64P_4N4L7S1S_SU55355FUL_4d72dfcc}