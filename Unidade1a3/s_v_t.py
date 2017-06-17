# coding: utf-8
# s = s0 + v * t
# Raquel Ambrozio
s0 = float(raw_input("posição inicial (m)? "))
v = float(raw_input("velocidade (m/s)? "))
t = float(raw_input("tempo (s)? " ))
s = s0 + v * t
print "posiçao inicial (m)? velocidade (m/s) tempo (s)? Posição final do móvel"
print "S(%.1f) = %.1f m" % (t, s)
