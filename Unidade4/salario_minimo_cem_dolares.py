# coding: utf-8
# salario minimo cem dolares
# raquel ambrozio


# anos

ano_inicial = int(raw_input())
ano_final = int(raw_input())
anos = (ano_final - ano_inicial) + 1

salario = []

for i in range(anos):
  dolar = float(raw_input())
  salario.append(dolar)

abaixo = 0
acima = 0
soma_ab = 0
soma_ac = 0

for j in range(len(salario)):
  if salario[j] <= 100:
    abaixo += 1
    soma_ab += salario[j]
  else:
    acima += 1
    soma_ac += salario[j]

if abaixo > 0:
  media_ab = soma_ab / abaixo
  porcentagem_ab = 100 * abaixo / anos
print "%d ano(s) abaixo (%d%% dos anos)" % (abaixo, porcentagem_ab)
print "media dos anos abaixo: U$ %.2f" % media_ab
if acima > 0:
  media_ac = soma_ac / acima
  porcentagem_ac = 100 * acima / anos
print "%d ano(s) acima (%d%% dos anos)" % (acima, porcentagem_ac)
print "media dos anos abaixo: U$ %.2f" % media_ac
    
    

