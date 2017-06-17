# coding: utf-8
# carregamentos
# raquel ambrozio

carregamentos = int(raw_input())
tempo_i = []
tempo_f = []
maior_tempo = 0

for i in range(carregamentos):
  tempos = raw_input().split()
  tempo_i.append(int(tempos[0]))
  tempo_f.append(int(tempos[1]))

contador = 0

for i in range(len(tempo_f)):
  diferenca = tempo_f[i] - tempo_i[i]
  if diferenca > maior_tempo:
    maior_tempo = diferenca
    contador = i + 1

print "carregamentos %d" % contador
  
  
  
