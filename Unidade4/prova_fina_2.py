# coding: utf-8
# prova final 2
# raquel ambrozio

numero = int(raw_input())
final = []
falta = []

for i in range(numero):
  nome = raw_input()
  nota = float(raw_input())
  if nota < 7.0:
    final.append(nome)
    conta = (500 - (60 * nota)) / 40.0
    falta.append(conta)
    

porcentagem = len(final) * 100 / numero


for i in range(len(final)):
  print final[i],":" , falta[i]

print "%d (%.1f%%) alunos na final" % (len(final), porcentagem)

  
