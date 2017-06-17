# coding: utf -8
# remove letras alternadas
# Raquel Ambrozio
var = ""
palavra = raw_input()
for i in range(0, len(palavra), 2):
     var += palavra[i]
     print var
