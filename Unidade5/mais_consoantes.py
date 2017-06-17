# coding: utf-8
# mais consoantes
# raquel ambrozio

lista_palavras = []
while True:
  palavra = raw_input()
  lista_palavras.append(palavra)
  contav = 0
  contac = 0
  for i in palavra:
    if i in "aeiou":
      contav += 1
    else:
      contac += 1
  if contac > contav:
      break
print len(lista_palavras)
