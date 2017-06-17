# coding: utf-8
# media 9999
# raquel ambrozio

soma = 0
quantidade = 0

while True:
    numero = int(raw_input())
    if numero == 9999:
        break
    soma += numero
    quantidade += 1.0

if quantidade != 0: 
    media = soma / quantidade
    print "%.1f" % media 
