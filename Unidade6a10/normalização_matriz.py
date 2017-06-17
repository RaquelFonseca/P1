# coding: utf-8
# 
# normalização_matriz

def normaliza_matriz(M):
	soma = 0
	cont = 0
	for i in range(len(M)):
		for j in range(len(M[0])):
			soma += M[i][j]
			cont += 1
			media = soma / cont
			
	for i in range(len(M)):
		for j in range(len(M[0])):
			M[i][j] = M[i][j] - media
	 
m = [
        [20, 5, 3],
        [ 6, 4, 2],
        [ 3, 1, 9],
]
normaliza_matriz(m)

assert m == [
        [ 15,  0, -2],
        [  1, -1, -3],
        [ -2, -4,  4],
]
