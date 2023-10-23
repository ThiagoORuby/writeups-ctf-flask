# Useless - PicoCTF

General Skills
{: .badge .text-bg-danger}

man
{: .badge .text-bg-black}

O desafio passa os dados necessários para uma conexão via SSH
para acesso a uma máquina remotamente e informa a existência de um
script intersante na home da máquina:

```bash
ssh picoplayer@saturn.picoctf.net -p63327
```

O arquivo na home, chamado `useless` é um bash script que faz operações
básicas:

```bash
# Basic mathematical operations via command-line arguments

if [ $# != 3 ]
then
  echo "Read the code first"
else
        if [[ "$1" == "add" ]]
        then 
          sum=$(( $2 + $3 ))
          echo "The Sum is: $sum"  

        elif [[ "$1" == "sub" ]]
        then 
          sub=$(( $2 - $3 ))
          echo "The Substract is: $sub" 

        elif [[ "$1" == "div" ]]
        then 
          div=$(( $2 / $3 ))
          echo "The quotient is: $div" 

        elif [[ "$1" == "mul" ]]
        then
          mul=$(( $2 * $3 ))
          echo "The product is: $mul" 

        else
          echo "Read the manual"
         
        fi
fi
```

Mas nada disso interessa, basta ver o manual desse script
usando o seguinte comando:

```
man useless

useless
     useless, — This is a simple calculator script

SYNOPSIS
     useless, [add sub mul div] number1 number2

DESCRIPTION
     Use the useless, macro to make simple calulations like addition,subtraction, multiplication and division.

Examples
     ./useless add 1 2
       This will add 1 and 2 and return 3

     ./useless mul 2 3
       This will return 6 as a product of 2 and 3

     ./useless div 6 3
       This will return 2 as a quotient of 6 and 3

     ./useless sub 6 5
       This will return 1 as a remainder of substraction of 5 from 6

Authors
     This script was designed and developed by Cylab Africa

     picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_6194}
```


---
> ### **FLAG:**
>
> picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_6194}