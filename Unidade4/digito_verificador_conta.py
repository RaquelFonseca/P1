# coding: utf-8
# digito verificador conta
# raquel ambrozio

numero = raw_input()
soma = 0


for i in range(len(numero)):
  soma += int(numero[i])
  if soma % 11 == 10:
    verificador = "x"
  else:
    verificador = str(soma % 11)

print "%s-%s" % (numero, verificador)

