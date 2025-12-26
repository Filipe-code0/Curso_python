num = int(input('Digite um numero para a sequencia fibonacci: '))

i = 0
res = 0
ant = 0
atu = 0

while i < num:

    if i == 0 or i == 1:
        res = 1
        ant = 1
        atu = 1
    
    else:
        res = ant + atu
        ant = atu
        atu = res
    i += 1

    print(f' {res} ', end = '')

    if i != num:
        print('->', end = '')
print()
