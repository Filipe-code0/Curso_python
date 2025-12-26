from math import hypot

a = float(input('Cateto oposto: '))
b = float(input('Cateto adjancente: '))

print(f'\nO cateto oposto: {a:.2f}\nO cateto adjacente: {b:.2f}\nA hipotenusa: {hypot(a,b):.2f}')
