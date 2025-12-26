soma = 0
cont = 0
n = 0
flag = 0
flag2 = 0
maior = 0
menor = 0

while flag != 2:

    n = int(input('digite um numero: '))
    soma += n
    cont += 1
    
    if flag2 == 0:
        menor = n
        maior = n
        flag2 = 1

    if n > maior:
        maior = n

    if n < menor:
        menor = n

    flag = int(input('Voce quer continuar?\n1.sim\n2.nao\nresposta: '))

media = soma/cont

print(f'Media dos valores: {media:.2f}\nMenor: {menor}\nMaior:{maior} ')

