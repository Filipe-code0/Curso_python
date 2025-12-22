from math import radians, cos, sin, tan

x = float(input('Valor valor do angulo: '))

seno = sin(radians(x))
coseno = cos(radians(x))
tangente = tan(radians(x))

print(f'valor de seno: {seno:.2f}, coseno: {coseno:.2f}, tangente:{tangente:.2f}')

