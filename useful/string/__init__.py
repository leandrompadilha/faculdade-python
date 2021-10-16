def readStr(msg):
    '''
    -> Valida se o input é str
    :param msg: Mensagem de input para o usuário digitar um valor
    '''
    red = '\033[1;31m'
    cls = '\033[0;0m'

    while True:
        try:
            n = str(input(msg))            
        except (ValueError, TypeError):
            print(f'{red} ERRO! Digite seu nome.{cls}')
            continue
        except (KeyboardInterrupt):
            print(f'{red} Entrada de dados interrompida pelo usuário.{cls}')
            exit()
        else:
            return n
            
