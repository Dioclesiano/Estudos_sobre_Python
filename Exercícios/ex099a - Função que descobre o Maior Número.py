'''
Faça um programa que tenha uma função chamda MAIOR(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(lista):
    for k, v in enumerate(lista):

        if k == 0:
            maior = v
        else:
            if v > maior:
                maior = v

    print(f'\nO maior número digitado foi \033[31m >> {maior} << \033[m')
    print()


# Programa Principal
lista = []
while True:
    n = int(input('Digite um número » '))
    lista.append(n)


    # Comandos para finalizar o Programa
    while True:
        stop = str(input('Deseja continuar » ')).upper()[0]
        if stop in 'SN':
            break
        print('Digite somente S[Sim] ou N[Não]')

    if stop in 'N':
        break

# Chamando uma função MAIOR()
print('Analisando')
print('.', end=' ', flush=True)
sleep(1)
print('.', end=' ', flush=True)
sleep(1)
print('.', end=' ', flush=True)
sleep(1)
print()
print('-_'*20)
maior(lista)
print('-_'*20)
'''

from ex099.Maior import maior
from random import randint

listas = []

cont = 0
while cont < 5:
    lista = []
    for c in range(0, 8):
        numero = randint(0, 100)
        if numero not in lista:
            lista.append(numero)
    listas.append(lista)
    cont += 1

maior(listas)