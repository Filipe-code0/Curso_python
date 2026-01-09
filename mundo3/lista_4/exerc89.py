from random import randint
from time import sleep
from operator import itemgetter
dicio = {}
for i in range(1,5):
    num = randint(0,6)
    dicio[f'jogador{i}'] = num
ranking = {}
for v,k in dicio.items():
    sleep(0.5)
    print(f'{v} tirou {k} no dado.')
ranking = sorted(dicio.items(), key=itemgetter(1), reverse=True)
print('-=' * 40)
for i,c in enumerate(ranking):
    sleep(0.5)
    print(f'{i+1} lugar: {c[0]} com {c[1]}')
print()
