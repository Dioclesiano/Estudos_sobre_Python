'''
Crie um módulo chamado MOEDA.PY que tenha as funções incorporadas AUMENTAR(), DIMINUIR(), DOBRO() e METADE().
Faça também um programa que importe esse módulo e use algumas dessas funções.
'''

# Esse módulo foi criado para o exercício 107 e copiado para o exercício 108. Neste exercício irei acrescentar uma DEF
# que coloca o símbolo de moeda no caso o Real(R$) nos dados inseridos pelo usuário. Também dará opção do usuário
# colocar a moeda desejada.

# Foram colocados as docs strings em todas as DEFs

def aumentar(preço, taxa=0):
    '''

    :param preço: É o valor do produto inserido pelo Cliente
    :param taxa: É o percentual de juros
    :return: Retorna a soma do valor do produto com a taxa
    '''
    resultado = preço + (preço * taxa/100)
    return resultado


def diminuir(preço, taxa=0):
    '''

    :param preço:É o valor do produto inserido pelo Cliente
    :param taxa: É o percentual de jros
    :return: Retorna a subtração do valor do produto com a taxa
    '''
    resultado = preço - (preço * taxa/100)
    return resultado


def dobro(preço):
    '''

    :param preço: É o valor do produto inserido pelo Cliente
    :return: Retorna o dobro do valor inserido
    '''
    resultado = preço * 2
    return resultado


def metade(preço):
    '''

    :param preço: É o valor do produto inserido pelo Cliente
    :return: Retorna a metade do valor inserido
    '''
    resultado = preço / 2
    return resultado


def real(preço=0, símbolo='R$'):
    '''

    :param preço: É o valor do produto inserido pelo Cliente
    :param símbolo: É o brasão de moeda, no caso é o R$
    :return: Retorna o valor inserido pelo cliente, formatado como moeda
    '''
    return f'{símbolo} {preço:0.2f}'. replace('.', ',')
# A palavra Replace significa 'Substituição'. Esse comando fará com que os pontos inerente da função float, sejam
# substituídos por vírgulas.