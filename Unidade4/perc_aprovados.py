
# perc_aprovados
# raquel ambrozio

total_alunos = int(raw_input())
assert total_alunos > 0
aprovados = 0
reprovados = 0

for i in range(total_alunos):s
        media = raw_input()
        if media in "Ff" or float(media) < 5.0:
                reprovados +=1
        else:
                aprovados += 1

porcentagem_aprovados = aprovados * 100 / total_alunos

print "%d%% (%d/%d) de aprovados" % (porcentagem_aprovados, aprovados, total_alunos)                
