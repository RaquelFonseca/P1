# coding: utf-8
# divisores
# raquel ambrozio

numero = int(raw_input())
assert numero > 0

for i in range(1, numero):
        if numero % i ==0:
                print i
