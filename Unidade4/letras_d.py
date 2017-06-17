quantidade = int(raw_input())
dobradas = []
n_dobradas = []

for i in range(quantidade):
    palavra = raw_input()
    palavra.append(p)
for palavras in palavra:
            repetidas = False
for i in range (len(palavra)-1):
                    if palavra[i] == palavra[i+1]:
                        repetidas = True
                    if repetidas == True:
                        dobradas.append(palavra)
                    else:
                        n_dobradas.append(palavra)
