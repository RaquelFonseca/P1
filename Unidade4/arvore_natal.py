# coding: utf-8
# arvore_natal
# raquel

num = int(raw_input())
num_esp = num - 1
num_ast = 1

for i in range (0, 2*num, 2):
	print " "*num_esp+"*"*num_ast
	num_ast = i+3
	num_esp -= 1
print " "*(num-1)+"*"
        
