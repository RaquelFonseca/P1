# coding: utf -8
# remove letras alternadas
# raquel ambrozio

palavra = raw_input()
nova = ""

for i in range(len(palavra)):
        if i % 2 == 0:
                nova += palavra[i]
print nova
