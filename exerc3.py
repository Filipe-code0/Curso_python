frase = input('Digite algo: ')

print(f'o tipo primitivo desse valor é {type(frase)}')
print(f'só tem espaço: {frase.isspace()}')
print(f'é um numeros: {frase.isnumeric()}')
print(f'é alfabetico: {frase.isalpha()}')
print(f'é alfanumerico: {frase.isalnum()}')
print(f'está em maiusculas: {frase.isupper()}')
print(f'está em minusculas: {frase.islower()}')
print(f'está capatilizada: {frase.istitle()}')

