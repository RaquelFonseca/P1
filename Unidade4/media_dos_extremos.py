# coding: utf-8
# media dos extremos
# raquel ambrozio

quantidade = int(raw_input())
assert quantidade > 1
lista = []

for i in range(quantidade):
  lista.append(int(raw_input()))

menor = lista[0]
maior = lista[0]
abaixo = 0
acima = 0

for i in range(len(lista)):
    if lista[i] < menor:
      menor = lista[i]
    if lista[i] > maior:
      maior = lista[i]
    media_extremos = (lista[0] + lista[-1]) / 2.0
    if lista[i] < media_extremos:
      abaixo += 1
    else:
      acima +=1

print "Menor numero: %d" % menor
print "Maior numero: %d" % maior
print "Media dos extremos: %.2f" % media_extremos
print "%d numero(s) abaixo da media" % abaixo
print "%s numero(s) acima da media" % acima
      
