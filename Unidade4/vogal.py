palavra = (raw_input())
string = ""


for i in range(len(palavra)):
    if palavra[i] in "AaEeIiOoUu":
        string += palavra[i]
    else:
        string += "-"

print string[0]
