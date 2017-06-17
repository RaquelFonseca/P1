# coding: utf-8
# espaço em disco
# Raquel Ambrozio

login = raw_input()
espaco = int(raw_input())
login2 = raw_input()
espaco2 = int(raw_input())
login3 = raw_input()
espaco3 = int(raw_input())
espaco = espaco / 1024.00 **2
espaco2 = espaco2 / 1024.00 ** 2
espaco3 = espaco3 / 1024.00 ** 2
espacot = espaco + espaco2 + espaco3
espacom = (espaco + espaco2 + espaco3) / 3.0

print '''SPLab - Espaço utilizado pelos usuários
---------------------------------------------------
Nr., Usuário, Espaço utilizado

1, %s, %.2f MB
2, %s, %.2f MB
3, %s, %.2f MB

Espaço total ocupado: %.2f MB
espaço médio ocupado: %.2f MB''' % (login, espaco, login2, espaco2, login3, espaco3, espacot, espacom)
