# coding: utf-8
# substitui espaco por virgula
# raquel ambrozio

frase = raw_input()
i = int(raw_input())
j = int(raw_input())
saida = " "

for caracteres in range(i,j):
        if frase[caracteres] == " ":
                saida += ", "
        else:
                saida += frase[caracteres] + " "
print saida[1:-1]


