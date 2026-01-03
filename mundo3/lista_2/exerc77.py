lista = []

while True:
    x = int(input('Digite um valor: '))
    
    if x in lista:
        print('Valor Duplicado! não vou adicionar...')

    else:
        print('Valor digitado com sucesso...')
        lista.append(x)

    saida = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
    if saida == 'N':
        break

print('-=' * 40)

print(f'Voce digitou os valores {sorted(lista)}')

