# coding: utf-8
# comeca letra a
# raquel ambrozio

def comeca_a(palavra):
    if palavra[0] == "A":
        return palavra
    
quantidade = 0

while True:
    palavra = raw_input()
    if palavra[0] == "A":
        break
    quantidade += 1

print "-" * 3
print "%d %s" % (quantidade, palavra)
