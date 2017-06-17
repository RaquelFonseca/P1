# coding: utf-8
# resumo compras
# raquel ambrozio

precos = []
soma = 0

while True:
  valor = raw_input()
  if valor == "fim":
    break
  precos.append(valor)
  soma += float(valor)

media = soma / len(precos)
mais_caro = float(precos[0])

for i in range(len(precos)):
  if float(precos[i]) > mais_caro:
    mais_caro = float(precos[i])

print "O valor medio por produto foi R$ %.2f. O produto mais caro custa R$ %.2f." % (media, mais_caro)
  
