meses =  ["jan", "fev", "mar", "abr", "mai", "jun",
          "jul", "ago", "set", "out", "nov", "dez"] 
mes_lucro1 = []
for i in range(len(meses)):
    mes_lucro = raw_input().split()
    mes_lucro1.append(mes_lucro)

for j in range(len(mes_lucro1)):
    lucro = int((mes_lucro1[0]) - (mes_lucro1[1]))
print meses[i], lucro
