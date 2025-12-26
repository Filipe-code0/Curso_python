pessoa_18 = homem = mulher_20 = 0

while True:

    print('-'*40)
    print(f'{'CADASTRE UMA PESSOA': ^40}')
    print('-'*40)

    while True:
        idade = int(input('Idade: '))
        if idade < 150 and idade > -1:
            break

    while True:
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
        if sexo == 'M' or sexo == 'F':
            break

    if idade > 18:
        pessoa_18 += 1

    if sexo == 'M':
        homem += 1

    if sexo == 'F' and idade < 20:
        mulher_20 += 1

    print('-'*40)

    while True:
        laco = str(input('Quer continuar? [S/N] ')).strip().upper()
        if laco == 'S' or laco == 'N':
            break

    if laco == 'N':
        break

print(f'{' FIM DO PROGRAMA ':=^40}')

print(f'Total de pessoas com mais de 18 anos: {pessoa_18}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher_20} mulher(s) com menos de 20 anos')
