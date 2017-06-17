# coding: utf-8
# zero_americano

def f(lista):
	somatorio = 0
	for i in range(len(lista)):
		somatorio += int(lista[i])
	return somatorio

while True:
	num = raw_input().split()
	if num[0] == "0":
		break
	soma = f(num)
	resultado  = soma % len(num)
	if resultado == 0:
		resultado = len(num)
	print resultado
