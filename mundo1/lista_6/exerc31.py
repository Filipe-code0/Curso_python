a = float(input('Numero: '))
b = float(input('Numero: '))
c = float(input('Numero: '))

menor = a

if b < a and b < c:
    menor = b

if c < a and c < b:
    menor = c

maior = a

if b > a and b > c:
    maior = b

if c > a and c > b:
    maior = c

print(f'menor numero : {menor}')
print(f'maior numero : {maior}')
