def aumentar(n1, n2 ):
    soma = n1 + n2
    print(f'\033[45m{n1:0.2f} + {n2:0.2f} = \033[31m{soma:0.2f}\033[m')


def diminuir(n1, n2):
    sub = n1 - n2
    print(f'\033[42m{n1:0.2f} - {n2:0.2f} = \033[31m{sub:0.2f}\033[m')


def dobro(n1):
    multi = n1 * 2
    print(f'\033[42mO dobro de {n1:0.2f} é \033[31m{multi:0.2f}\033[m')


def metade(n1):
    metad = n1/2
    print(f'\033[44mA metade de {n1:0.2f} é \033[31m{metad:0.2f}\033[m')
