from random import randint

print('*' * 40)
print('Tente advinhar um numero de 0 a 10:')

cont = 0
jogador = -1
computador = -2

while jogador != computador:
    computador = randint(0,10)
    jogador = int(input('chute:'))

    print(f'maquina: {computador}, voce: {jogador}')

    if jogador == computador:
        cont += 1
        print(f'Voce ganhou em {cont} jogadas!')

    else:
        cont += 1
        print('Voce errou!')
        print('*' * 40)

