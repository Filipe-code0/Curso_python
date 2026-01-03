entrada = str(input('Digite a expressao: '))
cont = 0
for i in range(0,len(entrada)):
    
    if entrada[i] in '(':
        cont += 1

    elif entrada[i] in ')' and cont > 0:
        cont += -1

if cont != 0:
    print('incorreto')

else:
    print('Correto')
