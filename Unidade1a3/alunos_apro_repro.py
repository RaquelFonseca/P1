# coding: utf-8
# Média de Alunos Aprovados e Reprovados
# Raquel Ambrozio da Fonseca / Programação 1 / 2014

print "Análise da Turma"

alunos_aprovados = int(raw_input("Qual o número de aprovados? "))
alunos_reprovados = int(raw_input("Qual o número de reprovados? "))

total_alunos = alunos_aprovados + alunos_reprovados
perc_aprovados = (alunos_aprovados * 100.0) / total_alunos
perc_reprovados = (alunos_reprovados * 100.0) / total_alunos

print "==="
print "Total de alunos na turma: ",total_alunos
print "Aprovados: %d = %.1f%%" % (alunos_aprovados, perc_aprovados)
print "Reprovados: %d = %.1f%%" % (alunos_reprovados, perc_reprovados)
