cont = soma = 0

while True:
    x = int(input('Digite um numero (999 para parar): '))
    if x == 999:
        break
    soma +=x
    cont+=1

print(f'a soma de {cont} valores = {soma}')
