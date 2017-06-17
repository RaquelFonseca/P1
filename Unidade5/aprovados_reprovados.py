# coding: utf-8
# aprovados reprovados
# raquel ambrozio

aprovados = 0
reprovados = 0
soma_aprovados = 0
soma_reprovados = 0


alunos = int(raw_input())

while alunos > 0:
  nota = float(raw_input())
  alunos -= 1
  if nota >= 7.0:
    aprovados += 1
    soma_aprovados += nota
  else:
    reprovados += 1
    soma_reprovados += nota

print "Reprovados: %d" % reprovados

if reprovados > 0:
  media_reprovados = soma_reprovados / reprovados
  print "Média: %.1f" % media_reprovados

print

print "Aprovados: %d" % aprovados

if aprovados > 0:
  media_aprovados = soma_aprovados / aprovados
  print "Média: %.1f" % media_aprovados

  
