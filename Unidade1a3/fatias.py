# coding: utf-8
# Números de fatias
# Raquel Ambrozio da Fonseca

num_convidados = int(raw_input())
opcao1 = 32 / num_convidados
opcao1_resto = 32 % num_convidados
opcao2 = 32.0 / num_convidados

print ('Opção 1: %d fatias cada, %d de resto %.2f') % (opcao1, opcao1_resto, opcao2)
print ('Opção 2: %.2f fatias cada') % opcao2
