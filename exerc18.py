from random import choice

aluno1 = input('Nome: ')
aluno2 = input('Nome: ')
aluno3 = input('Nome: ')
aluno4 = input('Nome: ')

lista = [aluno1, aluno2, aluno3, aluno4]

print(f'o sorteado pela professora: foi o aluno {choice(lista)}')

