# coding: utf-8
# pontos cnh
# raquel ambrozio

infracoes = raw_input().split()
pontos = 0

for i in range(len(infracoes)):
  if infracoes[i] == "Gravissima":
    pontos += 7
  elif infracoes[i] == "Grave":
    pontos += 5
  elif infracoes[i] == "Media":
    pontos += 4
  elif infracoes[i] == "Leve":
    pontos += 3

if pontos >= 20:
  print "%d pontos. CNH supensa." % pontos
else:
  print "%d pontos. CNH valida." % pontos 
