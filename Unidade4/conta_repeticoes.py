# coding: utf-8
# conta repeticoes
# raquel ambrozio

quantidade = int(raw_input())
lista = []

for i in range(quantidade):
               numero = int(raw_input())
               lista.append(numero)
lista2 = []
for i in range(len(lista)):
               if lista[i] != lista[i-1]:
                              lista2.append(lista[i])
quantidade = []
for i in range(len(lista2)):
               quantidade.append(lista.count(lista2[i]))
               print "%d: %d" % (lista2[i], quantidade[i]) 
