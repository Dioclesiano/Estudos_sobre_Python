'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo
em uma lista composta.
'''

from random import randint
from time import sleep

lista = []
jogo = []

print()
quantidade = int(input('Digite a quantidade de jogos devem ser sorteados » '))


total = 1
while quantidade >= total:

    cont = 0
    while True: # Esse while cria somente uma lista com seis jogos.
        sorteio = randint(1, 60)

        if sorteio not in jogo:
            jogo.append(sorteio)
            cont += 1

        if cont >= 6:
            break

    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()
    total += 1

print()
print('-'*15, ' SORTEANDO ', '-'*15)
for i, l in enumerate(lista):
    sleep(1)
    print(f'\033[31mO {i+1}º Jogo é ->  \033[m{l}')
