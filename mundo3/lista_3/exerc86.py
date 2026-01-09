from random import randint
from time import sleep
num = []
palpite = []
print('-' * 40)
print(f'{'JOGA NA MEGA SENA':^40}')
print('-' * 40)
n = int(input('Quantos jogos que palpitar? '))
print('-=' * 5,f'sorteando {n} jogos','-=' * 5)
for i in range(0,n):
    for j in range(0,6):
        m = randint(1,60)
        while m in num:
            m = randint(1,60)
        num.append(m)
    palpite.append(num[:])
    num.clear()
    sleep(0.5)
    print(f'jogo {i+1}: {palpite[i]}')

print(f'{'BOA SORTE':-^40}')
