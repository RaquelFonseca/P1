# coding: utf-8
# menor dos extremos
# raquel ambrozio

quantidade = int(raw_input())
assert quantidade > 1
lista = []

for i in range(quantidade):
        numeros = int(raw_input())
        lista.append(numeros)
abaixo = 0
acima = 0
abaixo1 = 0
acima1 = 0
for i in range(len(lista)):
        if lista[0] < lista[-1]:
               for i in range(len(lista)):
                       if i < lista[0]:
                               abaixo += 1
                        else:
                                acima +=1
                       if i < lista[-1]:
                               abaixo1 += 1
                        else:
                                acima1 += 1

print abaixo
print abaixo1
print acima
print acima1
        
        
