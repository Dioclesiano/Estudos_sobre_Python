'''
Faça um programa que tenha uma função chamada CONTADOR(), que receba três parâmetros: Início, fim e passo e realize
10
a contagem. Seu programa tem que realizar três contagens através da função criada:
A) De 1 até 10, de 1 em 1;
B) De 10 até 0, de 2 em 2;
C) Uma contagem personalizada.
'''
# Na progressão teremos Início, Fim e Razão(Intervalos)
from time import sleep

def contador(i, f, r):

    if r <= 0:
        r = r * (-1)  # Esta fórmula é para que anular o negativo. Neste caso se o usuário digitar um valor
                      # menor que zero(negativo); este valor será mudado para positivo.

    if i <= f:
        cont = i
        while cont <= f:
            print(f'{cont}', end='  ', flush=True)
            sleep(0.5)
            cont += r
        print()

    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end='     ', flush=True)
            sleep(0.5)
            cont -= r


# Programa Principal
print()
print()

print(f'\033[31mNúmeros contados de 0 à 10 de 1 em 1\033[m')
contador(1, 10, 1)
print()

print(f'\033[35mNúmeros contados de 10 à 0 de 2 em 2\033[m')
contador(10, 0, 2)
print()
print()
print('AGORA É A SUA VEZ DE INSERIR VALORES PARA A CONTAGEM.')
print()

i = int(input('Digite um número para iniciar a contagem » '))
f = int(input('Digite um número para finalizar a contagem » '))
r = int(input('Digite um número para formar uma sequencia de saltos durante a contagem » '))
print()
contador(i, f, r)
