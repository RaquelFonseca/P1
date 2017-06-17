# coding: utf-8
# soma multiplos do primeiro
# raquel ambrozio

lista = []

for i in range(11):
        numero = int(raw_input())
        lista.append(numero)

soma = 0
for i in range(1, len(lista)):
        if lista[i] % lista[0] == 0:
                soma += lista[i]
print soma
        
