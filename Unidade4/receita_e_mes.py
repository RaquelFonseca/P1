# coding: utf-8
# receita e mes
# raquel ambrozio

receitas = []
despesas = []
meses = ["jan", "fev", "mar", "abr", "mai", "jun",
                   "jul", "ago", "set", "out", "nov", "dez"]

for mes in range(12):
        valores = raw_input().split()
        receitas.append(float(valores[0]))
        despesas.append(float(valores[1]))

for i in range(len(meses)):
        print "%s %4.1f" % (meses[i], (receitas[i] - despesas[i]))
