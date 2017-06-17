# coding: utf-8
# remove letras iguais
# raquel ambrozio

palavra1 = raw_input()
palavra2 = raw_input()
palavra3 = ""


for i in palavra2:
               if i not in palavra1:
                              palavra3 += i

print palavra3
                              
