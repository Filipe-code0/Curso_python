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
print(f'cont: {cont}, total: {tot_idade}, mulheres: {mulheres}, media: {media}')
for i in grupo:
    if i['idade'] > media:
        print(i)
