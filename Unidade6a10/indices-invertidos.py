# coding: utf-8

# Indice Invertido

def gera_indice_invertido(texto):
	dic = {} # @variaveis_comentam
	palavras = texto.split()
	for i in range(len(palavras)):
		if palavras[i] in dic:
			dic[palavras[i]].append(i)
		else:
			dic[palavras[i]] = [i]
	return dic

texto = "eu prefiro que todos tirem notas boas do que eu ter que fazer um novo miniteste"

bala = gera_indice_invertido(texto)

print bala
