# coding: utf-8
# organiza notas
# Raquel Ambrozio

quantidade = int(raw_input())
matriculas = []
notas = []
soma = 0

while quantidade > 0:
    matriculas.append(int(raw_input()))
    nota = float(raw_input())
    notas.append(nota)
    soma += nota
    quantidade -= 1

media = soma / len(notas)

print ""

for i in range(len(matriculas)-1):
    for j in range(len(matriculas)-1-i):
        if matriculas[j] > matriculas[j+1]:
            matriculas[j], matriculas[j+1] = matriculas[j+1], matriculas[j]
            notas[j], notas[j+1] = notas[j+1], notas[j]

for i in range(len(matriculas)):
    print "%d: %.1f" % ( matriculas[i], notas[i])

print "Media da turma: %.1f" % media
