# coding: utf-8
# sequencia_dna
# raquel ambrozio

dna1 = raw_input()
dna2 = raw_input()
letras_iguais = 0

for i in range(len(dna1)):
        if dna1[i] == dna2[i]:
                letras_iguais += 1
if letras_iguais >= (len(dna1)) / 2:
        print "sim"
else:
        print "não"
