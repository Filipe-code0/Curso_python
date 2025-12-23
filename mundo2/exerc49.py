x = int(input('Primeiro termo da PA:'))
r = int(input('Razao da PA:'))

print(f'Termo[1]: {x}')

for i in range(1,10):
    x = x+r
    print(f'Termo[{i+1}]: {x}')

print()
