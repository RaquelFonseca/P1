# coding: utf-8
palavra1 = raw_input()
palavra2 = raw_input()
coincidentes = 0
total = ((len(palavra1)) + (len(palavra2)))
print "Letras coincidentes"
for i in range(1,len(palavra1)+1):
    if palavra1[i-1] == palavra2[i-1]:
        coincidentes += len(palavra1[i-1])
        print "'%s'" % palavra1[i-1], "na posição %d" % i
    else:
        coincidentes += 0
    porcentagem = (coincidentes * 100)/total
print "Total de Letras coincidentes: %d (%d%%) " % (coincidentes,porcentagem)
