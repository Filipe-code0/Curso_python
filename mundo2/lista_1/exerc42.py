valor = float(input('Valor da compra: '))

print('-' * 30)
print('Escolha a forma de pagamento')
print('1. A vista no dinheiro (10% de desconto)')
print('2. A vista no cartao (5% de desconto)')
print('3. Ate 2x no cartao')
print('4. 3 vezes ou mais no cartao')

opcao = int(input('Escolha a opcao de pagamento: '))

if opcao == 1:
            print(f'O pagamento ficara em {valor - (valor*0.10):.2f} no total')
elif opcao == 2:
            print(f'O pagamento ficara em {valor - (valor*0.05):.2f} no total')
elif opcao == 3:
            print(f'O pagamento ficara em {valor:.2f} no total')
elif opcao == 4:
            print(f'O pagamento ficara em {valor + (valor*0.20):.2f} no total')
else:
    print('Opcao Invalida')

print('-' * 30)

