'''
Faça um programa que tenha uma função chamada CONTADOR(), que receba três parâmetros: Início, fim e passo e realize
a contagem. Seu programa tem que realizar três contagens através da função criada:
A) De 1 até 10, de 1 em 1;
B) De 10 até 0, de 2 em 2;
C) Uma contagem personalizada.

from time import sleep

def contagem(i, f, p):

    if p < 0:
        p = p * (-1)

    if p > 0:
        if f > i:
            for c in range(i, f, p):
                print(f' {c} -> ', end='  ', flush=True)
                sleep(0.5)
            print(f)

        if i > f:
            for c in range(i, f, - p):
                print(f' {c} -> ', end='  ', flush=True)
                sleep(0.5)
            print(f)



print()
print()
print('Contagem Crescente')
for c in range(1, 11):
    print(f' -> {c}', end='  ', flush=True)
    sleep(0.5)

print()
print()

print('Contagem Decrescente')
for d in range(10, 0, -1):
    print(f' -> {d}', end='  ', flush=True)
    sleep(0.5)

print()
print()


print('Contagem Personalizada')
print()
print()

print('AGORA É SUA VEZ DE DIGITAR OS NÚMEROS')
i = int(input('Digite o número que iniciará a contagem » '))
f = int(input('Digite o número que finalizará a contagem » '))
p = int(input('Digite de quanto em quanto deseja contar » '))

print()

contagem(i, f, p)
'''
from ex098.Contagem import contagem

print('-='*30)
print('Contagem de 1 até 10 de 1 em 1')
contagem(1, 11, 1)

print('-='*30)
print('Contagem de 10 até 0 de 2 em 2')
contagem(10, 0, 2)

print('-='*30)
print('Agora é sua vez de personalizar a contagem!')
n1 = int(input('Digite o número para iniciar a contagem » '))
n2 = int(input('Digite o último número da contagem » '))
salto = int(input('Digite o intervalos dos números » '))
print('-='*30)
contagem(n1, n2, salto)
print('-='*30)
