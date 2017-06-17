# coding:  utf-8
# numero mais de uma vez
# raquel ambrozio da fonseca

k = int(raw_input())
n = raw_input().split()
posicao = 0

for i in range(len(n)):
  if int(n[i]) == k:
    posicao = i + 1
  elif int(n[i]) != k:
    posicao = "-1"
    
print posicao
