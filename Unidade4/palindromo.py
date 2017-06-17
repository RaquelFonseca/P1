# coding: utf-8
# palindromo
# raquel ambrozio

string = raw_input()
tamanho = len(string)


for i in range(tamanho/2):
               if string[i] != string[len(string)-1-i]:
                              print "'%s' (%d) != '%s' (%d)" % (string[i], i+1, string[len(string)-1-i], tamanho-i)
