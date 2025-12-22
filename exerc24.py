frase = str(input('Frase: ')).upper().strip()

print(f'A letra A aparece {frase.count('A')} vezes')
print(f'Primeiro na posição {frase.find('A')+1}')
print(f'Por ultimo na posição {frase.rfind('A')+1}')

