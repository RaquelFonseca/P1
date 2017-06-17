# coding: utf-8
# prova final 1
# raquel ambrozio

total_alunos = int(raw_input())
alunos_final = 0
nota_para_final = 0

for i in range(total_alunos):
        nota = float(raw_input())
        if nota > 4.0 and nota < 7.0:
                alunos_final += 1
                nota_para_final += nota

porcentagem = alunos_final * 100.0 / total_alunos
if alunos_final > 0:
        media = nota_para_final / alunos_final

print "%d (%.1f%%) alunos na final" % ( alunos_final, porcentagem)
if alunos_final > 0:
        print "Média das notas: %.1f" % media
