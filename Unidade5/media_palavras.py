# coding: utf-8
# media palavras
# raquel ambrozio

soma = 0
quantidade = 0

while True:
    palavra = raw_input()
    if palavra == "fim":
        break
    quantidade += 1
    soma += len(palavra)

if quantidade != 0:       
    resultado = (float(soma) / quantidade)
    print "%.1f" % resultado
else:
    print "0.0"

