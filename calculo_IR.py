# imports
from useful import other
from useful import number
from useful import string


# functions
def IR(nome, cpf, salario):
    '''
    -> Cria um dicionário com o nome do contribuinte, salário, valor do IR e salário líquido.

    :param nome: nome do contribuinte
    :param salario: salario do contribuinte
    '''
    x = dict()
    x['nome'] = nome
    x['cpf'] = cpf
    x['salario'] = salario
    if x['salario'] <= 1903.98:
        x['imposto'] = 0
    elif x['salario'] <= 2826.65:
        x['imposto'] = x['salario'] * 0.075
    elif x['salario'] <= 3751.05:
        x['imposto'] = x['salario'] * 0.15
    elif x['salario'] <= 4664.68:
        x['imposto'] = x['salario'] * 0.225
    else:
        x['imposto'] = x['salario'] * 0.275
    x['liquido'] = x['salario'] - x['imposto']
    return x


# lists
contribuintes = list()

# colors
red = '\033[1;31m'
green = '\033[1;32m'
cls = '\033[0;0m'
sub = '\033[4m'

# inputs
other.cls()
qtd = number.readInt('Olá, por favor digite a quantidade de contribuintes: ')
other.cls()

# process
for i in range(qtd):
    nome = string.readStr(f'Digite o nome do {i+1}º contribuinte: ')
    cpf = number.validateCPF('Digite seu CPF: ', contribuintes)
    salario = float(number.readFloat('Digite seu salário: R$'))
    contribuinte = IR(nome, cpf, salario)
    contribuintes.append(contribuinte.copy())
    other.cls()

# return
print(f'{sub}CONTRIBUINTES CADASTRADOS:{cls}\n')

somaImposto = 0
for i in contribuintes:
    nome = i['nome']
    cpf = i['cpf']
    renda = i['salario']
    imposto = i['imposto']
    liquido = i['liquido']

    print(
        f'Contribuinte:{green}{nome}{cls}\n'
        f'CPF:{green} {cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:]}{cls}\n'
        f'Salário:{green} R${renda:.2f}{cls}\n'
        f'Valor IR descontado:{green} R${imposto:.2f}{cls}\n'
        f'Salário líquido:{green} R${liquido:.2f}{cls}\n')

    x = i['imposto']
    somaImposto += x

mediaImposto = somaImposto / qtd
print(
    f'A SOMA do imposto dos contribuintes cadastrados é: {green}R${somaImposto:.2f}{cls}\n'
    f'A MÉDIA do imposto dos contribuintes cadastrados é: {green}R${mediaImposto:.2f}{cls}\n'
)

other.out()
