from datetime import datetime
pessoa = {}
ano_atual = datetime.now().year
pessoa['nome'] = input('Nome: ')
ano_nasc = int(input('Ano de Nacimento:'))
pessoa['idade'] = (ano_atual - ano_nasc)
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] == 0:
    print('-=' * 20)
    print(pessoa)
    for k,v in pessoa.items():
        print(f'{k} tem o valor de {v}')
else:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = ((35 + pessoa['contratação']) - ano_nasc)
    print('-=' * 20)
    print(pessoa)
    for k,v in pessoa.items():
        print(f'{k} tem o valor de {v}')

