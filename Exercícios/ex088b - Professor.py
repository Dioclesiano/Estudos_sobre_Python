'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo
em uma lista composta.
'''

from random import randint
from time import sleep

lista = list()
jogos = list()

print('-'* 30)
print('     JOGO DA MEGA SENA       ')
print('-'* 30)

print()

quantidade = int(input('Digite a quantidade de jogos » '))

total = 1
while total <= quantidade:

    cont = 0
    while True:
        sorteio = randint(1,60)

        if sorteio not in lista:
            lista.append(sorteio)
            cont += 1

        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print()
print('='*10, f'SORTEANDO {quantidade} JOGOS', '='*10)

print()

for i, l in enumerate(jogos):
    print(f'JOGO {i} -> {l}')
    sleep(1)
print()
print('-='*5, '<< Boa Sorte! >> ', '=-'*5)
