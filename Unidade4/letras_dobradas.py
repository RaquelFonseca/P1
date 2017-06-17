# coding: utf-8
# letras dobradas
# raquel ambrozio

quantidade = int(raw_input())
palavras = []
dobradas = []
n_dobradas = []

for i in range(quantidade):
  p = raw_input()
  palavras.append(p)

for palavra in palavras:
  repetidas = False
  for i in range(len(palavra)-1):
    if palavra[i] == palavra[i+1]:
      repetidas = True
  if repetidas:
    dobradas.append(palavra)
  else:
    n_dobradas.append(palavra)

print "%d palavra(s) com letras dobradas:" % len(dobradas)
print palavras[i]








  
  
