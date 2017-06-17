# coding: utf-8
# 
# Filtra Alunos

def filtra_alunos(alunos, inscritos, nota_min):
	total = len(alunos)
	for aluno in alunos[::-1]:
		if aluno not in inscritos or aluno[1] < 7.0:
			alunos.pop()
	return total - len(alunos)
	
inscritos = [121, 123, 124]
alunos = [ (120,8.0), (121,7.5), (122,5.0), (123,6.0), (124,9.0), (125,4.0) ]

assert filtra_alunos(alunos, inscritos, 7.0) == 4
assert alunos == [ (121,7.5), (124,9.0) ]
