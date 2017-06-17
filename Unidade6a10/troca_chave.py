# coding: utf-8
# 
# troca chave

def troca_chave(dic):
    novodic = {}
    for chave, valor in dic.items():
        novodic[valor] = chave
    return novodic
    
assert troca_chave({1:2}) == {2:1}
assert troca_chave({1:2, 2:3, 3:4}) == {2:1, 3:2, 4:3}
assert troca_chave({ '@':'V','a':'v', 'n':'o'}) == { 'V':'@','v':'a', 'o':'n'}
