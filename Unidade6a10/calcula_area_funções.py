# coding: utf-8
# 
# CALCULA AREAS COM FUNÇÕES

def areaQuadrado(lado):
	area = float(lado) ** 2
	return "A área do quadrado é %.2f" % area
	
def areaTriangulo(lado1, lado2):
	area = float(figura[1]) * float(figura[2])
	return "A área do triangulo é %.2f" % area

def areaCirculo(raio):
	area = (float(figura[1]) ** 2) * math.pi 
	return "A área do círculo é %.2f" % area
	
import math

while True:
	figura = raw_input().split()
	if figura[0] == "fim":
		break
	elif figura[0] == "Q":
		print areaQuadrado(figura[1])
	elif figura[0] == "T":
		print areaTriangulo(figura[1], figura[2])
	elif figura[0] == "C":
		print areaCirculo(figura[1])

