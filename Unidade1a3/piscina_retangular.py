# coding: utf-8
# Pidcina Retangular
# Raquel Ambrozio


comprimento = float(raw_input())
largura = float(raw_input())
altura = float(raw_input())
m2 = 1 / 2.5
ladrilhos = largura*comprimento + (comprimento*altura*2)+(altura*largura*2)
total = int(ladrilhos*m2)
import math

print "%s caixa (s)" % (math.floor(total))


