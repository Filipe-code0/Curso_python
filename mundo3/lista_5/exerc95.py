def escreva(txt):
    tam = len(txt)+4
    print(f'{"~" * tam}')
    print(f'  {txt}')
    print(f'{"~" * tam}')


texto = str(input('Texto: '))
escreva(texto)
