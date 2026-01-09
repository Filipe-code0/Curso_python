aluno = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) /2
    aluno.append([nome, [nota1, nota2], media])
    op = input('Quer continuar? [S/N] ').strip().upper()[0]
    if op == 'N':
        break
print('-=' * 20)
print(f'{'NO.':<4}{'Nome':<8}{'Media':>10}')
for c,i in enumerate(aluno):
    print(f'{c:<4}{i[0]:<8}{i[2]:>10.2f}')
print('-=' * 20)
while True:
    n = int(input('Mostrar notas de qual aluno? (999 interompe): '))
    if n == 999:
        print('Finalizando ...')
        break
    if n <= len(aluno)-1:
        print(f'Notas de {aluno[n][0]} são {aluno[n][1]}')
print('Volte Sempre!')
