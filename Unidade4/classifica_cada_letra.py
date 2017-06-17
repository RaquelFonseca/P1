# coding: utf-8
# classifica_cada_letra
# raquel ambrozio

palavra = raw_input()

for i in palavra:
        if i in "AEIOUaeiou":
                print "sim"
        elif i in "0123456789":
                print "<%s> nao" % i
        else:
                print "nao"
        
