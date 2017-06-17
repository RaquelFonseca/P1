# coding: utf-8
# media limite
# raquel ambrozio

numeros = []

while True:
       entrada = raw_input()
       if entrada == "-":
              break
       numeros.append(entrada)

limite = float(raw_input())

soma = 0
media = 0
contador = 0
i = 0

while media <= limite and i < len(numeros):
       soma +=  float(numeros[i])
       contador += 1
       media = soma / contador
       i += 1

if media > limite:
       media = soma / contador
       print "media = %.1f" % media
       print "num = %d" % contador

else:
       print "limite nao alcancado"
