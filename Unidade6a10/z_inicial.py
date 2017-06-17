# coding: utf-8

# Z_inicial

def z_inicial(lista):
	cont = 0
	for palavra in lista:
		if palavra[0] in "zZ":
			cont += 1
	return cont
	
lista1 = ["zumbi","Zeca","Recife"]
lista2 = ["livro", "cd", "software"]
assert z_inicial(lista1) == 2
assert z_inicial(lista2) == 0
		
