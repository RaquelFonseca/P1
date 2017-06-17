# coding: utf-8
# collatz
# raquel ambrozio

n = int(raw_input())

while True:
  if n  % 2 != 0:
    n = 3 * n + 1
    print n
  else:
    n = n / 2
    print n
  if n == 1:
    break
