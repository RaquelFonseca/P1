# coding: utf-8
# produto_posições
# Raquel Ambrozio

numero = raw_input()
somapar = 0
somaimpar = 0
for i in range(len(numero)):
    if i % 2 == 0:
        somapar += int(numero[i])
    else:
        somaimpar += int(numero[i])
print "%05d" % (somapar * somaimpar)
