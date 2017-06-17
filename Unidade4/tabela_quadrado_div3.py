# coding: utf -8
# tabela_quadrados_div3
# raquel ambrozio

numero_x = int(raw_input())
numero_y = int(raw_input())

if numero_x > numero_y:
                print "---"

for i in range(numero_x, numero_y+1):
        if i**2 % 3 == 0:
                print i, i ** 2, " *"
        else:
                print i, i**2
   
