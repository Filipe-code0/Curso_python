grupo = []
pessoa = {}
mulheres = []
tot_idade = cont = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).strip().upper()[0]
        if pessoa['sexo'] in 'FM':
            break
    pessoa['idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())
    tot_idade += pessoa['idade']
    cont += 1
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    op = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
media = tot_idade/cont
print(f'A) Ao todo temos {cont} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f}')
print(f'C) As mulheres cadastradas foram ',end='')
for i in mulheres:
    print(f'{i} ',end='')
print()
print(f'D) Lista das pessoas que estão acima de média:')
for i in grupo:
    if i['idade'] >= media:
        for k,v in i.items():
            print(f'    {k} = {v}; ', end = '')
        print()
print('<< ENCERRADO >>')
