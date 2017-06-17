# coding: utf-8
# eh palindromo
# raquel ambrozio

string = raw_input()
assert len(string) >= 1
string2 = string[::-1]

for i in range(len(string)):
  if string[i] == string2[i]:
    palindromo = True
  else:
    palindromo = False
if palindromo:    
  print "%s eh palindromo" % string
else:
  print "%s nao palindromo" % string
