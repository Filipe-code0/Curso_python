nome = str(input('Seu nome: '))

m = nome.split(' ') 

print(f'Maiusculo: {nome.upper()}, Mininusculo {nome.lower()}')
print(f'QTD. Letras: {len(nome.replace(' ',''))}, Qtd. Letras(primeiro nome): {len(m[0])}')

