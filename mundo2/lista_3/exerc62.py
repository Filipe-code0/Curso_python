soma = 0
cont = -1
n = 0 

while n != 999:

    cont += 1
    soma += n
    n = int(input('digite um numero: '))

print(f'Foram digitados {cont} numeros somando para um total de: {soma} ')

