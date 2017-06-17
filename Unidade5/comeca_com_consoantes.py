# coding: utf-8
# comeca com consoante
# raquel ambrozio

palavra = ""
palavras = []
comeca_consoantes = 0

while palavra != "***":
  palavra = raw_input()
  if palavra[0] not in "AaEeIiOoUu*":
    comeca_consoantes += 1
  

print "Palavras: %d" % comeca_consoantes


