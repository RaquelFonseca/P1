# coding: utf-8
# exercicios resolvidos
# raquel ambrozio

exercicios_resolvidos = raw_input().split()
alunos = raw_input().split()

maior = int(exercicios_resolvidos[0])
aluno = alunos[0]

for i in range(len(exercicios_resolvidos)):
  if int(exercicios_resolvidos[i]) > maior:
    maior = int(exercicios_resolvidos[i])
    aluno = alunos[i]

print aluno, maior
