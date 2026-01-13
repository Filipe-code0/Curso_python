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
print(f'{'cod':<5}{'nome':<5}{'gols':>5}{'total':>10}')
print('-' * 40)
for c,i in enumerate(elenco):
    print(f'{c}     {i["nome"]}     {i["gols"]}     {i["total"]}')
print('-' * 40)
while True:
    num = int(input('Mostrar dados de qual jogador? '))
    if num == 999:
        break
    elif num > len(elenco)-1:
        print('JOGADOR NÃO ENCONTRADO')
        print('-' * 40)
    else:
        print(f'Levantamento do jogador {elenco[num]["nome"]}')
        for c,i in enumerate(elenco[num]["gols"]):
            print(f'No jogo {c} fez {i} gols.')
        print('-' * 40)

