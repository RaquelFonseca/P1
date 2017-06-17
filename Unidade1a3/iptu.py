# coding: utf-8
# IPTU
# Raquel Ambrozio

area = float(raw_input("Área construída? "))
aliquota = float(raw_input("Alíquota? "))
iptu = area * aliquota + 35
desconto25 = iptu - (iptu*0.75)
desconto75 = iptu - desconto25
desconto5 = iptu - (iptu*0.95)
desconto95 = iptu - desconto5
parcela6 = desconto95 / 6
parcela10 = iptu / 10
print "IPTU: R$ %.2f" % iptu
print "Pagamento:"
print "1. Quota única. R$ %.2f" % desconto75
print "2. Em 6 parcelas. Total: R$ %.2f" % desconto95
print     "6 x %.2f" % parcela6
print "3. Em 10 parcelas. Total: R$ %.2f" % iptu
print     "10 x R$ %.2f" % parcela10


