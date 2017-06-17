# coding: utf-8
# salário bruto e líquido
# Raquel Ambrozio

nome = raw_input()
horas_extras = int(raw_input())
salario_minimo = float(raw_input())
valor_horaex = float(raw_input())

salario_horaex = valor_horaex * horas_extras
salario_bruto = 4 * salario_minimo + salario_horaex
descontosinss = salario_bruto* 0.88
desconto = salario_bruto - descontosinss
desconto_ir = salario_bruto*0.80
desconto2 = salario_bruto - desconto_ir
salario_liquido = salario_bruto - desconto - desconto2

print "O Salário Bruto de Antonio é de R$ %.2f" % salario_bruto
print "O Salário Líquido de Antonio é de R$ %.2f" % salario_liquido
