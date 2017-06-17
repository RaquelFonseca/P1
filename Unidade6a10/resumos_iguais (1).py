# coding: utf-8

# Resumos iguais

def agrupa_resumos_iguais(lista):
	dicionario = {}
	for numeros in lista:
		numeros = str(numeros)
		soma = 0
		for num in numeros:
			soma += int(num)
		numeros = int(numeros)
		soma = str(soma)
		if soma not in dicionario.keys():
			dicionario[soma] = [numeros]
		else:
			dicionario[soma].append(numeros)
	return dicionario
	
lista1 = [60, 343, 19, 1230, 51, 123]
print agrupa_resumos_iguais(lista1)
