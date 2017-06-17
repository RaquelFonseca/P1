# coding: utf -8
# relatorio de notas
# raquel ambrozio

total_alunos = int(raw_input())
assert total_alunos > 1
aprovados = 0
reprovados = 0
n_aprovados = 0
n_reprovados = 0

for i in range(total_alunos):
        nota = float(raw_input())
        if nota >=  5.0:
                aprovados +=1
                n_aprovados += nota
              
        else:
                reprovados +=1
                n_reprovados += nota
               

perc_aprovados =  (aprovados * 100.0) / total_alunos
perc_reprovados = (reprovados * 100.0) / total_alunos
n_m_aprovados =  n_aprovados / aprovados
if reprovados > 0:
        n_m_reprovados =  n_reprovados / reprovados


print "aprovados: %d (%.1f%%)" % ( aprovados, perc_aprovados)
print "nota média aprovados: %.2f" % n_m_aprovados
print "reprovados: %d (%.1f%%)" % (reprovados, perc_reprovados)

if reprovados > 0:
       
        print "nota média reprovados: %.2f" % n_m_reprovados




                
        
