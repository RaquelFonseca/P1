# coding: utf-8
# maior e menor nota
# raquel ambrozio

alunos = int(raw_input())
nomes = []
notas = []
maior_nota = 0
menor_nota = 10


for i in range(alunos):
  nomes.append(raw_input())
  notas.append(float(raw_input()))
  if notas[i] > maior_nota:
    maior_nota = notas[i]
  if notas[i] < menor_nota:
    menor_nota = notas[i]

for j in  range(len(nomes)):
  if notas[j] == maior_nota:
    print "%s: %.1f (maior nota)" % (nomes[j], notas[j])
  elif notas[j] == menor_nota:
    print "%s: %.1f (menor nota) " % (nomes[j], notas[j])
  else:
    print "%s: %.1f" % (nomes[j], notas[j])
    
    
    
  
  

