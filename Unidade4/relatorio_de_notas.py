# coding: utf-8
# relatorio de chuvas
# raquel ambrozio

indices = raw_input().split()
meses = raw_input().split()

maior = float(indices[0])
menor = float(indices[0])
soma = 0


for i in range(len(indices)):
  soma += float(indices[i])

  if float(indices[i]) >= maior:
    maior = float(indices[i])
    mes_ma = meses[i]
    
  if float(indices[i]) <= menor:
    menor = float(indices[i])
    mes_me = meses[i]

media = soma / len(indices)
    

print "Minimo: %.2f (em %s)" % (menor, mes_me)
print "Maximo: %.2f (em %s)" % (maior, mes_ma)
print "--- Abaixo da media"

for i in range(len(indices)):
  if float(indices[i]) <= media:
    print "%s: %.2f" % (meses[i], float(indices[i]))
  
