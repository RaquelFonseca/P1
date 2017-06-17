# programa para verificar se um numero é primo

entrada = int(raw_input())
if entrada <= 0:
       finalizar = "numero invalido"
       exit()

# i sera o divisor inicial
i = 1

# j sera o contador de ocorrencias
j = 0

# nenhum numero real vai ser divisivel por um numero maior que sua metade
entrada1 = entrada / 2

while i <= entrada:
       if entrada % i == 0:
              print ('eh divisivel por %d' % i)
              i += 1
              j += 1
       if i >= entrada1:
              # damos a i, o valor da variavel entrada, pois o proximo divisor sera o proprio numero
              i = entrada
              print ("eh divisivel por %d" % i)
              i += 1
              j += 1
       else:
              i += 1
if j == 2:
                     print "o numero eh primo"
else:
                     print "o numero nao eh primo"
