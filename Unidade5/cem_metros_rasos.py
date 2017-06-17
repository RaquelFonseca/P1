# coding: utf-8
# cem metros rasos

quantidade = int(raw_input())
lista_nomes = []
lista_media = []
lista_menor = []

while quantidade > 0:
    dados = raw_input().split(", ")
    nome = dados.pop(0)
    soma = 0
    menor = float(dados[0])
    for elem in dados:
        soma += float(elem)
        if float(elem) < menor:
            menor = float(elem)
    media = soma / len(dados)
    lista_nomes.append(nome)
    lista_media.append(media)
    lista_menor.append(menor)
    quantidade -= 1

for i in range(len(lista_nomes)):
    print "%s: media = %.2f, menor = %2.f" % (lista_nomes[i], lista_media[i], lista_menor[i])

i_menor = 0

for i in range(1, len(lista_menor)):
    if lista_menor[i] < lista_menor[i_menor]:
        i_menor = i
print "menor tempo: %s, %.2f" % (lista_nomes[i_menor], lista_menor[i_menor])

i_menor = 0

for i in range(1, len(lista_media)):
    if lista_media[i] < lista_media[i_menor]:
        i_menor = i
print "menor media: %s, %.2f" % (lista_nomes[i_menor], lista_media[i_menor])
