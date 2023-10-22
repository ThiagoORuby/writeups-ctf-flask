# Money-ware - PicoCTF 2023

General Skills 
{: .badge .text-bg-danger}

OSINT 
{: .badge .text-bg-dark}

Esse é um dos desafios propostos mais simples de solucionar. É dito que seu amigo
foi hackeado e solicitaram o pagamento em bitcoins para `1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX`.
O apenas desafio pede o nome do malware que ocasionou isso.

O primeiro passo é jogar a informação do destino dos bitcoins no google. Com isso, encontramos,
logo de inicio, uma noticia da [CNBC](https://www.cnbc.com/2017/06/28/ransomware-cyberattack-petya-bitcoin-payment.html) que informa um ataque hacker envolvendo esse "endereço". Lendo
atentamente o texto, podemos facilmente encontrar o nome do virus (malware) relacionado:

>The malware, which has been identified as a modified version of the **“Petya"** virus, has also affected business in >Western Europe, including Maersk, Merck and WPP.
>
>The virus locks users out of their computer and demands a ransom of $300 paid in Bitcoin.

---
> ### **FLAG:**
>
> picoCTF{Petya}