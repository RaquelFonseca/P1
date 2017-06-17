# coding: utf-8
# comeco palavra
# raquel ambrozioo

n = int(raw_input("n? "))
c = raw_input("c? ")

while n > 0:
  palavra = raw_input("palavra? ")
  n -= 1
  if palavra[0].lower() == c or palavra[0].upper() == c:
    print "%s comeca com %s" % (palavra, c)
  else:
    print "%s nao comeca com %s" % (palavra, c)

