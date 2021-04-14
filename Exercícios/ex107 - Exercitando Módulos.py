'''
107 - Crie um módulo chamado MOEDA.PY que tenha as funções incorporadas AUMENTAR(), DIMINUIR(), DOBRO() e METADE().
Faça também um programa que importe esse módulo e use algumas dessas funções.
'''
from ex107 import moedas
n = float(input('Digite o valor do produto » '))
print(f'O dobro do valor digitado é R$ {moedas.dobro(n):0.2f}')
print(f'A metade do valor digitado é R$ {moedas.metade(n):0.2f}')
print()
taxa = int(input('Digite o percentual da Taxa » '))
print(f'O aumento de {taxa}% sobre {n:0.2f} corresponde a {moedas.aumentar(n, taxa):0.2f}')
print(f'O desconto de {taxa}% sobre {n:0.2f} corresponde a {moedas.diminuir(n, taxa):0.2f}')
