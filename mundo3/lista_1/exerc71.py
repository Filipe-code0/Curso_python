clubes = ('Flamengo','Palmeiras','Cruzeiro','Mirassol','Fluminense',
          'Botafogo','Bahia','São Paulo','Grêmio','Red Bull',
          'Atlético Mineiro','Santos','Corinthians','Vasco da Gama',
          'Vitória','Internacional','Ceará','Fortaleza','Juventude','Sport')

print('-=' * 40)
print(f'Lista de times do Brasileirão: {clubes}')
print('-=' * 40)
print(f'Os 5 primeiros são: {clubes[0:5]}')
print('-=' * 40)
print(f'Os 4 ultimos são: {clubes[-4:]}')
print('-=' * 40)
print(f'Times em ordem alfabética: {sorted(clubes)}')
print('-=' * 40)
print(f'O Juventude está em {(clubes.index('Juventude')) + 1}')
print('-=' * 40)
