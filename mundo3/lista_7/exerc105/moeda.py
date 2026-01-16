def metade(preco):
    return preco*0.50

def dobro(preco):
    return preco*2

def aumentar(preco, taxa):
    return preco + (preco*(taxa/100))

def diminuir(preco, taxa):
    return preco - (preco*(taxa/100))

def moeda(valor):
    linha = valor[:.2f]
    return linha

