# coding: utf-8
# passagem aerea
# raquel ambrozio

# entrada:
distancia = float(raw_input())
aliquota = float(raw_input())
# processamento:
valor = distancia * aliquota + 51
d25 = valor * 0.25
valor25 = valor - d25
d5 =  valor * 0.95
p6 = d5 / 6.0
p10 = valor / 10.0
# saida:
import math
print "Valor da passagem: R$ %.2f" % valor
print
print '''Pagamento:
1. Á vista. R$ %.2f
2. Esm 6 parcelas. Total: R$ %.2f
    6 X R$ %.2f
3. Em 10 parcelas. Total: R$ %.2f
    10 x R$ %.2f''' % (valor25, d5, p6, valor, p10)


