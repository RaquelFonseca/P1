# coding: utf-8
# quadrado na circunferencia
# Raquel Ambrozio

import math
raio = float(raw_input())
area_circulo = math.pi * raio ** 2
area_quadrado = (math.sqrt(raio**2 +raio**2))**2
area_nao_comum = area_circulo - area_quadrado
print "Àrea não comum: %.5f" % area_nao_comum
