x = int(input('Primeiro termo da PA:'))
r = int(input('Razao da PA:'))

print(f'Termo[1]: {x}')

i = 1

while i < 10:
    x = x+r
    print(f'Termo[{i+1}]: {x}')
    i += 1

print()
