# coding: utf-8
# tabela quadrados div_3
# Raquel Ambrozio

x = int(raw_input())
y = int(raw_input())
if x > y:
    print "---"
for i in range(x, y+1):
    ii = i ** 2
    if ii % 3 == 0:
        print i, i ** 2, "*"
    else:
        print i, i ** 2
    
   
    
