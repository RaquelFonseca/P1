# soma  valores
# coding: utf-8

def f(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma

contador = 0
numeros = []

while True:
    numero = int(raw_input("valor? "))
    contador += 1
    if numero == -1:
        break
    numeros.append(numero)

media = f(numeros) / len(numeros)
print "Quantidade de valores: %d" % contador
print "Soma dos valores: %.1f" % f(numeros)
print "Média: %.1f" % media
