# Melhore o jogo DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

# Código que eu fiz

import random
computador = random.randint(0,10)
n = int(input('Olá! Sou o seu computador. Adivinhe o número que pensei » '))

while n != computador:
    if n < computador:
        print('Você errou! Digite um valor maior.')
        n = int(input('Olá! Sou o seu computador. Adivinhe o número que pensei » '))
    elif n > computador:
        print('Você errou! Digite um valor menor.')
        n = int(input('Olá! Sou o seu computador. Adivinhe o número que pensei » '))

print('Parabéns! Você acertou.')

# Código que o professor fez

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

acertou = False

cont = 0

while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    cont += 1

    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Tente novamente. Digite um valor maior.')
        elif jogador > computador:
            print('Tente novamente. Digite um valor menor.')

print('Parabéns! Você acertou com {} tentativas.'.format(cont))


# Outra Solução

from random import randint

computador = randint(0, 10)

while True:
    cliente = int(input('Digite um número » '))

    if cliente > computador:
        print('Digite um número menor')
    elif cliente < computador:
        print('Digite um número maior')
    else:
        print('Parabéns, conseguiu!')
        break
