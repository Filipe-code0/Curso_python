total_compra = prod_caro = flag = 0

print('-'*40)
print(f'{'ATACADÃO BARATÃO': ^40}')
print('-'*40)

while True:

    produto = str(input('Produto: ')).strip().capitalize()

    preco = float(input('Preço: R$'))

    total_compra += preco

    if flag == 0:
        prod_barato = produto
        preco_barato = preco
        flag =1

    elif preco < preco_barato:
        prod_barato = produto
        preco_barato = preco
        

    if preco > 1000.00:
        prod_caro += 1

    while True:
        laco = str(input('Quer continuar? [S/N] ')).strip().upper()
        if laco == 'S' or laco == 'N':
            break

    if laco == 'N':
        break

print(f'{' FIM DO PROGRAMA ':=^40}')

print(f'Total da compra: {total_compra:.2f}')
print(f'Temos {prod_caro} produtos custando mais de R$1000.00')
print(f'O produto masi barato foi a {prod_barato} custando {preco_barato:.2f}')
