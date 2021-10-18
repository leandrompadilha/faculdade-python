def readInt(msg):
    '''
    -> Valida se o input é int

    :param msg: Mensagem de input para o usuário digitar um valor
    '''
    red = '\033[1;31m'
    cls = '\033[0;0m'

    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'{red}ERRO! Digite um número inteiro válido.{cls}')
            continue
        except (KeyboardInterrupt):
            print(f'{red}\nEntrada de dados interrompida pelo usuário.{cls}')
            exit()
        else:
            return n


def readFloat(msg):
    '''
    -> Valida se o input é float
    :param msg: Mensagem de input para o usuário digitar um valor
    '''
    red = '\033[1;31m'
    cls = '\033[0;0m'

    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'{red}ERRO! Digite um número real válido.{cls}')
            continue
        except (KeyboardInterrupt):
            print(f'{red}\nEntrada de dados interrompida pelo usuário.{cls}')
            exit()
        else:
            return n


def validateCPF(msg, list=[]):
    '''
    -> Valida se o input é um CPF válido

    :param cpf: número do CPF
    :param list: nome da lista na qual o sistema verificará se o CPF digitado já foi cadastrado. (opcional)
    :return: número do CPF válido
    '''
    red = '\033[1;31m'
    green = '\033[1;32m'
    cls = '\033[0;0m'

    while True:
        try:
            # Input CPF
            cpf = str(input(msg)).replace('.', '').replace('-', '')
            # Valida a qtd de números digitados
            if len(cpf) != 11:
                print(
                    f'{red}CPF inválido, este documento deve conter dígitos, tente novamente{cls}'
                )
                return validateCPF()
            for i in list:
                if cpf in i['cpf']:
                    print(f'{red}CPF já cadastrado, tente novamente.{cls}')
                    return validateCPF()
            # Separação de números
            int(cpf)
            num1 = int(cpf[0])
            num2 = int(cpf[1])
            num3 = int(cpf[2])
            num4 = int(cpf[3])
            num5 = int(cpf[4])
            num6 = int(cpf[5])
            num7 = int(cpf[6])
            num8 = int(cpf[7])
            num9 = int(cpf[8])
            num10 = int(cpf[9])
            num11 = int(cpf[10])
            # Validar se todos os números são iguais
            if num1 == num2 == num3 == num4 == num5 == num6 == num7 == num8 == num9 == 0 == num11:
                print(f'{red}CPF inválido, tente novamente{cls}')
                return validateCPF()
            # Validação primeiro dígito Verificador
            primeira_soma = num1*10 + num2*9 + num3*8 + num4 * \
            7 + num5*6 + num6*5 + num7*4 + num8*3 + num9*2
            primeiro_digito = (primeira_soma * 10) % 11
            if primeiro_digito == 10:
                primeiro_digito = 0
            # Validação segundo dígito Verificador
            segunda_soma = num1*11 + num2*10 + num3*9 + num4*8 + num5 * \
            7 + num6*6 + num7*5 + num8*4 + num9*3 + primeiro_digito*2
            segundo_digito = (segunda_soma * 10) % 11
            # Comparação dos dois últimos números e conclusão
            if (primeiro_digito == num10 and segundo_digito == num11):
                return cpf
            else:
                print(f'{red}CPF é inválido, tente novamente{cls}')
                return validateCPF()
        except (ValueError, TypeError):
            continue

