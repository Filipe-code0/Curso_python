def isfloat(arg):
    if arg == "":
        return False
    cont = pontos = 0
    for i in arg:
        if i not in '0123456789.,':
            return False
        if i in ',.':
            pontos += 1
            if cont == 0 or pontos > 1:
                return False
        cont += 1
    return True

def leiaDinheiro():
    txt = input('Digite o preco: R$').strip()
    while isfloat(txt) == False:
        print(f'ERRO {txt} eh um preco invalido!')
        txt = input('Digite o preco: R$')
    res = float(txt.replace(',','.'))
    return res

