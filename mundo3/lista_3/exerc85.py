linha = []
coluna = []
pares = 0
ter = 0
seg = []
for i in range(0,3):
    for j in range(0,3):
        n = int(input(f'Digite um valor para [{i},{j}]: '))
        if n%2 == 0:
            pares += n
        if i == 2:
            ter += n
        if i == 1:
            seg.append(n)
        coluna.append(n)
        linha.append(coluna[:])
        coluna.clear()
print('Matrix:')
for i in range(0,9):
    print(f'{linha[i]}', end ='')
    if i == 2 or i == 5 or i == 8:
        print()

maior = max(seg)

print(f'Soma pares: {pares}')
print(f'Soma ter. linha: {ter}')
print(f'Maior seg. linha: {maior}')
