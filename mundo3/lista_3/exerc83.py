num = [[], []]
for i in range(0,7):
    n = int(input('Digite um numero: '))
    if n%2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
num[1].sort()
print('-=' * 40)
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores Impares digitados foram: {num[1]}')
