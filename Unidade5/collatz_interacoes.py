n = int(raw_input())
contador = 0
while True:
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1
    contador += 1
    if n == 1:
        break

print contador
