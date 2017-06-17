# coding: utf-8

# Peso Ideal com Função

def calcula_peso(sexo, altura):
	if sexo in "Mm":
		ideal = 72.7 * altura - 58
		return ("Homem", ideal)
	elif sexo in "Ff":
		ideal = 62.1 * float(altura) - 44.7
		return ("Mulher", ideal)
		
while True:
	dados = raw_input().split()
	if dados[0] == "****":
		break
	sexo = dados[0]
	altura = float(dados[1])
	print "%s: peso ideal é %.1f" % calcula_peso(sexo, altura)
