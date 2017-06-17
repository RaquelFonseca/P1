# coding: utf-8

# Colegas de sala

def colegas_de_sala(salasprofs, professor):
	lista = []
	for prof in salasprofs:
		if salasprofs[professor] == salasprofs[prof] and prof != professor:
			lista.append(prof)
	return lista
	
salasprofs = {
'Franklin': 206,    'Tiago':206,        'Eliane': 206,
'Adalberto':209,    'Wilkerson':207,    'Dalton': 204,
'Jorge': 204
}

assert set(colegas_de_sala(salasprofs, 'Franklin')) == set(['Tiago', 'Eliane'])
assert set(colegas_de_sala(salasprofs, 'Adalberto')) == set([])
