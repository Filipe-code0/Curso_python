x = float(input('lado: '))
y = float(input('lado: '))
z = float(input('lado: '))

if (x <= y+z and  y <= x+z and z <= y+x):
    print('E possivel formar um triangulo')

else:
    print('nao e possivel formar um triangulo')
