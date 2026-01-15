def área(largura, comprimento):
    print(f'A área do seu terreno {largura}x{comprimento} é de {largura*comprimento:.2f} metros quadrados')

print('Controle de terrenos')
print('-' * 30)
lar = float(input('LARGURA (m): '))
com = float(input('COMPRIMENTO (m): '))
área(lar, com)
