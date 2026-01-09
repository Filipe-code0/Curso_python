dicio = {}
dicio['Nome'] = input('Nome: ')
dicio['Media'] = float(input('Media: '))
if dicio['Media'] > 7.0:
    dicio['Situacao'] = 'Aprovado'
elif dicio['Media'] > 5.0:
    dicio['Situacao'] = 'Recuperacao'
else:
    dicio['Situacao'] = 'Reprovado'
for i,j in dicio.items():
    print(f'{i} é igual {j}')
print()
