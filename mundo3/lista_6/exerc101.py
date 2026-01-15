def ficha(nome="<desconhecido>", gols=0):
    print(f'o jogador {nome} fez {gols} gol(s) no campeonato.')

print('-'*30)
nome = str(input('Nome do jogador: '))
gols = input('Número de Gols: ')
if nome == '' and gols == '':
    ficha()
elif nome == '':
    ficha(gols=gols)
elif gols == '':
    ficha(nome=nome)
else:
    ficha(nome,gols)
