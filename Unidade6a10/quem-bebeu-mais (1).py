# coding: utf-8
# 
# Quem bebeu mais

sabado = [[1, 2, 3], [0, 1, 0], [3, 1, 2]]
domingo = [[2, 0, 3], [0, 2, 1], [1, 1, 2]]

def quem_bebeu_mais(sabado, domingo):
    lista = []
    for i in range(len(sabado[0])):
        soma = 0
        for j in range(len(sabado)):
            soma += sabado[j][i] + domingo[j][i]
            
        lista.append(soma)
    
    ind = 0
    for i in range(len(lista)):
		if lista[ind] < lista[i]:
			ind = i
    return ind + 1
			
print quem_bebeu_mais(sabado, domingo)
