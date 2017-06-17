# coding: utf-8
# divisores_pares
# raquel ambrozio

numero = int(raw_input())

for i in range(1, numero):
         if i % 2 == 0 and numero % i == 0:
                  print i

