# coding: utf-8
# quant_par_impar_1
# raquel ambrozio

numero = raw_input().split()
par = 0
soma_par = 0
impar = 0
soma_impar = 0

for i in range(len(numero)):
        if int(numero[i]) % 2 == 0:
                par += 1
                soma_par += float(numero[i])
        else:
                impar += 1
                soma_impar += float(numero[i])

print "pares: %d" % par
print "impares: %d" % impar

if par != 0:
        media = soma_par / par
        print "media pares: %.1f" % media
else:
        print "media pares: 0.0"
if impar != 0:
        media = soma_impar / impar
        print "media impares: %.1f" % media
else:
        print "media impares: 0.0"
