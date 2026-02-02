from time import sleep
from lib import flio as fl
def linha(qtd=10):
    print('-'*qtd)

def cabecalho(txt):
    linha(40)
    print(f'\033[32m{txt.center(40)}\033[m')
    linha(40)

def menu(file):
    while True:
        cabecalho('Menu Principal')
        print('\033[36mEscolha uma opcao\033[m')
        print('\033[34m1. Lista de pessoas\033[m')
        print('\033[34m2. Inserir a lista\033[m')
        print('\033[34m3. Sair\033[m')
        sleep(0.5)
        op = int(input('\033[33mOpcao: \033[m'))
        sleep(1)
        linha(40)
        if op == 1:
            fl.printfl(file)
            sleep(0.3)
        elif op == 2:
            nome = str(input('Nome da pessoa: ')).strip()
            while True:
                try:
                    idade = int(input('Idade da pessoa: '))
                    sleep(0.3)
                except:
                    print('\033[31mERRO! Responda com um numero inteiro valido\033[m')
                else:
                    fl.appendfl(file, nome, idade, 'anos')
                    print('Operacao feita com sucesso')
                    break
        elif op == 3:
            print('Saindo do Programa')
            sleep(0.5)
            linha(40)
            break
        else:
            print('Opcao invalida.')
