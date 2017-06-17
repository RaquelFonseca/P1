# coding: utf-8
# area do cilindro
# Raquel Ambrozio
print "Cálculo da Superfície de um Cilindro"
print "---"
diametro_cilindro = float(raw_input("Medida do diâmetro? "))
altura_cilindro = float(raw_input("Medida da altura? "))
print "---"
import math
area_base = math.pi * ((diametro_cilindro/2)**2)
area_lateral = altura_cilindro * 2 * math.pi * (diametro_cilindro/2)
area_cilindro = area_base*2 + area_lateral
print "Àrea calculada: %.2f" % area_cilindro

