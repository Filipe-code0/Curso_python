lista = []
while True:
    num = int(input('Digite um numero: '))
    lista.append(num)
    opcao = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
pares = []
impares = []
for i in range(0,len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])

    elif lista[i] % 2 == 1:
        impares.append(lista[i])

print(f'A lista completa eh {lista}')
print(f'A lista de pares eh {pares}')
print(f'A lista de impares eh {impares}')
