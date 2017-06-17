# coding: utf-8
# get items

def get_items(valores, indices):
    lista = []
    for i in range(len(indices)):
        if indices[i] < len(valores):
            lista.append(valores[indices[i]])
        else:
            lista.append(None)
    return lista
        

valores = [10, 20, 14, 17, 22, 9, 32]
indices = [2, 5, 0]

assert get_items(valores, indices) == [14, 9, 10]

print get_items(valores, indices)

valores = [10, 20, 14, 17, 22, 9, 32]
indices = [2, 5, 8, 0]

assert get_items(valores, indices) == [14, 9, None, 10]

print get_items(valores, indices)
