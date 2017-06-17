# -*- coding: cp1252 -*-
# união listas


def uniao_listas(l1, l2):
    for i in range(len(l1)-1, -1, -1):
        if l1[i-1] == l1[i]:
                l1.pop(i)
    for i in range(len(l2)):
        if l2[i] != l1[i] :
            l1.append(l2[i])
            

l1 = [2, 1, 3, 3, 4]
l2 = [2]
uniao_listas(l1, l2)
print l1
