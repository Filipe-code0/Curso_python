x = float(input('lado: '))
y = float(input('lado: '))
z = float(input('lado: '))

if (x <= y+z and  y <= x+z and z <= y+x):

    if x == y and x == z:
        print('E possivel formar um triangulo equilatero')

    elif x == y or x == z or z == y:
        print('E possivel formar um triangulo isosceles')

    else:
        print('E possivel formar um triangulo escaleno')

else:
    print('nao e possivel formar um triangulo')
