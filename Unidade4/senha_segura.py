# coding: utf-8
# senha segura
# raquel ambrozio


senha = raw_input()
digitos_i = []
digitos_p = []

for i in range(len(senha)):
  if i % 2 == 0:
    digitos_i.append(int(senha[i]))
  else:
    digitos_p.append(int(senha[i]))

for i in range(len(digitos_i)):
  if digitos_i[i] % 2 != 0 and digitos_p[i] % 2 == 0:
    segura = "segura"
  else:
    segura = "insegura"
print segura

  
