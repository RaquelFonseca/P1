# coding: utf-8
# senha_segura_letras_repetidas
# raquel ambrozio

senha = raw_input()
nova_senha = ""

for i in range(len(senha)):
        if senha[i] == " ":
                nova_senha += senha[i]
        else:
                nova_senha += senha[i] * 2

print nova_senha

if len(nova_senha) >= 13:
        print "senha segura"
else:
        print "senha insegura"
