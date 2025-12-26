from datetime import date

maiores = 0
menores = 0

for i in range(0,7):
    x = int(input('Ano de nascimento: '))
    y = date.today().year - x

    if y < 21:
        menores += 1

    elif y >= 21:
        maiores += 1

print(f'QTD de maiores {maiores}, QTD de menores {menores}')

