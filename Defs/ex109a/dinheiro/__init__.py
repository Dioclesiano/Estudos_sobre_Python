def aumentar(preço, taxa):
    '''

    #:param preço: Valor do Produto inserido pelo Cliente
    #:param taxa: Porcentagem da taxa inserido pelo Cliente
    #:return: Retorna a soma do parcelamento total com juros incluídos
    '''
    soma = preço + (preço*taxa)/100
    return soma

def valor(preço, simbolo):
    '''

    :param preço: Valor do Produto inserido pelo Cliente
    :param simbolo: Brasão da moeda desejada inserida pelo Cliente
    :return: Retorna o valor do produto formatado pela moeda desejada
    '''
    return f'{simbolo}{preço:0.2f}'.replace('.', ',')

# Aqui é outras opções para DEF

def aumentar(n=0, taxa=0):
    soma = n + (n*taxa)/100
    return soma

def diminuir(n=0, taxa=0):
    dim = n - (n*taxa)/100
    return dim

def real(n=0, simbolo='R$'):
    return f'\033[31m{simbolo}{n:0.2f}\033[m'.replace('.', ',')



def aumento(n=0, taxa=0, formato=False):
    soma = n + (n * taxa)/100
    return f'{soma:0.0f}' if formato is False else real(soma)

def diminuir(n, taxa, formato=False):
    dim = n - (n * taxa)/100
    return f'{dim:0.0f}' if formato is False else real(dim)

def formatando(msg):
    tamanho = len(msg) + 4

    print('='*tamanho)
    print(' ', msg)
    print('='*tamanho)

def real(n=0, simbolo='R$'):
    return f'{simbolo}{n:0.2f}'.replace('.', ',')