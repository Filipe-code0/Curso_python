lista = []
while True:
    num = int(input('Digite um numero: '))
    lista.append(num)
    opcao = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
lista.sort(reverse=True)
print(f'Voce digitou {len(lista)} elementos.')
print(f'OS valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
