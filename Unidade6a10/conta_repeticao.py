#coding:utf-8
# conta_repeticoes


# armazena os valores da lista sem  duplicacoes, valores a ser pesquisados
def lista_valores_pesquisados(lista):
    assert lista != []
    lista_numeros = lista[:]

    for i in range(len(lista_numeros)-1,-1,-1):
        if lista_numeros.count(lista_numeros[i]) > 1:
             lista_numeros.pop(i)

    return   lista_numeros


# conta a ocorrencia de um numero na lista
def conta_repeticao_numero(lista_numeros, lista):
    assert lista != []
    assert lista_numeros != []

    lista_repeticoes = []
    
    for valor in lista_numeros:
        lista_repeticoes.append('%d: %d'%(valor,lista.count(valor)))

    return  lista_repeticoes   
    


# dados lidos
contador = int(raw_input())
controle = 0
lista_lida = []

while controle < contador:
    valor = int(raw_input())
    lista_lida.append(valor)
    controle += 1


# monta as listas
numeros_pesquisados = lista_valores_pesquisados(lista_lida)
numero_repetidos = conta_repeticao_numero(numeros_pesquisados, lista_lida)

# imprime o resultado  final
for valor in numero_repetidos:
    print valor
    
    

