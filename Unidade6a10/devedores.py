# coding: utf-8

# devedores

def devedores(contas):
	cont = 0
	for pessoa in contas:
		if contas[pessoa] < 0:
			cont += 1
	return cont
	
contas = { 'Ana':1000, 'Antonio':500, 'William':0, 'Carlos':2500, 'Kate':-1300 }
assert devedores(contas) == 1
