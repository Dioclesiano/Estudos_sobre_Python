'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para
o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
n = int(input('Digite o número do seu bilhete: '))
c = random.randint(1, 5)

if n == c:
    print('Você digitou {} e o número sorteado foi {}. Parabéns Você ganhou!'.format(n,c))
else:
    print('Infelizmente você não ganhou.')



O exercício acima eu fiz. O exercício abaixo o professor fez:
Começa importando o método randint() da biblioteca RANDOM
Também vou importar método sleep() da biblioteca time para simular tempo de processamento

from random import randint
from time import sleep

computador = randint(0, 5) #Faz o computador "PENSAR"
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))  # Jogador tenta adivinhar
print('Processando...')
sleep(2)

if jogador == computador:
    print('PARABÊNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
'''

from random import randint

n = int(input('Você tem 3 tentativas para acertar o meu número. Digite aqui sua opção » '))

lista = []

cont = 0
for c in range(1, 4):
    sorteio = randint(0, 10)
    lista.append(sorteio)

    if n == sorteio:
        cont += 1

for k, v in enumerate(lista):
    print(f'O {k+1}° número sorteado foi {v}')

if n in lista:
    print(f'Você acertou {cont} vez(es). Parabéns!')
else:
    print(f'Você não acertou nenhuma vez.')
