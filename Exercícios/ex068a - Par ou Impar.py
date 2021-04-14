# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador
# perder mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# Esse exercício que fiz faltou o loop
'''
from random import randint

print('{:~^100}'.format(' VAMOS JOGAR PAR OU ÍMPAR '))

computador = randint(1, 1000)

n = int(input('Digite o número selecionado » '))
p = str(input('Digite sua opção [P]Par ou [I]Ímpar » ')).strip().upper()

soma = computador + n

print()
print('{:~^100}'.format(' Relatório '))
print('{:=^40}'.format(''))
print(f'A soma dos valores foi {soma}')
print(f'O computador jogou {computador} e você jogou {n}.')
print('{:=^40}'.format(''))

cont = 1
while True:
    if soma % 2 == 0:
        if p == 'P':
            print('\033[31mVocê ganhou por escolher Par!\033[m')
            break
        else:
            print('\033[7;31mO computador ganhou por escolher Par!\033[m')
            break

    else:
        soma % 2 == 1
        if p == 'I':
            print('\033[31mVocê ganhou por escolher Ímpar!\033[m')
            break
        else:
            print('\033[31mO computador ganhour por escolher Ímpar!\033[m')
            break

    cont += 1

print('{:~^100}'.format(''))


'''

from random import randint
from ex068.Definições import parImpar

cont = 0
while True:
    escolha = 'a'
    while escolha not in 'P I':
        escolha = str(input('Digite P[Par] ou I[Ímpar] » ')).upper()[0]

    computer = randint(0, 100)
    jogador = int(input('Digite seu número » '))

    soma = computer + jogador

    if escolha == 'P':
        if parImpar(soma) == 'P':
            print(f'Você Ganhou! O resultado {soma} é Par. Você escolheu {jogador} e o computador {computer}')
            cont += 1
        else:
            print(f'Você perdeu! O resultado {soma} é Ímpar. Você escolheu {jogador} e o computador {computer}')
            break
    elif escolha == 'I':
        if parImpar(soma) == 'I':
            print(f'Você Ganhou! O resultado {soma} é Ímpar. Você escolheu {jogador} e o computador {computer}')
            cont += 1
        else:
            print(f'Você perdeu! O resultado {soma} é Par. Você escolheu {jogador} e o computador {computer}')
            break

print(f'Parabéns! Você ganhou {cont} vez(es).')
