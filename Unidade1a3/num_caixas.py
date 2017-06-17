capacidade = float(raw_input("Capacidade de revestimento? "))
print "== Dados do vão a revestir =="
comprimento = float(raw_input("Comprimento? "))
largura = float(raw_input("Largura? "))
altura = float(raw_input("Altura? "))

area_total = (comprimento*altura*2) + (altura*largura*2) + largura *comprimento

num_caixas = area_total / capacidade
print
import math

print "== Resultados =="
print "Área total a revestir: %.1f m2" % area_total
print "Número de caixas: %d" % int(math.ceil(num_caixas))



