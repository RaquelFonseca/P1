# coding: utf-8
# menor palavra dos extremos
# raquel ambrozio

quantidade = int(raw_input())
assert quantidade > 1
palavras = []

for i in range(quantidade):
  palavra = raw_input()
  palavras.append(palavra)

menor = ""

for i in range(len(palavras)):
  if palavras[0] < palavras[-1]:
    menor = palavras[0]
  elif len(palavras[0]) == len(palavras[-1]):
    menor = 
  else:
    menor = palavras[-1]

print menor
