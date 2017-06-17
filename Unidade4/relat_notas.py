# coding: utf-8
# relatorio de notas
# Raquel Ambrozio da Fonseca

n_alunos = int(raw_input())
assert n_alunos > 1

aprovados = 0
reprovados = 0
per_apro = 0
per_repro = 0
n_m_apro = 0
n_m_repro = 0
media1 = 0
media2 = 0


for i in range(1, n_alunos+1):
    notas = float(raw_input())
    if notas >= 5.0:
        aprovados += 1
        per_apro = aprovados * 100.0 / n_alunos
        media1 += notas
        n_m_apro = media1 / float(aprovados)
    else:
        reprovados += 1
        per_repro = reprovados * 100.0 / n_alunos
        media2 += notas
        n_m_repro = media2 / float(reprovados)
print "aprovados: %d (%.1f%%)" % (aprovados, per_apro)
if reprovados >= 1: 
    print "nota média aprovados: %.2f" % n_m_apro
    print "reprovados: %d (%.1f%%)" % (reprovados, per_repro)
    print "nota média reprovados: %.2f" % n_m_repro
else:
    print "nota média aprovados: %.2f" % n_m_apro
    print "reprovados: %d (%.1f%%)" % (reprovados, per_repro)
    
        
        
    
