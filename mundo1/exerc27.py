velocidade = float(input('Velocidade do carro: '))

if velocidade > 80.0:
    print(f'Voce foi multado no valor de {(velocidade - 80)*7:.2f}')

else:
    print('Prossiga normalmente')

