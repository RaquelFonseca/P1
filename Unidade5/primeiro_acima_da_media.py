# coding: utf-8
# primeiro acima da media
# raquel ambrozio

sequencia = ""
lista = []
soma = 0

while sequencia != "fim":
               sequencia = raw_input()

               if sequencia != "fim":
                              soma += float(sequencia)
                              lista.append(float(sequencia))


media = soma / len(lista)
maior = 0
posicoa = 0


for i in range(len(lista)):
               if lista[i] > media:
                              maior = lista[i]
                              posicao = i
                              break

print "%d, %.2f > %.2f" % (posicao, maior, media)
               
               


