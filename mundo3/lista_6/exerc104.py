def ajuda(com):
    help(com)


while True:
    comando = str(input('Comando ou biblioteca >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
