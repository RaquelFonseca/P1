# coding: utf-8
# unidades de medidas
# Raquel Ambrozio

medida = float(raw_input())
polegadas =  medida * 36 / 0.9144 
pes = polegadas / 12
jardas = pes / 3
print "Jardas: %.3f yd" % jardas
print "Pés: %.3f ft" % pes
print "Polegada: %.3f in" % polegadas 
