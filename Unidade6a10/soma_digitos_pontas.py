# coding: utf-8
# soma digitos pontas
# raquel ambrozio


def spm(numero):
    primeiros = int(numero[:2])
    ultimos = int(numero[3:])
    meio = int(numero[2])
    resultado = "%04d" % ((primeiros + ultimos) * meio)
    print  resultado
    
    
spm(numero = raw_input())
    

    
    

