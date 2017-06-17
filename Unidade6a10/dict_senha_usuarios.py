# coding: utf-8

# dict_senhas_usuarios

def quantidade_usuarios(cadastro):
	cont = 0
	for elem in cadastro:
		if elem != 9999:
			cont += len(cadastro[elem])
	return cont

lsd = {1234:['Andrey'], 1226:['Nazareno', 'Livia'], 9999:['administrador'] }
deq = {1114:['Ana', "joao"] }

assert quantidade_usuarios(lsd) == 3
assert quantidade_usuarios(deq) == 2
