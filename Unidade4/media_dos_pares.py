# coding: utf-8
# media dos pares
# raquel ambrozio

quantidade = int(raw_input())
assert quantidade > 0
somapar = 0
pares = 0
numeros = []

for i in range(quantidade):
        numero = int(raw_input())
        numeros.append(numero)
        if numero % 2 == 0:
                somapar += numero
                pares += 1
media = somapar / float(pares)
menores_media = 0

for i in range(len(numeros)):
        if numeros[i] < media:
                        menores_media +=1

print "soma: %d" % somapar
print "media: %.1f" % media
print "%d numero(s) abaixo da media" % menores_media
