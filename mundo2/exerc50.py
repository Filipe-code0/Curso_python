n = int(input('Numero a ser analisado: '))

v = 0

for i in range(2,n):
    if n%i == 0 and n != i:
        v = 1

if v == 0:
    print('o numero é primo')

else:
    print('o numero não é primo')
