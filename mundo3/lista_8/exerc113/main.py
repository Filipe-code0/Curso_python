def f_linha(Ap=0, num=30):
    if Ap == 0:
        print(f'{"-":>10}', end='')
        print('-'*30)
    if Ap == 1:
        print('-'*50)

from time import sleep
import flio_basics as fl
while True:
    sleep(1)
    f_linha()
    print(f'{"|":>10}{"MENU PRINCIPAL":^31} |')
    f_linha()
    f_linha(1)
    print('1- Vizualizar tabela')
    print('2- Cadastrar pessoa')
    print('3- Sair do sistema')
    f_linha(1)
    res = int(input('RESPOSTA: '))
    f_linha(1)
    sleep(1)
    if res == 1:
        print()
        fl.printfl('nome.txt')
        f_linha(1)
    elif res == 2:
        nome = str(input('Nome: ')).strip()
        idade = int(input('Idade: '))
        fl.appendfl('nome.txt',nome,idade)
        f_linha(1)
    elif res == 3:
        print('VOLTE SEMPRE')
        f_linha(1)
        break
    sleep(1)
