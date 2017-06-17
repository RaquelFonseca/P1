# coding: utf-8

# Soma matrizes esparsas

def soma_matrizes_esparsas(M1, M2):
	soma = {}
	soma[str(M1[2].keys())] = M1[2].values()
	soma[str(M2[2].keys())] = M2[2].values()
	print soma
	return M1[0], M1[1], soma


M1 = (120, 200, {(115, 64): -5})
M2 = (120, 200, {(20, 55): 5})

SOMA1 = soma_matrizes_esparsas(M1, M2)
"""print SOMA1
assert SOMA1 == (120, 200, {(116, 64): -5, (20, 55): 5})

M3 = (120, 200, {(115, 64): 5})
SOMA2 = soma_matrizes_esparsas(SOMA1, M3)
assert SOMA1 == M2"""

