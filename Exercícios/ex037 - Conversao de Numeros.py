# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para Binário
# 2 para Octal
# 3 para Hexadecimal

'''
from time import sleep

n1 = int(input('Digite um número inteiro » '))
print('[1] para Binário')
print('[2] para Octal')
print('[3] para Hexadecimal')
n2 = int(input('Digite sua opção de conversão » '))

if n2 == 1:
    print('Convertendo para Binário...')
    sleep(1)
    print('*' * 50)
    print('O número decimal {} equivale a »> \033[1m{}\033[m <« em Binário.'.format(n1, bin(n1)[2:]))
    print('*' * 50)
elif n2 == 2:
    print('Convertendo para Octal...')
    sleep(1)
    print('*' * 50)
    print('O número decimal {} equivale a »> \033[1m{}\033[m <« em Octal'.format(n1, oct(n1)[2:]))
    print('*' * 50)
elif n2 == 3:
    print('Convertendo para Hexadecimal...')
    sleep(1)
    print('*' * 50)
    print('O número decimal {} equivale a \033[1m{}\033[m em Hexadecimal.'.format(n1, hex(n1)[2:]))
    print('*' * 50)
else:
    print('\033[1:31mNão identificado. Tente novamente!')


'''
from time import sleep

conversoes = ['Binário',
              'Hexadecimal',
              'Octal']

print('')
n = int(input('Digite um número decimal para ser convertido » '))

# Usei um For para exibir as opções  de escolha
print()
print('SELECIONE'.center(30))
for c in range(0, 3):
    print(f'[{c+1}] para conversão {conversoes[c]} ')

print()
while True:
    try:
        escolha = int(input('Digite sua opção de conversão » '))

        if escolha == 0 or escolha == -1 or escolha == -2:
            continue

        print()
        if escolha > 1 or escolha < 4:
            print(f'A opção selecionada foi \033[31m{conversoes[escolha - 1]}\033[m')
            print()

            print(f'Analisando ')
            for c in range(0, 3):
                print('.')
                sleep(1)

            print()
            print('RESULTADO'.center(30))
            valido = False
            while not valido:
                if escolha == 1:
                    valido = True
                    print(f'O número decimal {n} corresponde a >> {bin(n)[2:]} << em {conversoes[escolha - 1]}')

                elif escolha == 2:
                    valido = True
                    print(f'O número decimal {n} corresponde a >> {hex(n)[2:]} << em {conversoes[escolha - 1]}')
                elif escolha == 3:
                    valido = True
                    print(f'O número decimal {n} corresponde a >> {oct(n)[2:]} << em {conversoes[escolha - 1]}')
            break
        else:
            print('Erro')
    except IndexError:
        print('Entrada Inválida! Digite um número inteiro intre [1 e 3]')
