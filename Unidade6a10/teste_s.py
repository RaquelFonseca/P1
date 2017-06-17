# coding: utf-8

import os


def cria_matriz(tamanho_da_matriz):
    matriz = []
    for i in range(tamanho_da_matriz):
        linha_matriz = []
        for j in range(tamanho_da_matriz):
            if i == j:
                linha_matriz.append(1*2)
            else:
                linha_matriz.append(0)
        matriz.append(linha_matriz)
    return matriz

tamanho = int(raw_input())

print cria_matriz(tamanho)

os.system("Pause")
