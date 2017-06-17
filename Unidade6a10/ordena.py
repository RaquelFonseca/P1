# coding: utf-8
# ordena


def ordena(lista):

    for j in range(1, len(lista)):
        chave = lista[j]
        i = j - 1

        while i >= 0 and lista[i] > chave:
            lista[i + 1] = lista[i]
            i -= 1
        lista[i + 1] = chave

    resultado = lista[::-1]
    return resultado

vetor = []

while True:

    palavra = raw_input()

    if palavra == "####":
        break
    vetor.append(palavra)
    ordena(vetor)

    for i in range(len(ordena(vetor))):
        if palavra == ordena(vetor)[i]:
            print "*", ordena(vetor)[i]
        else:
            print ordena(vetor)[i]
    print "----"

