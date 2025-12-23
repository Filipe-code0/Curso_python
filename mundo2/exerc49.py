x = int(input('Primeiro termo da PA:'))
r = int(input('Razao da PA:'))

for i in range(0,10):
    x = x+r
    print(f'Termo[{i+1}]: {x}')

print()
