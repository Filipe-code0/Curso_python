print('-' * 50)
n = int(input('Escreva um numero inteiro para gerar o fatorial: '))
i = 1
r = 1

print(f'{n}! = ', end = '')
while i!=n+1:
    r *= i
    i += 1
    print(f'{i-1}', end = '')
    if i != n+1:
        print(' * ', end = '')
    else:
        print(' = ', end = '')

print(f'{r}')
print('-' * 50)

