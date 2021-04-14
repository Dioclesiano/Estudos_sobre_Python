# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# Esse exercício está completo, feito pelo professor.

from random import randint

ganhou = 0
cont = 1
while True:
    computador = randint(1, 10)
    n = int(input('Digite o número: '))
    resultado = computador + n

    selecionar = ' '
    while selecionar not in 'PI':  # Enquanto selecionar não receber 'P' ou 'I'
        selecionar = str(input('Digite sua opção: Par ou Ímpar [P/I] » ')).strip().upper()[0]

    if resultado % 2 == 0:
        if selecionar == 'P':
            print('{:~^100}'.format(''))
            print('Você Ganhou!')
            print('{:~^100}'.format(''))
            ganhou += 1
        else:
            print('{:!^100}'.format(''))
            print('Você perdeu!')
            print('{:!^100}'.format(''))
            break

    elif resultado % 2 == 1:
        if selecionar == 'I':
            print('{:~^100}'.format(''))
            print('Você Ganhou!')
            print('{:~^100}'.format(''))
            ganhou += 1
        else:
            print('{:!^100}'.format(''))
            print('Você perdeu!')
            print('{:!^100}'.format(''))
            break
    cont += 1


print(f'\033[31mVocê fez {cont} jogadas e ganhou {ganhou} vez(es).\033[m')