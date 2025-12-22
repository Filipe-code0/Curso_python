#tabela para cores no terminal
#
# estilo    |    texto     |    fundo
# 0 nenhum  |  30 branco   | 40 branco
# 1 grifado |  31 vermelho | 41 vermelho   
# 4 _____   |  32 verde    | 42 verde
# 7 neg.    |  33 amarelo  | 43 amarelo
#           |  34 azul     | 44 azul
#           |  35 roxo     | 45 roxo 
#           |  36 ciano    | 46 ciano 
#           |  37 cinza    | 47 cinza
#
# padrao: \033["estilo";"texto";"fundo"m
# \033[m para limpar
#pode se usar variaveis com fstrings

#vermelho 
print('\033[1;31;40mOla mundo\033[m')

#amarelo sublinhado
amarelo = '\033[4;33;40m'
limpar = '\033[m'
print(f'{amarelo}Ola mundo{limpar}')

#preto e branco
pretobranco = '\033[7;40m'
print(f'{pretobranco}Ola mundo{limpar}')

