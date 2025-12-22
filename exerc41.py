peso = float(input('seu peso: '))
altura = float(input('sua altura: '))

IMC = peso / (altura*altura)

if 18.5 > IMC:
    print(f'seu IMC de {IMC:.1f} indica que voce esta abaixo do peso')

elif IMC >= 18.5 and IMC < 25.0:
    print(f'seu IMC de {IMC:.1f} indica que voce esta no peso ideal')

elif IMC >= 25.0 and IMC < 30.0:
    print(f'seu IMC de {IMC:.1f} indica que voce esta com sobrepeso')

elif IMC >= 30.0 and IMC < 40.0:
    print(f'seu IMC de {IMC:.1f} indica que voce esta com Obesidade')
   
elif IMC >= 40.0:
    print(f'seu IMC de {IMC:.1f} indica que voce esta com obesidade morbida')


