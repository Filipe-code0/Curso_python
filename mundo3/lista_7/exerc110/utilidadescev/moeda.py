def metade(preco=0, formato=True, moeda = 'R$'):
    preco = preco*0.50
    if formato == True:
        preco = f_moeda(preco, moeda)
    return preco

def dobro(preco=0, formato=True, moeda = 'R$'):
    preco = preco*2
    if formato == True:
        preco = f_moeda(preco, moeda)
    return preco

def aumentar(preco=0, taxa=0, formato=True, moeda = 'R$'):
    preco = preco + (preco*(taxa/100))
    if formato == True:
        preco = f_moeda(preco, moeda)
    return preco

def diminuir(preco=0, taxa=0, formato=True, moeda = 'R$'):
    preco = preco - (preco*(taxa/100))
    if formato == True:
        preco = f_moeda(preco, moeda)
    return preco

def f_moeda(preco=0, moeda='R$'):
    preco = f'{moeda}{preco:.2f}'.replace('.',',')
    return preco

def resumo(preco=0, aumento=0, reducao=0):
    print('-'*40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-'*40)
    print(f'Preco analisado:            {f_moeda(preco):<20}')
    print(f'Dobro do preco:             {dobro(preco):<20}')
    print(f'Matade do preco:            {metade(preco):<20}')
    print(f'80% de aumento:             {aumentar(preco, 80):<20}')
    print(f'35% de reducao:             {diminuir(preco, 35):<20}')
