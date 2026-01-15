def voto(ano_nasc):
    from datetime import datetime
    ano = datetime.now().year
    idade = ano - ano_nasc
    if idade >=18 and idade < 65:
        return f'Com idade {idade} anos: Obrigatório'
    elif idade < 18 and idade >= 16 or idade >= 65:
        return f'Com idade {idade} anos: Opcional'
    elif idade < 16 and idade >= 0:
        return f'Com idade {idade} anos: Não vota'
    else:
        return f'ERRO, idade impossível'
        
print('-' * 30)
ano_nasc = int(input('Em que ano você nasceu? '))
print(voto(ano_nasc))
