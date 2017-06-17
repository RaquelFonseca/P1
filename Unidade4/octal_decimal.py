# coding: utf-8
# octal decimal
# raquel ambrozio

numero_octal = raw_input()
expoente = len(numero_octal)
decimal = 0


for i in range(len(numero_octal)):
        expoente -= 1
        decimal0 = int(numero_octal[i]) * (8 ** expoente)
        decimal += decimal0
        print "%d * 8^ %d = %d" % (int(numero_octal[i]), expoente, decimal0)

print "%d(8) = %d(10)" % (int(numero_octal), decimal)
        
