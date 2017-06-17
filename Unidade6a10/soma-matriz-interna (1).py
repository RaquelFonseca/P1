# coding: utf-8
# 
# Soma matriz interna

M1 = [[1, 3, 5, 2, 7, 8, 30, -5],
	  [9, -8, 20, 3, 0, 5, -7, 12],
	  [43, 22, -2, -3, -10, 5, 20, 0],
	  [1, 2, 3, 4, 5, 6, 7, 8],
	  [10, 20, -30, -40, 50, 60, 70, -80]]
	  
def soma_matriz_interna(matriz, inicio, fim):
	soma = ""
	for j in range(inicio[0], fim[0] + 1):
		for i in range(inicio[1], fim[1] + 1):
			soma += " %s" % matriz[j][i]
	return soma

p1 = (1,2)
p2 = (3,4)

print soma_matriz_interna(M1, p1, p2)

"""
assert soma_matriz_interna(M1, p1, p2) == 20 + 3 + 0 + -2 + -3 + -10 + 3 + 4 + 5  
assert soma_matriz_interna(M1, (0,0), (1,1)) == 1 + 3 + 9 + -8


M2 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
assert soma_matriz_interna(M2, (1,1),(2,2)) == 5 + 6 + 8 + 9"""
