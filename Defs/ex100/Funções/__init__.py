from random import randint


def sorteia(n):
    for c in range(1, 6):
        n = randint(0, 100)
        return n


def somaPar(n):
    # Para somar todos os elementos da lista usaria esse comando.
    # return sum(sorteia(n))
    soma = 0
    for c in n:
        if c % 2 == 0:
            soma += c
    return soma