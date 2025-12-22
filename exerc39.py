from datetime import date

competidor = int(input('Ano de nascimento do competidor: '))

data = date.today()
ano = data.year
categoria = ano - competidor

if categoria <= 9:
    print('Categoria: Mirim')

if categoria > 9 and categoria <= 14:
    print('categoria: Infantil')

if categoria > 14 and categoria <=19:
    print('categoria: Junior')

if categoria == 20:
    print('categoria: Senior')

if categoria > 20:
    print('categoria: Master')

