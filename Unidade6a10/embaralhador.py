# coding: utf-8
#
# Embaralhador

# Corrigir a instrução I que ta dando errado
# Ver como imprime varios elementos de uma lista em uma linha só

def instrucoes(sequencia, instrucao):
	nova_seq = []
	if instrucao == "GE":
		nova_seq = [sequencia[-1]]
		for i in range(len(sequencia) - 1):
			nova_seq.append(sequencia[i])
		return nova_seq
	elif instrucao == "GD":
		for i in range(1, len(sequencia)):
			nova_seq.append(sequencia[i])
		nova_seq.append(sequencia[0])
		return nova_seq
	elif instrucao == "I":
		for i in range(1, len(sequencia) - 1, 2):
			nova_seq.append(sequencia[i - 1])
			nova_seq.append(sequencia[i])
		return nova_seq

sequencia = raw_input().split()

while True:
	instrucao = raw_input()
	if instrucao == "fim":
		break
	sequencia = instrucoes(sequencia, instrucao)
	print sequencia
