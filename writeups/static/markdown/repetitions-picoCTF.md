# Repetitions - PicoCTF

General Skills 
{: .badge .text-bg-danger}

Base64 
{: .badge .text-bg-dark}

Como as próprias tags do desafio indicam, precisamos usar base64.
Baixando o arquivo, vemos logo que se trata de uma informação codificada
em base64:

```bash
cat enc_flag

VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVh
RmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNk
MlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVW
VkpEVGxaYVdFMVhSbFZrTTBKVVZXMTRWMDVHV2toalJYUlhDazFyV25sVVZXaHpWakpHZEdWRlZs
aGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==
```

Decodificando o arquivo com o **base64** do linux, vemos que o resultado é outro
base64:

```bash
base64 enc_flag

VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVh
RmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNk
MlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVW
VkpEVGxaYVdFMVhSbFZrTTBKVVZXMTRWMDVHV2toalJYUlhDazFyV25sVVZXaHpWakpHZEdWRlZs
aGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==
```

Seguindo a dica, multiplas decodificações são necessárias para achar a flag e para
isso, podemos construir um código em bash para rodar o base64 no arquivo até encontrar
a flag (o que pode ser simulado com a ideia de ter o termo "picoCTF" no conteúdo):

```bash
while true
do
    base64 -d -i enc_flag >> enc_flag
    cat enc_flag

    if grep -q "picoCTF" enc_flag
    then
        break
    fi
done
```

**saída:**
```
...
picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_4557ec3e}
```

---
> ### **FLAG:**
>
> picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_4557ec3e}




