# coding: utf-8
# serie fibonacci
# raquel ambrozio

a= 0
b = 1
limite = int(raw_input())
while b < limite:
               b = a + b
               a = b + a
               print b
               print a
               
