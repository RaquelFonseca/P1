# coding: utf-8
# sequencia dna
# Raquel Ambrozio

contador = 0
dna1 = raw_input()
dna2 = raw_input()
for i in range(len(dna1)):
    if dna1[i] == dna2[i]:
        contador += 1
if contador > len(dna2) / 2:
    print  "sim"
else:
    print "nao"

    
    

