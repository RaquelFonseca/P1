#coding: utf-8
# difs acima  media
# raquel ambrozio

soma = 0
lista_diferenca = []

while True:
  sequencia = raw_input().split()
  if int(sequencia[0]) == 0 and int(sequencia[1]) == 0:
    break
  soma += abs(int(sequencia[0]) - int(sequencia[1]))
  lista_diferenca.append(abs(int(sequencia[0]) - int(sequencia[1])))

media = soma / len(lista_diferenca)

for i in range(1, len(lista_diferenca)):
  if lista_diferenca[i] > media:
    print i + 1

  
                                    
