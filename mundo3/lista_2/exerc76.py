lista = []
pos_max = []
pos_min = []
for i in range(0,5):
    lista.append(int(input(f'Digite um valor para a posicao {i}: ')))
    if i == 0:
        minimo = maximo = lista[0]
    elif lista[i] > maximo:
        maximo = lista[i]
    elif lista[i] < minimo:
        minimo = lista[i]
print(f'O maior valor foi {maximo} nas posicoes ', end ='')
for c, v in enumerate(lista):
    if v == maximo:
        print(f'{c}...',end = '')
print()
print(f'O menor valor foi {minimo} nas posicoes ', end ='')
for d, m in enumerate(lista):
    if m == minimo:
        print(f'{d}...',end = '')
print()

