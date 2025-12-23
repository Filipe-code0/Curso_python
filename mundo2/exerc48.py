s = 0

for i in range(0,6):
    c = int(input('Insira um numero: '))
    if c%2 == 0:
        s += c

print(f'Resultado da soma dos pares: {s}')
