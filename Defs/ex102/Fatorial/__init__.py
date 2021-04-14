from math import factorial
from time import sleep


def fatorial(n, show=False):
    multi = []
    mult = 1
    cont = n
    if show == True:
        print('=×' * 40)
        print(f'Cálculo Fatorial linear de {n}...')
        while cont >= 1:
            sleep(0.7)
            print(f'{cont}', end='')
            if cont > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
            mult *= cont
            multi.append(mult)
            cont -= 1
        sleep(1)
        print(f'{mult}', end='')
        print()
        print('=×' * 40)

        print('=×' * 40)
        print(f'Cálculo Fatorial tabular de {n}...')
        sleep(0.7)
        decrescente = n-1
        soma = 0
        for k, v in enumerate(multi):
            print(f'{v:<4} x {decrescente:<1} = {v * decrescente}')
            soma += multi[k]
            decrescente -= 1
        print(f'O fatorial de {n} é {mult} e a soma dos elementos apresentados {soma}')
        print('=×' * 40)

    else:
        print('=×' * 30)
        print(f'O fatorial de {n} é » {factorial(n)}')
        print('=×' * 30)


def organizarLista(multi):
    """
    Esta função organiza de maneira decrescente os elementos de uma Lista.
    :param multi: Recebe uma lista com vários elementos de valores aleatórios
    :return: A mesma lista com os mesmos valores e elementos organizados de forma decrescente
    """
    for c in range(0, len(multi)):
        for d in range(0, len(multi)):
            if multi[c] > multi[d]:
                aux = multi[c]
                multi[c] = multi[d]
                multi[d] = aux
    return multi
