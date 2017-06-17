# -*- coding: cp1252 -*-
#def soma_matrizes(m1, m2):
 #   matriz_soma = []
  #  for i in range(len(m1)):
   #     soma = []
    #    for j in range(len(m1[0])):
     #       soma.append(m1[i][j] + m2[i][j])
      #  matriz_soma.append(soma)
    #return matriz_soma
            



#def soma_colunas(m):
    #lista_soma = []
    #for i in range(len(m)):
      #  soma = 0
     #   linha = 0
    #    for j in range(len(m[0])):
   #         soma += m[linha][i]
  #          linha += 1
 #       lista_soma.append(soma)
#    return lista_soma
        


#def diagonal_principal(M):
#   diagonal_principal = []
#    for i in range(len(M)):
 #       for j in range(len(M[0])):
 #           if i == j:
  #              diagonal_principal.append(M[i][j])
   # return diagonal_principal

#def triangulo_superior(m):
 #   abaixo_diagonal_p = []
  #  for i in range(len(m)):
   #     for j in range(len(m[0])):
    #        if i > j:
     #           abaixo_diagonal_p.append(m[i][j])
   # for i in range(len(abaixo_diagonal_p)):
    #    if abaixo_diagonal_p[i] == 0:
     #       return True
    #return False

#def zera_diagonal(m):
 #   for i in range(len(m)):
  #      m[i][i] = 0

#def busca_matriz(m, e):
 #   for i in range(len(m)):
  #      for j in range(len(m[0])):
   #         if m[i][j] == e:
    #            resultado = (i, j)
     #           return resultado
    #return None

#def zera_negs(M):
 #   for i in range(len(M)):
  #      for j in range(len(M[0])):
   #         if M[i][j] < 0:
    #            M[i][j] = 0



#def jogo_da_velha(tabuleiro):
 #   for i in range(len(tabuleiro)):
  #      if tabuleiro[0][i] or tabuleiro[1][i] or tabuleiro[2][i] or tabuleiro[i][0] or tabuleiro[i][1] or tabuleiro[i][2] or tabuleiro[i][i] == "O":
  #          resultado = "O ganhou"
  #          break
  #          
  #      elif tabuleiro[0][i] or tabuleiro[1][i] or tabuleiro[2][i] or tabuleiro[i][0] or tabuleiro[i][1] or tabuleiro[i][2] or tabuleiro[i][i] == "X":
  #          resultado = "X ganhou"
  #          break
#
   #     linha = 0
    #    coluna = len(tabuleiro[0])-1
    #    secundaria = []
     #   for j in range(len(tabuleiro[0])):
     #       secundaria.append(tabuleiro[linha][coluna])
     #       linha += 1
      #      coluna -= 1
       # for k in range(len(secundaria)):
        #    if secundaria[k] == "O":
         #       resultado = "O ganhou"
         #   elif secundaria[k] == "X":
          #      resultado = "X ganhou"
           # else:
            #    resultado = "Ninguém ganhou"
    #return resultado
        

        
#tabuleiro = [['X', 'O', 'X'],['O', 'O', 'X'],['X', 'O', 'O'] ]

#print jogo_da_velha(tabuleiro)
palavra = "AAAAAAAbbbbbCCCCddDDD"

maior = 0
for i in range(len(palavra)):
    contador = 0
    if palavra[i] != palavra[i-1]:
        contador += 1
    if  maior <= contador:
        maior = contador
print maior

M1 = [[1,2,3],\
       [1,5,6],\
        [0,3,9]]

M2 = [[-3, 0, 1],\
        [1, -2, 9],\
        [3, 4, -5]]
    



