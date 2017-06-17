# coding : utf-8
# soma div5
# raquel ambrozio

n = int(raw_input())
soma = 0

for i in range(n):
        numeros = int(raw_input())
        if numeros % 5 == 0:
                soma += numeros

print soma
        
