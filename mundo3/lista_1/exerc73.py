w = int(input('Digite um numero: '))
x = int(input('Digite outro numero: '))
y = int(input('Digite mais um numero: '))
z = int(input('Digite o ultimo numero: '))

tupla = (w,x,y,z)

print(f'Voce digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')

cont = 0

if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print('Os valores pares são: ' , end = '')

for i in range(0, len(tupla)):

    if tupla[i] % 2 == 0:
        print(f'{tupla[i]} ' , end = '')

print()
