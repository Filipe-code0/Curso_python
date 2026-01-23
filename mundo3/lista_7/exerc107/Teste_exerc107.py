import moeda

p = float(input('Digite o preco: R$'))
print(f'A metade de {moeda.f_moeda(p,"U$")} eh {moeda.metade(p, moeda = 'U$')}')
print(f'A dobro de {moeda.f_moeda(p, "L$")} eh {moeda.dobro(p, moeda = 'L$')}')
print(f'Aumentando 10% de {p} eh {moeda.aumentar(p,10)}')
print(f'Diminuindo 13% de {p} eh {moeda.diminuir(p,13)}')
