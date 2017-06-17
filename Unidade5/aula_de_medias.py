# coding: utf -8
# aula de medias
# raquel ambrozio

valores = []
soma = 0

while True:

  valor = float(raw_input())
  valores.append(valor)
  soma += valor

  if soma > 100:
    break
  

media = soma / len(valores)

print "Quantidade de numeros lidos: %d" %  len(valores)
print "Soma dos numeros lidos: %.2f " % soma
print "Media = %.2f" % float(media)
print

print "Abaixo da media"

for i in range(len(valores)):
  if valores[i] < media:
    print "%.2f (%do)" % (valores[i], i+1)

print

print "Acima da media"

for i in range(len(valores)):
  if valores[i] > media:
    print "%.2f (%do)" % (valores[i], i+1)
    
    

  
