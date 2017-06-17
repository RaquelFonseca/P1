# coding: utf-8
# converte senha
# raquel ambrozio

senha = raw_input()
resto_senha = senha[1:]
nova_senha = senha[0]
cont = 0


for i in range(len(resto_senha)):
  if resto_senha[i] in "Aa":
    nova_senha += "4"
    cont += 1
  elif resto_senha[i] in "Ee":
    nova_senha += "3"
    cont += 1
  elif resto_senha[i] in "Ii":
    nova_senha += "1"
    cont += 1
  elif resto_senha[i] in "Oo":
    nova_senha += "0"
    cont += 1
  else:
    nova_senha += resto_senha[i]

print "%s (%d troca(s))" % (nova_senha, cont)

