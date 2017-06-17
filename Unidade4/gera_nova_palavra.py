# coding: utf-8
# gera nova palavra
# raquel ambrozio

palavra = raw_input()
nova_palavra0 = ""
nova_palavra1 = ""

for i in range(len(palavra)):
  if i % 2 == 0:
    nova_palavra0 += palavra[i]
  else:
    nova_palavra1 += palavra[i]
    
  


#for i in range(len(palavra)):
 # if i % 2 != 0:
  #  nova_palavra1 += palavra[i]

nova = nova_palavra0 + nova_palavra1

print nova
