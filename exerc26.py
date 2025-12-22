from random import randint

x = int(input('Advinhe o numero: '))

y = randint(0,5)

print(f'a maquina escolheu {y} e voce escolheu {x}')

if x==y:
    print(f'Voce ganhou da maquina!!')

else:
    print('Voce perdeu :(')

