# coding: utf-8
# organiza partes das matriculas
# raquel ambrozio


i = 0
lista = []

while i == 0:
       matricula = int(raw_input())
       if matricula < 0:
              break
       lista.append(matricula)

posicao = int(raw_input()) 
parte1 = lista[:posicao-1]
parte2 = lista[posicao-1:]

for i in parte1:
       print i

print "---"

parte2.sort()

for i in parte2:
       print i



