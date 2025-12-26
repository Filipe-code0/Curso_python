x = float(input('Peso da pessoa: '))

maior = x
menor = x

for i in range(0,4):
    x = float(input('Peso da pessoa: '))

    if x > maior:
        maior = x

    if x < menor:
        menor = x

print(f'O maior peso foi: {maior:.2f}Kg, o menor peso foi: {menor:.2f}Kg')
