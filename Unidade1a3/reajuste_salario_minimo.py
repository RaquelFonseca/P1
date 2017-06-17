# coding: utf-8
# reajust_salario_minimo
# Raquel Ambrozio

salario_atual = float(raw_input("Valor atual? "))
novo_salario = float(raw_input("Novo valor? "))
reajuste = 100 * (novo_salario - salario_atual) / salario_atual
print "Reajuste de %.1f%%" % reajuste
