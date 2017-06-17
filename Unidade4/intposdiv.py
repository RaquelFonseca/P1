# coding: utf-8
# inteiros positivos divisiveis
# Raquel Ambrozio

a = int(raw_input())
b = int(raw_input())
k = int(raw_input())

for i in range(a, k+1):
    if i % a == 0 and i % b == 0:
        print i
        
