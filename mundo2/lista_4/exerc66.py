from random import randint

cont = 1

while True:

    print('-' * 40)

    print('ESCOLHA ENTRE PAR OU IMPAR')

    opcao = 0

    while opcao != 1 and opcao != 2:
        opcao  = int(input('2 para par e 1 para impar:  '))

    computador = randint(0,5)
    jogador = int(input('Digite um numero inteiro:  '))

    print(f'jogador escolheu {jogador} e computador escolheu {computador}')

    cond = jogador + computador


    if cond % 2 == 0 :
        print('Soma: PAR')
        
        if opcao == 1:
            print(f'JOGADOR PERDEU, no {cont} jogo')
            break

        else:
            print(f'JOGADOR GANHOU, pela {cont}º vez')

    else:
        print('Soma: IMPAR')
        if opcao == 2:
            print(f'JOGADOR PERDEU, no {cont} jogo')
            break
        
        else:
            print(f'JOGADOR GANHOU, pela {cont}º vez')

    cont +=1

print('O JOGO ACABOU') 
print('-' * 40)
