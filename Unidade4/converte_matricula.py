# coding: utf-8
# converte_matricula
# raquel ambrozio

matricula = raw_input()
soma = 1

for i in range(1, len(matricula)):
        soma += int(matricula[i])
        if i == 5:
                soma += 0
print soma
