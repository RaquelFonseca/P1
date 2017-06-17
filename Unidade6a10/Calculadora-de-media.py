# coding: utf-8

# Calculadora de Medias

def realiza_medias(entrada, valores):
	soma = 0
	if entrada == "MA":
		for i in valores:
			soma += float(i)
		media = soma / len(valores)
		return "Média Aritmética: %.4f" % (media)
	elif entrada == "MG":
		soma = 1
		for i in valores:
			soma *= float(i)
		media = soma ** (1. / len(valores))
		return "Média Geométrica: %.4f" % (media)
	elif entrada == "MH":
		for i in valores:
			soma += 1 / float(i)
		media = len(valores) / soma
		return "Média Harmônica: %.4f" % (media)

while True:
	entrada = raw_input().split()
	if entrada[0] == "Q":
		break
	valores = raw_input().split()
	for i in range(len(entrada)):
		print realiza_medias(entrada[i], valores)
	print "----"	
