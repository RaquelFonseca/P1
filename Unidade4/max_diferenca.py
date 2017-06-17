# coding: utf-8
# max diferença
# raquel ambrozio

elementos = int(raw_input())
assert elementos > 1
lista = []
maior_diferenca = 0

for i in range(elementos):
  n = float(raw_input())
  lista.append(n)

for i in range(len(lista)-1):
  resultado = lista[i] - lista[i+1]
  if resultado > maior_diferenca:
    a = lista[i]
    b = lista[i+1]

print "%.1f e %.1f" % (a, b)
