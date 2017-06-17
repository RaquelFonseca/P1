# coding: utf-8

# Espaço em Disco

def bytes_pra_mega(numero):
	convertido = float(numero) / (1024 ** 2)
	return convertido

def porc_uso(lista):
	porcentagem = []
	somador = 0
	for i in range(len(lista)):
		somador += lista[i]
	for i in range(len(lista)):
		porcentagem.append(lista[i]/somador)
	return porcentagem
	
login = []
espaco = []

while True:
	dados = raw_input().split()
	if dados[0] == "fim":
		break
	login.append(dados[0])
	espaco.append(bytes_pra_mega(dados[1]))
	
porcentagem = porc_uso(porcentagem)

print "SPLab - Espaço utilizado pelos usuários"
print "---------------------------------------------"
print "Nr., Usuário, Espaço Utilizado, %% do uso"

for i in range(len(login)):
	print "%d, %s, %.2f, %.2f%%" % (i + 1, login[i], espaco[i], porcentagem)
	
	
