# coding: utf-8
# 
# Decifra segredo

def decifra(chave, mensagem):
	palavra = ""
	for letra in mensagem:
		palavra += chave[letra]
	return palavra

chave1={'@':'V','a':'v','n':'o','l':'i','#':' ','4':'a','+':'u'}
assert decifra( chave1, '+a4') == 'uva'
assert decifra( chave1, '@nan#al+#4#+a4') == 'Vovo viu a uva'

# Decifre estas frases...
chave2 = {'a': 'l', '@': 'a', '#': ' ', 'b': 'o', '+': 'd', 'm': 'u', 'c': 's','n': 'S', 

'1': 't', '9': 'e', '3': 'm', 'r': 'f', '4': 'r', 'w': '!','v': 'v', 'y': 'c','x': 'p', 


'[': 'g', 'z': 'n', ']': 'i', 'k': ',' ,'7':'P', '5':'b'}


decifra(chave2,'n9#vby9#ybzc9[m]m#a94#9c1@#39zc@[93k#@[4@+9y@#@#m3#x4br9ccb4w')
decifra(chave2,'7@4@59zck#x4br9ccb49cw')
	
