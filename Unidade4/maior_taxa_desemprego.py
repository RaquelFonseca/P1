# coding: utf-8
# maior taxa desemprego
# raquel ambrozio

n = int(raw_input())
paises = []
desemprego = []

for i in range(n):
  paises.append(raw_input())
 
for i in range(n):
  desemprego.append(float(raw_input()))

maior = desemprego[0]

for i in range(len(desemprego)):
  if desemprego[i] > maior:
    maior = desemprego[i]
    print "%s: %.1f%%" % (paises[i], desemprego[i])

  
