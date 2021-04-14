# Faça um programa que leia três números e mostre qual é o maior e qual é o menor


'''
from time import sleep

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
print('Analisando números ... ')
sleep(1)

# Descobrindo o menor número digitado
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2

if n3 < n1 and n3 < n2:
    menor = n3

# Descobrindo o maior número digitado
maior = n3
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2

print('\033[32mO menor número é \033[31;43m{}\033[m'.format(menor))
print('\033[31mO maior número é \033[4;35;46m{}\033[m'.format(maior))


Resolvendo a mesma atividade de uma maneira mais complexa
'''

from ex033.Defs import *  # Quando utilizo o símbolo * durante a importação eu importo tudo.
from time import sleep

lista = []

print('Será pedido que digite 3 números por vez')
for c in range(2, -1, -1):
    lista.append(int(input('Digite um número » ')))
    print(f'Resta {c}')

print()

for k, v in enumerate(lista):
    print(f'O {k+1}° número digitado foi {v}')

print()
print('{:=^30}'.format('RESULTADO'))
sleep(3)
print(f'O menor número digitado é {Menor(lista[0], lista[1], lista[2])}')
print(f'O maior número digitado é {Maior(lista[0], lista[1], lista[2])}')
print(f'FIM'.center(30))
