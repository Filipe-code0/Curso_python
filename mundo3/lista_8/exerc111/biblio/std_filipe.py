def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))

        except KeyboardInterrupt:
            print(f'\n\033[1;31;40mUsuario preferiu nao digitar o numero\033[m')
            return 0
            break

        except:
            print('\033[1;31;40mERRO: por favor, digite um valor valido\033[m')
            continue

        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        
        except KeyboardInterrupt:
            print(f'\n\033[1;31;40mUsuario preferiu nao digitar o numero\033[m')
            return 0
            break

        except:
            print('\033[1;31;40mERRO: por favor, digite um valor valido\033[m')
            continue

        else:
            return n

