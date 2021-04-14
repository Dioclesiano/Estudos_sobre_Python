from random import randint

itens = ('Par', 'Ímpar')
computador = randint(0, 1)

print('{:=^100}'.format(' PAR OU ÍMPAR '))
print()
print('Para começar escolha sua opção: ')

jogador = int(input('Digite um número » '))


if computador == 0: # Computador escolheu Par
    if jogador % 2 == 0: # Jogador escolheu Par
        print('O computador escolheu Par! \033[4;30mVocês empataram\033[m.')
    elif jogador % 2 == 1: # Jogador escolheu Ímpar
        print('O computador escolheu um número par e você escolheu um número ímpar.')
        print('\033[7;31mO Computador Ganhou!\033[m')

else: # Computador escolheu Ímpar
    if jogador % 2 == 0: # Jogador escolheu Par
        print('Você escolheu um número par e o computador escolheu um número ímpar.')
        print('\033[7;31mVocê Ganhou!\033[m')
    elif jogador % 2 == 1: # Jogador escolheu Ímpar
        print('O Computador escolheu Ímpar. Vocês empataram!')
print()
print('{:=^100}'.format(' FIM '))