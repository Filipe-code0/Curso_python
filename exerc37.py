from datetime import date

ano = int(input('Ano de nascimento: '))

data = date.today()
ano_atual = data.year

if ano_atual - ano == 18:
    print('Alistece as forcas armadas, esse e seu ano de alistamento')

elif ano_atual - ano > 18:
    print(f'Seu ano de alistamento ja passou do prazo em {(ano_atual - ano) - 18} ano(s)')

else:
    print(f'Seu ano de alistamento ainda ocorera em {abs((ano_atual - ano) - 18)} ano(s) ')
