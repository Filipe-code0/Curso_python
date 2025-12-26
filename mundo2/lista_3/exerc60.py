flag = 1
a = 10
i = 0

while a != 0:

    if flag ==1:
        x = int(input('Primeiro termo da PA: '))
        r = int(input('Razao da PA: '))
        flag =0

    j = 0

    while j < a:
        print(f'Termo[{i+1}]: {x}')
        j += 1
        x = x+r
        i += 1

    a = int(input('Digite quantos termos a frente deseja ver: '))

print('PROGRAMA TERMINOU')

print()
