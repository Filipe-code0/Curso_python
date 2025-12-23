val_casa = float(input('Qual e o valor da casa? '))
salario = float(input('Quanto voce ganha de salario? '))
qtd_ano = float(input('Em quantos anos voce ira pagar? '))

mensalidade = val_casa / (qtd_ano * 12)

if mensalidade > (salario*0.30):
    print('Emprestimo negado')
else:
    print(f'Emprestimo aceito, mensalidade: {mensalidade:.2f}')

