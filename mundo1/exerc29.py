distancia = float(input('Qual é a distancia da viagem: '))

if distancia <= 200.0:
    print(f'a passagem custara: {distancia*0.50:.2f}')

else:
    print(f'a passagem custara: {distancia*0.45:.2f}')
