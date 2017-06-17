# coding: utf-8

# Lanche mais pedido

def lanchemaispedido(pedidos):
	cont_mais = 0
	cont = 0
	for i in range(len(pedidos)):
		for j in range(len(pedidos)):
			if pedidos[i] == pedidos[j]:
				cont += 1
		if cont > len(pedidos) / 2:
			cont_mais = cont
			indice = i
			return pedidos[indice]

ines = ['basadad', 'casa', 'salada', 'salada', 'salada', 'tapioca']

print lanchemaispedido(ines)

			
				
