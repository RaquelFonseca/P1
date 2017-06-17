# coding: utf-8
# perimetro de um triangulo a apartir da distância
#Raquel Ambrozio

ax = int(raw_input())
ay = int(raw_input())
bx = int(raw_input())
by = int(raw_input())
cx = int(raw_input())
cy = int(raw_input())
import math
dab = math.sqrt((bx-ax)**2+(by-ay)**2)
dbc = math.sqrt((cx-bx)**2+(cy-by)**2)
dca = math.sqrt((ax-cx)**2+(ay-cy)**2)
perimetro = dab + dbc + dca
print "o perímetro é de %.2f" % perimetro
