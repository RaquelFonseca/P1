# coding: utf-8
# 
# Cria login

def cria_login(nome):
	nome = nome.split()
	login = nome[0].lower()
	for i in nome:
		if i != nome[0] and i[0].upper() == i[0]:
			login += i[0].lower()
	return login
	
while True:
	nome = raw_input()
	if nome == "fim":
		break
	print "%s: %s" % (nome, cria_login(nome))
