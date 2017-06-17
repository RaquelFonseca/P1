# coding: utf-8
# codigo formulario
# raquel ambrozio

codigo = raw_input()
codigo_formulario = "verdadeiro"

for i in range(len(codigo)-1):
  if int(codigo[i]) % 2 == 0 and int(codigo[i+1]) % 2 == 0 or int(codigo[i]) % 2 != 0 and int(codigo[i+1]) % 2 != 0:
    codigo_formulario = "falso"

print "%s: %d algarismos." % (codigo_formulario, len(codigo))
  
    
    
  
