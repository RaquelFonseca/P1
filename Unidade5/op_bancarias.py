# coding: utf-8
# op bancariais
# raquel ambrozio

dados = raw_input().split()
saldo_atual = float(dados[1])

while True:
  valores = raw_input().split()
  if valores[0] == "3":
    break
  if valores[0] == "1":
    saldo_atual -= float(valores[1])
  if valores[0] == "2":
    saldo_atual += float(valores[1])

print "Saldo de R$ %.2f na conta de %s" % (saldo_atual, dados[0])
