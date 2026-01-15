from time import sleep
def linha():
    print('-=' * 15)

def contador(ini, fim, passo):
    print(f'Contagem de {ini} até {fim} de {abs(passo)} em {abs(passo)}')
    if ini < fim:
        fim = fim + 1
    else:
        fim = fim - 1
        passo = (passo * -1)
    for i in range(ini,fim,passo):
        print(f'{i} ', end='', flush = True)
        sleep(0.5)
    print('FIM!')

linha()
contador(1,10,1)
linha()
contador(10,0,2)
linha()
print('Agora é a sau vez de personalisar a contagem!')
inicio = int(input('Inicio: '))
final = int(input('Fim: '))
passos = int(input('Passo: '))
linha()
contador(inicio, final, passos)
