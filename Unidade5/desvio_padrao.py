# coding: utf-8
# desvio padrao
# raquel ambrozio

valores = []
soma = 0


while True:
  valor = raw_input()
  if valor == "fim":
    break

  soma += float(valor)
  valores.append(valor)


media = soma / len(valores)
quadrados = 0
soma2 = 0


for i in range(len(valores)):
  desvio = int(valores[i]) - media
  quadrados = desvio ** 2
  soma2 += quadrados


variancia = soma2 / len(valores)



import math



dp = math.sqrt(variancia)



print "m = %.2f" % float(media)
print "dp = %.2f" % float(dp)

  
