n = int(input('Numero: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print(f'unidade: {u}, dezena: {d}, centena: {c}, milhar: {m}')

