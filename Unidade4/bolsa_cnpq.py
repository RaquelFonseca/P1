# coding: utf-8
# bolsa cnpq

meses =["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
bolsa = 500
gastos = raw_input().split()
resto = 0
lista_resto = []



for i in range(len(meses)):
  saldo = bolsa - int(gastos[i])
  resto += saldo
  lista_resto.append(resto)

maior = 0

for indice in range(len(lista_resto)):
  
  if lista_resto[indice] >= lista_resto[maior]:
    
    maior = indice
print meses[maior]


