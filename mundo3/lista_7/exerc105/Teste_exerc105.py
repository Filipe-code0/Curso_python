import moeda

p = float(input('Digite o preco: R$'))
print(f'A metade de {p} eh {moeda.metade(p)}')
print(f'A dobro de {p} eh {moeda.dobro(p)}')
print(f'Aumentando 10% de {p} eh {moeda.aumentar(p,10)}')
print(f'Diminuindo 13% de {p} eh {moeda.diminuir(p,13)}')
