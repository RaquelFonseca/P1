# raquel ambrozio
# series alternadas
# coding: utf-8

quantidade = int(raw_input())
primeiro = 1
segundo = 1
lista = []

for i in range(quantidade):
    lista.append(primeiro)
    lista.append(segundo)
    print lista[i]
    primeiro = primeiro + 3
    segundo = segundo * primeiro
    
