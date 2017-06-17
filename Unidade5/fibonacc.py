# serie de fibonacci

atual = 0
anterior = 0
proximo = 1
limite = int(raw_input())

while atual < limite:
       print proximo
       anterior = atual
       atual = proximo
       proximo = anterior + atual
       
