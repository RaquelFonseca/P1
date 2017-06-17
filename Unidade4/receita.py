#coding: utf-8
# receita
# raquel ambrozio

receitas = []
despesas  = []

for mes in range(12):
        valores = raw_input().split()
        receitas.append(float(valores[0]))
        despesas.append(float(valores[1]))

for i in range(len(receitas)):
        print " %4.1f" % (receitas[i] - despesas[i])       
