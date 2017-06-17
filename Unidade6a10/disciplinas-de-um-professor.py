# coding: utf-8
# 
# Disciplinas de um professor

def disciplina(alocacao, professor):
	

alocacao = {("P1", 4): ['Jorge', 'Dalton','Wilkerson'],
         ("LP1", 4): ['Jorge', 'Dalton', 'Eliane', 'Wilkerson'],
         ("EVOL", 2): ['Dalton'],
         ("IC", 4): ['Eliane', 'Joseana'],
         ("P2", 4): ['Livia', 'Raquel', 'Nazareno'],
         ("GRAFOS", 2): ['Patricia']}

assert set(disciplinas(alocacao, "Dalton")[0]) == set(['P1', 'LP1', 'EVOL'])
assert disciplinas(alocacao, "Dalton")[1] == 10
assert set(disciplinas(alocacao, "Eliane")[0]) == set(['LP1', 'IC'])
assert disciplinas(alocacao, "Eliane")[1] == 8

