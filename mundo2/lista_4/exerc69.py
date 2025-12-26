print('='*40)
print(f'{'BANCO CEV': ^40}')
print('='*40)

x = int(input('Que valor você quer sacar? R$'))

#calculo

rest = x%50

total_50 = x // 50
total_20 = (x % 50) // 20
total_10 = ((x % 50) % 20) // 10
total_1 = (((x % 50) % 20) % 10) // 1



print(f'Total de {total_50} cédulas de R$50')
print(f'Total de {total_20} cédulas de R$20')
print(f'Total de {total_10} cédulas de R$10')
print(f'Total de {total_1} cédulas de R$1')

print('='*40)
print('Volte sempre ao BANCO CEV! tenha um bom dia!')
