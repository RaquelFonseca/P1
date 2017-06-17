import math
angulo_inicial = float(raw_input())
passo = float(raw_input())
n = int(raw_input())
tabela_angulos = []

for i in range(n):
  seno = math.sin(math.radians(angulo_inicial))
  cosseno = math.cos(math.radians(angulo_inicial))
  tabela_angulos.append("|%6.1f|%7.5f|%7.5f|" %( angulo_inicial, seno, cosseno))
  angulo_inicial += passo

a = "Angulo"
b = "Seno"
c = "Cosseno"
print "I%7sI%7sI%7sI" % (a, b, c)

for valores in tabela_angulos:
  print  valores
