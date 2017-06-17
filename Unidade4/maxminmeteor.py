# coding: utf-8
# maxminmeteor
# raquel ambrozio

valores = raw_input().split()
horarios = raw_input().split()

maior = float(valores[0])
menor = float(valores[0])

for i in range(len(valores)):

  if float(valores[i]) > maior:
    maior = float(valores[i])
    hora_ma = horarios[i]
  if float(valores[i]) < menor:
    menor = float(valores[i])
    hora_me = horarios[i]

print "Min: %s %.2f" % (hora_me, menor)
print "Max: %s %.2f" % (hora_ma, maior)
    
