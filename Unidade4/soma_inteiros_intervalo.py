# coding: utf-8
# soma inteiros intervalo
# raquel ambrozio

a = int(raw_input())
b = int(raw_input())
assert a <= b
soma = 0

for i in range(a, b+1):
  soma += i

print "Soma: %d" % soma
