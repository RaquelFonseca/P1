# coding: utf-8
# relatorio de notas 2
# raquel ambrozio

total_alunos = int(raw_input())
aprovados = 0
nota_media_aprovados = 0
reprovados = 0
nota_media_reprovados = 0

for i in range(total_alunos):
  nota = float(raw_input())

  if nota >= 5.0:
    aprovados += 1
    nota_media_aprovados += nota

  else:
    reprovados += 1
    nota_media_reprovados += nota

media_aprovados = nota_media_aprovados / float(aprovados)
porcentagem_aprovados = aprovados * 100.0 / total_alunos

print "aprovados : %d (%.1f%%)" % (aprovados, porcentagem_aprovados)
print "nota media aprovados : %.2f" % media_aprovados

if reprovados > 0 :
  media_reprovados = nota_media_reprovados / float(reprovados)
  porcentagem_reprovados = reprovados * 100.0 / total_alunos
  print "reprovados : %d (%.1f%%)" % (reprovados, porcentagem_reprovados)
  print "nota media reprovados : %.2f" % media_reprovados

  
