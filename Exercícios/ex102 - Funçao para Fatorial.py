'''
Crie um programa que tenha uma função FATORIAL() que receba dois parâmetros: O primeiro que indique o número a calcular
e o outro chamado SHOW, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de
cálculo do fatorial.


def fatorial(n, show=True):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta/operação matemática
    :return: O valor do Fatorial de um número n.
    """
    cont = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        cont *= c
    return cont


# Programa Principal
n = int(input('Digite um número para calcular o seu fatorial » '))
print(fatorial(n, show=True))

# Show é um comando que permite mostrar ou ocultar a operação matemática

'''

from random import randint
from ex102.Fatorial import fatorial

num = randint(1, 10)
show = ' '
while show not in 'SN':
    show = str(input(f'Deseja exibir as operações que calcula o fatorial de {num} [S/N] » ')).upper()[0]
    if show == 'S':
        show = True
        break
    elif show == 'N':
        show = False
        break
    else:
        print('Entrada Inválida! Digite [S] para exibir as operações ou [N] para não exibir.')

print('=×'*40)
fatorial(num, show)
print('=×'*40)