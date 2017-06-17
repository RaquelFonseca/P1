# coding: utf-8
# fornecimento de energia
# raquel ambrozio

quantidade = int(raw_input())

r = 0.7
e = 0.5
c = 0.3

t_consumo_r = 0
t_consumo_e = 0
t_consumo_c = 0

contador_r = 0
contador_e = 0
contador_c = 0

lista_consumidor = []
lista_kwh = []
lista_tipo = []

for i in range(quantidade):
       consumidor = raw_input()
       lista_consumidor.append(consumidor)
       kwh = float(raw_input())
       lista_kwh.append(kwh)
       tipo_consumidor = raw_input()
       lista_tipo.append(tipo_consumidor)

for i in range(len(lista_tipo)):
       if lista_tipo[i] == "R":
              t_consumo_r += lista_kwh[i]
              contador_r += 1
       elif lista_tipo[i] == "E":
              t_consumo_e += lista_kwh[i]
              contador_e += 1
       else:
              t_consumo_c += lista_kwh[i]
              contador_c += 1
              

print "Total do consumo (Consumidor Regular) : %.2f kwh" % t_consumo_r
print "Total do consumo (Consumidor Especial) : %.2f kwh" % t_consumo_e
print "Total do consumo (Consumidor Carente) : %.2f kwh" % t_consumo_c

print "-" * 3

m_consumo_r = t_consumo_r / contador_r
m_consumo_e = t_consumo_e / contador_e
m_consumo_c = t_consumo_c / contador_c

print "Media de consumo (Consumo Regular): %.2f kwh" % m_consumo_r
print "Media de consumo (Consumo Especial): %.2f kwh" % m_consumo_e
print "Media de consumo (Consumo Carente) : %.2f kwh" % m_consumo_c

print "-" * 3


soma_total = 0

for valor in lista_kwh:
       soma_total += valor

m_geral_consumo = soma_total / len(lista_kwh)

print "Media geral de consumo: %.2f kwh" % (m_geral_consumo)

print "-" * 3

print "Consumidores acima da media geral:"

for i in range(len(lista_kwh)):
       if lista_kwh[i] > m_geral_consumo:
              if lista_tipo[i] == "R":
                     preco = lista_kwh[i] * r
              elif lista_tipo[i] == "E":
                     preco = lista_kwh[i] * e
              else:
                     preco = lista_kwh[i] * c
              print "(%s) %s R$ %.2f" % (lista_tipo[i], lista_consumidor[i], preco)

print "-" * 3
       
       
