# coding: utf-8
# abaixo da media
# raquel ambrozio

numeros = []
soma = 0


while True :
  numero = raw_input()
  if numero == "fim":
    break
  soma += int(numero)
  numeros.append(numero)

media = float(soma) / len(numeros)
print "%.2f" % media


for i in range(len(numeros)):
  if int(numeros[i]) < media:
    print "%d %d" % (i+1, int(numeros[i]))
