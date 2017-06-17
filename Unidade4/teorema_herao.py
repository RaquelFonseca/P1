# coding: utf-8
# teorema de hera
# raquel ambrozio

import math

quantidade = int(raw_input())
lista_area = []

for i in range(quantidade):
    lado = raw_input().split()
    s = (float(lado[0]) + float(lado[1]) + float(lado[2])) / 2.0
    A = math.sqrt(s*(s-float(lado[0]))*(s- float(lado[1]))*(s-float(lado[2])))
    lista_area.append(A)

maiores = 0
soma_maiores = 0

for i in range(len(lista_area)):
    print "Area %d: %.2f" % (i+1, lista_area[i])
    if lista_area[i] > 100:
        maiores += 1
        soma_maiores += lista_area[i]

if maiores > 0:
    print "Numero maiores: %d, area media: %.2f" % (maiores, soma_maiores / maiores)
    
