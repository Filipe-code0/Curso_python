while True:

    print('-'*50)
    num = int(input('Digite um numero para gerar sua tabuada: '))

    if num < 0:
        break
    
    for i in range(1,11):
        print(f'{num} * {i:2} = {num*i}')


print('-'*50)
print('PROGRAMA ENCERRADO')
