#coding: utf-8
# letras coincidentes
# raquel ambrozio

# coding: utf-8

palavra1 = raw_input()
palavra2 = raw_input()

print "Letras coincidentes"

if len(palavra1) == len(palavra2):
	cont = 0
	for i in range(len(palavra1)):
		if palavra1[i] == palavra2[i]:
			cont += 1
			letra = palavra1[i]
			posicao = i + 1
			print "'%s' na posição %d" % (letra, posicao) 

	if cont != 0:
                total_letras = len(palavra1) + len(palavra2)
                porc = (cont * 100.0) / total_letras
                print "Total de letras coincidentes: %d (%d%%)" % (cont, porc)
        else:
                print "Total de letras coincidentes: 0 (0%)"




elif len(palavra1) < len(palavra2):
	cont = 0
	for k in range(len(palavra1)):
		if palavra1[k] == palavra2[k]:
			cont += 1
			letra = palavra1[k]
			posicao = k + 1
			print "'%s' na posição %d" % (letra, posicao)

	if cont != 0:
        	total_letras = len(palavra1) + len(palavra2)
        	porc = (cont * 100.0) / total_letras
        	print "Total de letras coincidentes: %d (%d%%)" % (cont, porc)
	else:
		print "Total de letras coincidentes: 0 (0%)"


elif len(palavra1) > len(palavra2):
        cont = 0
        for g in range(len(palavra2)):
                if palavra2[g] == palavra1[g]:
                        cont += 1
                        letra = palavra2[g]
                        posicao = g + 1
                        print "'%s' na posição %d" % (letra, posicao)


	if cont != 0:
        	total_letras = len(palavra1) + len(palavra2)
                porc = (cont * 100.0) / total_letras
                print "Total de letras coincidentes: %d (%d%%)" % (cont, porc)
        else:
        	print "Total de letras coincidentes: 0 (0%)"
             
                
