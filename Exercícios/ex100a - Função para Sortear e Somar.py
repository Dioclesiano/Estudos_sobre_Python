'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas SORTEIA() e SOMAPAR(). A primeira
função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os
valores PARES sorteados pela função anterior.

from random import randint

# Função SORTEIA()
def sorteia(total):
    n = randint(0, total)
    numeros.append(n)

# Função SOMAPAR()
def somapar(soma):
    print(soma)


# Listas
numeros = []

# Programa Principal
total = int(input('Digite o limite de contagem para sortear cinco elementos. De 0 até ... » '))
for c in range(0, 5):
    sorteia(total)

soma = 0
for k, v in enumerate(numeros):
    if v % 2 == 0:
        print(f'\033[36mO {k+1}° número digitado é par >> {v}.\033[m')
        soma += v

    else:
        print(f'\033[31mO {k+1}° número sorteado não é par >> {v}.\033[m')


print(f'\nA soma dos valores pares é {soma}')

'''

from ex100.Funções import sorteia, somaPar
from time import sleep

numero = []
n = 0

print('Sorteando .', end=' ')
sleep(0.5)
print('.', end=' ')
sleep(0.5)
print('.', end=' ')
sleep(0.5)
print()
for c in range(1, 6):
    num = sorteia(n)
    numero.append(num)
    print(f'{num}', end='  ')
print()
print('=*'*30)
for k, v in enumerate(numero):
    print(f'O {k+1}° número sorteado foi {v}')
print('=*'*30)
print(f'O maior número Par >>> {somaPar(numero)} <<<')
