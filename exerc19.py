from random import shuffle

w = input('Aluno1: ')
x = input('Aluno2: ')
y = input('Aluno3: ')
z = input('Aluno4: ')

lista = [w,x,y,z]

shuffle(lista)

print('Ordem de aprestancao: ')
print(lista)

