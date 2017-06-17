# coding: utf-8

# Agenda Telefonica

agend_nom = []
agend_num = []

def insertion_sort(lista1):
	for j in range(1, len(lista1)):
		chave = lista1[j]
		i = j - 1
		while lista1[i] > chave and i >= 0:
			lista1[i + 1] = lista1[i]
			i -= 1
		lista1[i + 1] = chave
	return lista1

while True:
	comando = raw_input()
	if comando == "finalizar":
		break
	elif comando == "inserir":
		quant = int(raw_input())
		for i in range(quant):
			agend_nom.append(raw_input())
			agend_num.append(raw_input())
	elif comando == "buscar":
		nome = raw_input()
		indice = "X"
		for i in range(len(agend_nom)):
			if agend_nom[i] == nome:
				print "Nomé: %s\nFone: %s" % (agend_nom[i], agend_num[i])
				print "----------"
		if indice == "X":
			print "Nome inexistente"
			print "----------"
			
	else:
		for i in range(len(agend_nom)):
			print "Nome: %s\nFone: %s" % (agend_nom[i], agend_num[i])
