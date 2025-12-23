i = 0

while i!=1:
    print('Qual e o seu sexo? ')
    n = str(input('Digite M para masculino e F para feminino:  ')).upper()
    
    if n == 'M' or n == 'F':
        i = 1
    
    else:
        print('Erro: tente novamente\n')

print('Operacao bem sucedida!')
