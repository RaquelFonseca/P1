# coding: utf-8
# SAMU
# raquel ambrozio

soma = 0
lista = []


for i in range(1, 13):
        atendimentos = int(raw_input())
        soma += atendimentos
        lista.append(atendimentos)

media = float(soma) / len(lista)
print "Media mensal de atendimentos: %.2f" % media
print "----"

for i in range(len(lista)):
        if lista[i] > media:
                print "Mes %d: %d" % (i+1, lista[i])
       
