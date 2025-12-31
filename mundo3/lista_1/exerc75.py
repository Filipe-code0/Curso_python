tupla = ('Programar' , 'Amer', 'Facilitar', 'Carro', 'frgkj', 'polo', 'pulso')
vogais = ('a','e','i','o','u')

print(len(tupla))

for i in tupla:
    print(f'na palavra {i} temos ', end ='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra.lower() , ' ' ,end = '')
    print()


