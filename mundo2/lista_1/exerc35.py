num = int(input('escreva o numero: '))

print('escolha uma opcao\n1. para binario\n2. para octal\n3. para hexadecimal')

opcao = int(input('opcao: '))

if opcao == 1:
    print(f'numero: {bin(num)}')

elif opcao == 2:
    print(f'numero: {oct(num)}')

else:
    print(f'numero: {hex(num)}')

print('-' * 12)
