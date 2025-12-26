n = int(input('Numero a ser analisado: '))
flag = 0

for i in range(1,n+1):
    if n%i == 0:
        print(f'\033[31m{i}\033[m', end = ' ')
        if i != 1 and i != n or n ==1:
            flag = 1

    else:
        print(f'\033[34m{i}\033[m', end = ' ')

print()

if flag == 0:
    print('O numero é primo')

elif flag == 1:
    print('O numero não é primo')

