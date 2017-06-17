# coding: utf-8
# maioridade penal
# raquel ambrozio

nomes = raw_input().split()
idades = raw_input().split()
assert len(nomes) == len(idades)

for i in range(len(idades)):
  if int(idades[i]) >= 18:
    print nomes[i]
  

