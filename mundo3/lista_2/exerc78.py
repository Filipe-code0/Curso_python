lista = []
for i in range(0,5):
    x = int(input('Digite um valor: '))
    pos = j = 0
    if i == 0:
        lista.insert(i,x)
    else:
        while j < i:
            if x >= lista[j]:        
                pos += 1
            j += 1
        lista.insert(pos,x)
    if pos == i:
        print(f'Adicionado no final da lista')
    else:
        print(f'Adicionado na posicao {pos} da lista')
print('-='*40)
print(f'Os valores digitados em ordem foram {lista}')
