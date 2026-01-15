def fatorial(num, show=False):
    """
        -> Calcula o fatorial de um numero
        :param num: O numero a ser calculado
        :param show: (Opcional), mostrar ou não a conta
        :return: o valor fatorial do numero
    """
    i = 0
    atual = 1
    while i < num:
        i += 1
        atual *= i
        if show:
            print(f'{i} ', end ='')
            if i != num:
                print(f'x ', end ='')
            else:
                print(f'= ', end ='')
    return atual

print('-' * 30)
print(fatorial(5,True))
print()
