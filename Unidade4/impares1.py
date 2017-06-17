# coding: utf-8
# impares_1
# raquel ambrozio

for numeros in range(1, 101, 2):
    if numeros % 3 == 0 or numeros % 5 == 0:
        numeros = "*"
    print numeros
    
