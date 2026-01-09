jogador = {}
gols = []
elenco = []
total_gols = 0
while True:
    jogador.clear()
    gols.clear()
    total_gols = 0
    jogador['nome'] = str(input('Nome do jogador: '))
    num = int(input('Quantas partidas ele jogou? '))
    for i in range(0,num):
        pts = int(input(f'Quantos gols na partida{i}? '))
        total_gols += pts
        gols.append(pts)
    jogador['gols'] = gols[:]
    jogador['total'] = total_gols
    elenco.append(jogador.copy())
    op = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if op == 'N':
        break
print('-=' * 20)
print(f'{'cod:<5'}{'nome:<5'}{'gols:>5'}{'total:>5'}')
print('-' * 20)
for c,i in enumerate(elenco):
    print(f'{c:<5}{elenco[i]["nome"]:<5}{}{}')
print(f'Foi um total de {jogador['total']} gols.\n')

