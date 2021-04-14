# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[30m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='\033[36m » \033[m')

print('FIM')
print('\nO número {} é divisível pelos números em branco.'.format(n))

if cont == 2:
    print('{:*^32}'.format(''))
    print('** O número digitado é PRIMO  **')
    print('{:*^32}'.format(''))
else:
    print('{:!^39}'.format(''))
    print('!!  \033[7;31;40m O número digitado não é PRIMO \033[m  !!')
    print('{:!^39}'.format(''))
