Z = 1

while Z != 5:

    print('-' * 53)
    print('-' * 20, 'CALCULADORA', '-' * 20, '\n')

    X = float(input('Insira o 1º numero: '))
    Y = float(input('Insira o 2º numero: '))

    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NUMEROS')
    print('[5] SAIR DO PROGRAMA')

    Z = int(input('Insira a opção: '))

    if Z==1:
        print(f'RESULTADO: {X} + {Y} = {X+Y}')
        print()

    elif Z==2:
        print(f'RESULTADO: {X} * {Y} = {X+Y}')
        print()

    elif Z==3:

        if X > Y:
            print(f'RESULTADO: {X} > {Y}')

        elif Y > X:
            print(f'RESULTADO: {Y} > {X}')

        else:
            print(f'RESULTADO: {Y} = {X}')

        print()

    elif Z==4:
        print('REINICIANDO')
        print()
    elif Z==5:
        print('DESLIGANDO')
        print()
    else:
        print('OPCAO NAO EXISTE')
        print()
        
