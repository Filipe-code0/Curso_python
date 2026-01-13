jogador = {}
gols = []
total_gols = 0
jogador['nome'] = str(input('Nome do jogador: '))
num = int(input('Quantas partidas ele jogou? '))
for i in range(0,num):
    pts = int(input(f'Quantos gols na partida{i}? '))
    total_gols += pts
    gols.append(pts)
jogador['gols'] = gols[:]
jogador['total'] = total_gols
print('-=' * 20)
print(jogador)
print('-=' * 20)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 20)
print(f'O jogador {jogador['nome']} jogou {num} partidas.')
for c,i in enumerate(gols):
    print(f'    => Na partida {c}, fez {i} gols.')
print(f'Foi um total de {jogador["total"]} gols.\n')

