# coding: utf-8

# Copa

def joga_em(selecao, cidade, grupos, estadios):
	for grupo in grupos:
		if selecao in grupos[grupo]:
			for estadio in estadios:
				if grupo == estadio[0] or grupo == estadio[1]:
					if cidade in estadios[estadio]:
						return True
	return False

			

grupos = {"A":["Brasil","Croácia", "México","Camarões"], 
          "B":["Espanha", "Holanda", "Chile", "Austrália"], 
          "C":["Colômbia", "Grécia", "Costa do Marfim", "Japão"], 
          "D":["Uruguai", "Costa Rica", "Inglaterra", "Austrália"], 
          "E":["Suiça", "Equador", "França", "Honduras", ], 
          "F":["Argentina", "Bósnia", "Irã", "Nigéria"],
          "G":["Alemanha", "Portugal", "Gana", "Estados Unidos"],
          "H":["Bélgica", "Argélia", "Rússia", "Córeia do Sul"]
         }

estadios = {("A","B"): ["Belo Horizonte", "Fortaleza", "Salvador"],
            ("C","D"): ["Rio de Janeiro", "Recife", "Fortaleza", "Salvador"],
            ("E","F"): ["Brasília", "São Paulo", "Rio de Janeiro"],
            ("G","H"): ["Porto Alegre", "Salvador", "Rio de Janeiro", "Brasília"]
           }

assert joga_em("Croácia", "Fortaleza", grupos, estadios)
assert joga_em("Alemanha", "Porto Alegre", grupos, estadios)
assert not joga_em("Brasil", "Brasília", grupos, estadios)
