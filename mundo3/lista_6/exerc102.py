def leiaInt(txt):
    n = input(txt).strip()
    while n.isnumeric() == False:
        print(f'\033[1;31;40mERRO! Digite um número inteiro válido\033[m')
        n = input(txt).strip()
    return int(n)

n = leiaInt('Digite um numero: ')
print(f'Você acabou digitar o numero {n}')
