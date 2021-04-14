# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

'''
n = int(input('Digite um número inteiro: '))

if n % 2 == 0:
    print('O número digitado é Par.')
else:
    print('O número digitado é Ímpar.')


Abaixo criei um programa um pouco mais complexo
'''

from random import randint

def imparPar(a):
    if a % 2 == 0:
        return f'Par'
    if a % 2 == 1:
        return f'Ímpar'


while True:
    while True:
        pedido = str(input('Deseja Par ou Ímpar » ')).lower()
        if pedido in 'par p':
            print('Você escolheu PAR')
            break
        elif pedido in 'impar ímpar i':
            print('Você escolheu ÍMPAR')
            break
        else:
            print('Deu erro')


    n = int(input('Digite um número » '))
    print(imparPar(n))


    sorteio = randint(0, 1000)
    print(f'O resultado é {sorteio} que é {imparPar(sorteio)}')

    computer = randint(0, 1000)
    print(imparPar(computer))



    if imparPar(n) == imparPar(computer):
        print('Empatamos. Vamos denovo.')
    elif imparPar(n) == imparPar(sorteio):
        print('Parabéns! Você ganhou')
        break
    elif imparPar(computer) == imparPar(sorteio):
        print('Eu ganhei de você. O computador arrasa.')


print('-_'*20)
print('{:=^40}'.format(' CAMPEÃO '))
print(f'-_'*20)
