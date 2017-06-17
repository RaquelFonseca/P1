# coding: utf-8
# encontrar numeros primos
# raquel ambrozio

limite = int(raw_input())

for i in range(2, limite+1):
               for h in range(2, i):
                              if i % h == 0:
                                             print "%d = %d * % d" % (i, h, i/h)
                                             break
               else:
                              # encontrou o numero primo
                              print i, 'eh um numero primo'

