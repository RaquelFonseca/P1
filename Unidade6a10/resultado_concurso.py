# Raquel Ambrozio
# resultado concurso
# coding: utf-8



def reclassifica(resultado_preliminar, recursos):
    for i in range(len(resultado_preliminar)):
        if recursos[1] > resultado_preliminar[i][1] or (recursos[1] == resultado_preliminar[1] and recursos[2] > resultado_preliminar[i][2]):
            resultado_preliminar.insert(i, recursos)
            return
    resultado_preliminar.append(recursos)
  


preliminar = [("pedro", 9.5, 35), ("joao", 8.2, 26), ("ana", 7.1, 25)]
recursos = [("carlos", 10.0, 45), ("julio", 8.2, 25), ("aline", 7.0, 23)]

for i in recursos:
        reclassifica(preliminar, i)
print preliminar
