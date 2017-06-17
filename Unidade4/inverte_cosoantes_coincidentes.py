# coding: utf-8
# inverte consoantes coincidentes
# raquel ambrozio

palavra1 = raw_input()
palavra2  = raw_input()
coincidentes = ""
print "cosoantes coincidentes"

for i in range(len(palavra1)):
  if palavra1[i] == palavra2[i]:
    if palavra1[i] not in "AaEeIiOoUu":
      coincidentes += palavra1[i]
      print '"%s" na posicao %d' % (palavra1[i],i+1)


coincidentes_invertidas = coincidentes[::-1]
if coincidentes == coincidentes[::-1]:
  conincidentes_invertidas = ""
print 'Inverso das coincidentes "%s"' %  coincidentes_invertidas
