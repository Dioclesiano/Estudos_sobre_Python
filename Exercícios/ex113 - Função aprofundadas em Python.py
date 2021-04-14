'''
Rescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade

from ex113.Def import leiaFloat, leiaString, moeda

n = leiaFloat('Digite o valor do produto\n=> R$ ')
simbolo = leiaString('Digite o Brasão da moeda do seu País » ')

print()
print(f'O produto digitado custa \033[35m{moeda(n, simbolo)}\033[m')
'''

from ex113.Validador import *

n1 = leiaInt('Digite um Número Inteiro » ')
n2 = leiaFloat('Digite um número Decimal » ')

print(f'O Número Inteiro digitado foi {n1} e o Número Real digitado foi {n2:.2f}')
