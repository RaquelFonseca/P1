salario_antigo = float(raw_input('Salário atual? '))
aumento = float(raw_input("Aumento projetado (em %)? "))
percentual_inss = float(raw_input("Nova contribuição da previdência (em %)? "))
novo_salario = float((salario_antigo * aumento) / 100.0)+ salario_antigo
contribuicao = ((novo_salario * percentual_inss) /100.0)
salario_liquido = novo_salario - contribuicao
print 
print "Dados do NOVO salário"
print "==="
print "Salário: R$ %.2f" % (novo_salario)
print "Contribuição previdenciária: R$ %.2f (%.1f%%)" % (contribuicao, percentual_inss)
print "Salário líquido: R$ %.2f" % salario_liquido
