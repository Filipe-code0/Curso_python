from random import randint
from time import sleep
def sorteia(vet):
    print(f'Sorteando os numeros da lista: ', end = '')
    for i in range(0,5):
        numeros.append(randint(0,10))
        print(f'{numeros[i]} ', end= '', flush=True)
        sleep(0.4)
    print()
def somaPar(vet, pares):
    for i in vet:
        if i%2 == 0:
            pares += i
    sleep(1)
    print(f'A soma de todos os pares eh: {pares}')
    return pares
numeros = []
pares = 0
sorteia(numeros)
pares = somaPar(numeros, pares)
