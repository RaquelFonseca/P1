# coding: utf-8
# fila por altura
def insere_na_fila(fila, nome, altura):
	tupla = nome, altura
	for i in range(len(fila)):
		if fila[i][1] >= altura:
			fila.insert(i, tupla)
			return
	fila.append(tupla)
fila = [("maria", 1.05), ("joao", 1.09), ("ana", 1.16)]
insere_na_fila(fila, "jose", 1.12)
assert fila == [("maria", 1.05), ("joao", 1.09), ("jose", 1.12), ("ana", 1.16)]
