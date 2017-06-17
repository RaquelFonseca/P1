# coding: utf-8
# numero_perfeito
# raquel ambrozio

numero = int(raw_input())
soma = 0
for i in range(1, numero):
        if numero % i == 0:
                soma += i
if soma == numero:
        print "%d eh um numero perfeito." % numero
else:
        print "%d nao eh número perfeito." % numero

                
                
        
        
