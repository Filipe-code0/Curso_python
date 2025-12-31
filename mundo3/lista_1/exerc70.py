numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze',
           'doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')

while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 20 >= num and num >= 0:
        break
    print('Tente novamente, ' , end = '')

print(f'voce digitou o numero {numeros[num]}')
