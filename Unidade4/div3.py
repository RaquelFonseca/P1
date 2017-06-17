# coding: utf-8
# tabela_quadrados_div3
# Raquel Ambrozio

x = int(raw_input())
y = int(raw_input())
for i in range(x, y+1):
    if i**2 % 3 == 0:
        print i, i**2 + "*"
