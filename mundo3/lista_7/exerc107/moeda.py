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
