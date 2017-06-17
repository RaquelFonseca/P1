#coding:utf-8

palavra = 'alomundo'
busca = 'mu'
posicao = 0 # vou precisar para comparar com a proxima letra da palavra, sem voltar para o inicio dela
contida = False # controle de verificacao

for index in range(len(palavra)):
	if busca[0] == palavra[index]:
		posicao = index #atualizo a posicao
		contida = True # atualizo o controle
		if contida == True:
			if busca[1] == palavra[posicao + 1]: #comparo as letras
				print busca + ' esta contida em ' + palavra
				break
			else:
				print 'nao esta contida'
		else:
			print 'nao esta contida'
			break
