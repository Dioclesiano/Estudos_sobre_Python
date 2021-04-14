'''
Crie um módulo chamado MOEDA.PY que tenha as funções incorporadas AUMENTAR(), DIMINUIR(), DOBRO() e METADE().
Faça também um programa que importe esse módulo e use algumas dessas funções.
'''

def aumentar(preço, taxa):
    resultado = preço + (preço * taxa/100)
    return resultado


def diminuir(preço, taxa):
    resultado = preço - (preço * taxa/100)
    return resultado


def dobro(preço):
    resultado = preço * 2
    return resultado


def metade(preço):
    resultado = preço / 2
    return resultado
