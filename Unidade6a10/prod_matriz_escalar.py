# coding: utf-8

# Prod_matriz_escalar

MxN = raw_input().split()
M = int(MxN[0])
N = int(MxN[1])

matriz = []
for lin in range(M):
	matriz.append(raw_input().split())

K = int(raw_input())

for i in range(M):
	for j in range(N):
		matriz[i][j] = int(matriz[i][j]) * K
		
	
print matriz
