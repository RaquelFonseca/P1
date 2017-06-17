# coding: utf-8

# Unidade de medida

SI = {"km": 1000, "hm": 100, "dam": 10, "m": 1,
		"dm": 0.1, "cm": 0.01, "mm": 0.001}
		
while True:
	entrada = raw_input().split()
	conversao = 0.0
	valor1 = int(entrada[0])
	valor2 = int(entrada[2])
	if valor1 == 0 and valor2 == 0:
		break
	for medida in SI.keys():
		if medida == entrada[1]:
			conversao += valor1 * SI[medida]
		if medida == entrada[3]:
			conversao += valor2 * SI[medida]
	print "%.2f m" % conversao
