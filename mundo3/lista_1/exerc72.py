from random import randint

a = randint(0,10)
b = randint(0,10)
c = randint(0,10)
d = randint(0,10)
e = randint(0,10)

tupla = (a,b,c,d,e)

print(f'Os valores sorteados foram: {tupla[0]} {tupla[1]} {tupla[2]} {tupla[3]} {tupla[4]}')
print(f'O maior valor sorteado foi: {max(tupla)}')
print(f'O menor valor sorteado foi: {min(tupla)}')

