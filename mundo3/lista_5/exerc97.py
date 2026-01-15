def linha():
    print('-=' * 25)

def maior(*vet):
    tam = len(vet)
    linha()
    print('Analisando os valores passados...')
    for i in vet:
        print(f'{i} ', end='')
    if len(vet) != 0:
        maior = max(vet)
    else:
        maior = 'Não existe'
    print(f'Foram informados {tam} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    
maior(6,19)
maior(26,19,3,12)
maior(62,19,14)
maior(6)
maior()
print()
