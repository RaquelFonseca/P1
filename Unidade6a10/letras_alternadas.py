# coding: utf-8
# letras alternadas


def letras_alternadas(palavra):
    nova = ""
    for i in range(len(palavra)):
        if i % 2 == 0:
            nova += palavra[i]
    return nova

n = int(raw_input())
for i in range(n):
    palavras = raw_input()
    print letras_alternadas(palavras)
        
    
