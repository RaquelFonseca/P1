# coding: utf-8

# Número de disciplinas estilo problema

def num_disciplinas(entrada, disciplinas, horarios):
	for i in range(len(disciplinas)):
		if entrada[0] != disciplinas[i] and entrada[1] != horarios[i]:
			if len(entrada) == 2:
				disciplinas.append(entrada[0])
				horarios.append(entrada[1])
			else:
				adicionar = 0
				for j in range(2, len(entrada)):
					if entrada[j] not in disciplinas:
						 adicionar += 1
				if adicionar == 0:
					disciplinas.append(entrada[0])
					horarios.append(entrada[1])
	return (disciplinas, horarios)
	
disciplinas = []
horarios = []

num_disci = int(raw_input())

for num in range(num_disci):
	entrada = raw_input().split()
	if len(disciplinas) == 0 and len(entrada) == 2:
		disciplinas.append(entrada[0])
		horarios.append(entrada[1])
	else:
		valor = num_disciplinas(entrada, disciplinas, horarios)
		disciplinas = valor[0]
		horarios = valor[1]

print len(disciplinas)
