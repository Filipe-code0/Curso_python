salario = float(input('Seu Salario: '))

if salario >1250.00:
    print(f'10% de aumento de do salario qeuivalente a {salario:.2f} + {salario*0.10:.2f} = {salario + salario*0.10:.2f}')
    
else:
    print(f'15% de aumento de do salario qeuivalente a {salario:.2f} + {salario*0.15:.2f} = {salario + salario*0.15:.2f}')
