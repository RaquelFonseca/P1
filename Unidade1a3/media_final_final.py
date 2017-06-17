# coding: utf-8
# Cálculo de médias
# Raquel Ambrozio
print "== Estágio 1 =="
peso1 = float(raw_input("Peso? "))
nota1 = float(raw_input("Nota? "))
print "== Estágio 2 =="
peso2 = float(raw_input("Peso? "))
nota2 = float(raw_input("Nota? "))
print "== Estágio 3 =="
peso3 = float(raw_input("Peso? "))
nota3 = float(raw_input("Nota? "))
print "== Resultados =="
media_parcial = peso1 * nota1 + peso2 * nota2 + peso3 * nota3
print media_parcial
nota_final1 = (5 -(media_parcial*0.6)) / 0.4
nota_final2 = (7 -(media_parcial*0.6)) / 0.4
print "Nota na final, na média 5.0 = %d" % nota_final1
print "Nota na final, na média 7.0 = %d" % nota_final2

