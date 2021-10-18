def cls():
    '''
    -> Limpa a tela 
    
    :return: Sem retorno
    '''
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        

def IR(nome, salario):
    '''
    -> Cria um dicionário com o nome do contribuinte, salário, valor do IR e salário líquido.

    :param nome: nome do contribuinte
    :param salario: salario do contribuinte
    '''
    i = dict()
    i['nome'] = nome
    i['salario'] = salario    
    if i['salario'] <= 1903.98:
        i['imposto'] = 0
    elif i['salario'] <= 2826.65:
        i['imposto'] = i['salario'] * 0.075
    elif i['salario'] <= 3751.05:
        i['imposto'] = i['salario'] * 0.15
    elif i['salario'] <= 4664.68:
        i['imposto'] = i['salario'] * 0.225
    else:
        i['imposto'] = i['salario'] * 0.275
    i['liquido'] = i['salario'] - i['imposto']
    return i
    
def out():
    '''
    -> exibe mensagem para confirmar saída do programa
    :return: Sem retorno
    '''
    red	  = '\033[1;31m'
    cls   = '\033[0;0m'
    from modules import other
    sair = input(f'Pressione {red}ENTER{cls} para sair.')
    other.cls()
    exit()