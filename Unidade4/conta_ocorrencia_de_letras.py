# coding: utf-8
# conta ocorrencia de letra
# raquel ambrozio

letra = raw_input()

palavras = raw_input()
ocorrencia = 0
posicao = []
por = 0

print "Letra %s:" % letra

for i in range(len(palavras)):
  if palavras[i] == letra:
    ocorrencia += 1
    por = ocorrencia * 100.0 / len(palavras)
    posicao.append(i+1)

print "%d ocorrencia(s) (%.2f%%)" % (ocorrencia, por)
if ocorrencia > 0:
  print "Na(s) posição(ções): (%s)" % str(posicao)[1:-1]


