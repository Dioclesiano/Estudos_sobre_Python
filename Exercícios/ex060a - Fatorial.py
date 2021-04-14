# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# ex: 5! = 5x4x3x2x1 = 120

from ex060.Defs import *

# Importando fatorial
from math import factorial


n = int(input('Digite um número para apresentar o Fatorial » '))
f = factorial(n)

print('O fatorial de {} é {}.'.format(n, f))

# Outras maneiras

n = int(input('Digite um número para calcular o Fatorial » '))

# Usando While
calculo = 1
crescente = 1
decrescente = n

escolha = int(input('Digite [1] para exibição em Linha ou [2] para Tabelas » '))
while crescente <= n:
    if escolha == 1:
        print(f' {decrescente} ', end='')
        if decrescente > 1:
            print('x', end='')
        else:
            print(f'= {calculo}', end='')

    elif escolha == 2:
        if calculo > 1:
            print(f'{calculo} x {decrescente} = {calculo}')
    calculo *= decrescente
    crescente += 1
    decrescente -= 1

# Usando For
lista = ['Formato Linha',
         'Formato Tablela']

print()
formatar('MENU')


for c in range(0, 2):
    print(f'Digite [{c+1}] para exibir {lista[c]} ')

print()
escolha = int(input('Digite sua opção de acordo com o MENU » '))
print()

if escolha == 1:
    fatorial = 1
    for c in range(n, 0, -1):
        print(f'{c} x ' if c > 1 else f'{c} = ', end='')
        fatorial *= c
    print(fatorial, end='')
    print()
else:
    mult = n
    cont = n - 1
    multiplicacao = 1
    for c in range(n, 1, -1):
        multiplicacao = mult * cont
        print(f'{mult:8d} x {cont:2d} = {multiplicacao}')
        mult *= cont
        cont -= 1
