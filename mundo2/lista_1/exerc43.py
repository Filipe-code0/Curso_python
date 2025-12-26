from random import randint

print('-'*30)
print('PEDRA, PAPEl e TESOURA')
print('1. pedra')
print('2. papel')
print('3. tesoura')

jogador = int(input('escolha o numero da opcao de ataque: '))
maquina = randint(1,3)

print()

if maquina == 1 and jogador == 3 or maquina == 2 and jogador == 1 or maquina == 3 and jogador == 2:
    print('Maquina venceu {^<>^}')

elif maquina == 3  and jogador == 1 or maquina == 1 and jogador == 2 or maquina == 2 and jogador == 3:
    print('Voce venceu !!!')

else:
    print('Empate...')

print()

print(f'maquina {maquina}, jogador {jogador}')
print('Its over BABY')
print('-'*30)

