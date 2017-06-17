# coding: utf-8
# maioridade penal modificada
# raquel ambrozio

dados = raw_input().split()
quantidade = 0

for i in range(1, len(dados), 2):
  if int(dados[i]) >= 18:
    quantidade += 1
    print "%s: %s" % (dados[i-1], dados[i])

print "%d pessoa(s) com maioridade penal" % quantidade
