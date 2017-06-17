# codinfg: utf-8
# menor diferenca
quantidade = int(raw_input())
numeros = []
for i in range(quantidade):
	numero = float(raw_input())
	numeros.append(numero)
ind_m =  1
for i in range(2, quantidade):
	m_d = abs(numeros[ind_m] - numeros[ind_m-1])
	dif = abs(numeros[i] - numeros[i-1])
	if dif > m_d:
		ind_m = i
print "%.1f e %.1f" % (numeros[ind_m-1], numeros[ind_m])
