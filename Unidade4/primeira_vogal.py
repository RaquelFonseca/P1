# coding: utf-8
# primeira_vogal
# raquel ambrozio

palavra = raw_input()


for vogal in range(len(palavra)):
         if palavra[vogal] in "AEIOUaeiou":
                 print palavra[vogal]
                 break
else:
        print "-"
