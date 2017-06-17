lista = []
palavras = raw_input()
contador = 0
lista = palavras.split("#")

palavras = []
for i in lista:
    palavras.append(i)


for i in range(len(palavras)-1):
    if palavras[i][0] == palavras[i+1][0]:
        contador += 1
        

print contador
