# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que não quer mostrar o termo.

n = int(input('Digite o primeiro termo da Progressão Aritmética » '))
razao = int(input('Digite a razão da Progressão Aritmética » '))
primeiro = n
cont = 1
acrescimo = 10
total = 0

while acrescimo != 0:
    total += acrescimo

    while cont <= total:
        print('{} - '.format(primeiro), end='')
        primeiro += razao
        cont += 1

    print('Pausa')
    acrescimo = int(input('Digite [0] para sair ou o valor que deseja acrescentar nos termos da PA »  '))
