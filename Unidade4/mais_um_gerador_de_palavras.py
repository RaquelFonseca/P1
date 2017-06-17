# coding: utf-8
# mais um gerador de palavras
# raquel ambrozio

palavra1 = raw_input()
palavra2 = raw_input()
assert len(palavra1) == len(palavra2)
nova_palavra = ""

for i in range(len(palavra1)):
    if palavra1[i] != palavra2[i]:
      nova_palavra += palavra1[i] + palavra2[i]
    else:
      nova_palavra += palavra1[i] + palavra1[i] * i

print nova_palavra
      
    
    
