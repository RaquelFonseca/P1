# coding: utf-8
# area da esfera
# Raquel Ambrozio
print "Cálculo da superfície de uma esfera"
print "---"
diametro = float(raw_input("Medida do diâmetro? "))
import math
area_esfera = 4 * math.pi * ((diametro/2)**2)
print "---"
print "Àrea calculada: %.2f" % area_esfera
