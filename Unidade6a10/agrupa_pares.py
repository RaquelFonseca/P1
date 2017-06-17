# coding: utf-8

# agrupa pares

def agrupa_pares_impares(lista):
	dicionario = {"pares": [], "impares": []}
	for num in lista:
		if num % 2 == 0:
			dicionario["pares"].append(num)
		else:
			dicionario["impares"].append(num)
	return dicionario
	
assert agrupa_pares_impares([10, 24, 97, 88]) == {"pares":[10, 24, 88], "impares":[97]}
assert agrupa_pares_impares([11, 23, 35]) == {"pares":[ ], "impares":[11, 23, 35]}
