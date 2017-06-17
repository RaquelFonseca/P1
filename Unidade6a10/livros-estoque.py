# coding: utf-8
# 
# Livros Estoque

def ausentes(dicionario):
	cont = 0
	for livro in dicionario:
		if dicionario[livro] == 0:
			cont += 1
	return cont
	
livros = { "Metamorfose": 0, "O Principe": 0, "Vigiar e Punir": 0, "Dumbo": 22}
assert ausentes(livros) == 3
