# Crie um programa que faça o computador jogar JOKENPÔ com você.

#  from emoji import emoji
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('\033[31mVAMOS JOGAR?')

print('''Escolha uma das opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA\033[m''')

#  print(emoji(':smile:', use_aliases=True))
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

print('processando...')
sleep(1)

print()
print('{:=^40}'.format(' JOKENPO '))
print('Computador jogou \033[4;30m{}\033[m'.format(itens[computador]))
print('Você jogou \033[4;30m{}\033[m'.format(itens[jogador]))
print('{:=^40}'.format(' FIM '))
print()

if computador == 0:  # Computador jogou Pedra
    if jogador == 0:  # Jogador jogou Pedra
        print('Empatou!')
    elif jogador == 1:  # Jogador jogou Papel
        print('Você Ganhou! Parabéns!')
    elif jogador == 2:  # Jogador jogou Tesoura
        print('O computador venceu!')
    else:
        print('Jogada Inválida!')

elif computador == 1:  # Computador jogou Papel
    if jogador == 0:  # Jogador jogou Pedra
        print('O computador venceu!')
    elif jogador == 1:  # Jogador jogou Papel
        print('Empatou!')
    elif jogador == 2:  # Jogador jogou Tesoura
        print('Você Ganhou! Parabéns!')
    else:
        print('Jogada Inválida!')

elif computador == 2:  # Computador jogou Tesoura
    if jogador == 0:  # Jogador jogou Pedra
        print('Você Ganhou! Parabéns!')
    elif jogador == 1:  # Jogador jogou Papel
        print('O computador venceu!')
    elif jogador == 2:  # Jogador jogou Tesoura
        print('Empatou!')
    else:
        print('Jogada Inválida!')
