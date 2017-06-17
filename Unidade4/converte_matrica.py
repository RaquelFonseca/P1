# coding: utf-8
# converte_matricula
# raquel ambrozio

matricula = raw_input()
soma = "1"

for i in range(1,len(matricula)):
    soma += matricula[i]
    if i == 4:
        soma += "0"

print soma

        
