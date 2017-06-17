# Coding: utf-8
nota1 = float(raw_input())
nota2 = float(raw_input())
nota3 = float(raw_input())
peso1 = float(raw_input())
peso2 = float(raw_input())
peso3 = float(100-(peso2+peso1))
nota1 = nota1/100.0
nota2 = nota2/100.0
nota3 = nota3/100.0

print "Média Final: %.1f" %(nota1*peso1 + nota2*peso2 +nota3*peso3)
