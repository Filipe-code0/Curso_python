# Analisador Completo

# Variaveis
flag = 0
homem_velho = ''
maior_idade = 0
menor_idade = 0
soma = 0

# loop de perguntas:

for i in range(0,4):

    x = str(input('Nome: ')) 
    y = int(input('Idade: '))
    z = str(input('Sexo: ')).strip().upper()

# Tratamento de 1 caso:

    if flag == 0:
        if z == 'MASCULINO':
            homem_velho = x
            maior_idade = y
            
        flag = 1

# Comparacoes:

    if z == 'MASCULINO' and y > maior_idade:
        homem_velho = x
        maior_idade = y

    if z == 'FEMININO' and y < 20:
        menor_idade += 1

    soma += y

media = soma/4

print(f'Media de idade do grupo: {media:.2f}')
print(f'Homem mais velho: {homem_velho} com {maior_idade}')
print(f'Mulheres com menos de 20 anos: {menor_idade}')
