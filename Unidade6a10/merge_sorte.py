# MERGE SORTE ========================


# coding: utf-8


def merge(lista1, lista2):
    i = 0
    j = 0
    lista_resultado = []
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            lista_resultado.append(lista1[i])
            i += 1
        else:
            lista_resultado.append(lista2[j])
            j += 1
    if i < len(lista1):
        lista_resultado += lista1[i:]
    elif j < len(lista2):
        lista_resultado += lista2[j:]
    return lista_resultado
            
        
l1 = [2, 0, 3]
l2 = [1, 4, 7]
print merge(l1,l2)
