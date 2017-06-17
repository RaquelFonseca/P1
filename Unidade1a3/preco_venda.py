# coding: utf-8
# preço de venda
# Raquel Ambrozio

custo = float(raw_input())
despesas = float(raw_input())
lucro = float(raw_input())
impostos = float(raw_input())
comissoes = float(raw_input())
descontos = float(raw_input())
encargos = float(raw_input())
preco = (custo + despesas + lucro) * 100 / (100 - impostos - comissoes - descontos - encargos)
import math

print "Preço de venda é R$ %.2f (%.2f + R$ 0.61)" % (math.ceil(preco),math.ceil( preco))
