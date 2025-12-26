ano = int(input('Ano: '))

if ano%400 == 0:
    print('ano bisexto')

elif ano%2==0 and ano%100 != 0:
    print('ano bisexto')

else:
    print('ano normal')

