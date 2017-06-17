# coding: utf-8
# ataque mais positivo
# raquel ambrozio

quantidade = int(raw_input())
times = []
gols = []
soma = 0

for i in range(quantidade):
  nome_time = raw_input()
  times.append(nome_time)
  gols_time = int(raw_input())
  soma += gols_time
  gols.append(gols_time)

media = float(soma) / len(gols)
melhor_ataque = 0

for i in range(len(gols)):
  if gols[i] > melhor_ataque:
    melhor_ataque = gols[i]

print "Time(s) com melhor ataque (%d gol(s))" % melhor_ataque

for i in range(len(gols)):
  if gols[i] == melhor_ataque:
    print times[i]

print 
print "Media de gols marcados : %.1f" % media


  
