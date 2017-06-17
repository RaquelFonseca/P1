# coding: utf-8
# unidades de temperaturas
# Raquel Ambrozio
fahrenheit = float(raw_input())
celsius = (fahrenheit - 32) * 5 / 9.0
kelvin = celsius + 273.15
print "Fahrenheit: %.3f F" % fahrenheit
print "Celsius: %.3f C" % celsius
print "Kelvin: %.3f K" % kelvin
