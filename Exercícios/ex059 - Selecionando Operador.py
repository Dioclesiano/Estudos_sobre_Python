# Crie um programa que leia dois valores e mostre um menu na tela:

from ex059.Definicoes import *
# Programa que fiz

n1 = float(input('Digite o primeiro número » '))
n2 = float(input('Digite o segundo número » '))

maior = ''
contador = 1

while 0 < contador <= 5:
    select = int(input('Digite um número de acordo com sua escolha: \n'
                       '[1] SOMA \n'
                       '[2] MULTIPLICAÇÃO \n'
                       '[3] MAIOR \n'
                       '[4] NOVOS NÚMEROS \n'
                       '[5] SAIR DO PROGRAMA \n'))

    if select == 1:
        print('A soma entre R$ {:.2f} + R$ {:.2f} = R$ {:.2f}'.format(n1, n2, n1+n2))

    elif select == 2:
        print('A multiplicação entre {} x {} = {}'.format(n1, n2, n1*n2))

    elif select == 3:
        if n2 > n1:
            maior = n2
            print(f'O maior número digitado é {maior}')
        elif n1 > n2:
            maior = n1
            print(f'O maior número digitado é {maior}')

    elif select == 4:
        n1 = float(input('Digite o primeiro número » '))
        n2 = float(input('Digite o segundo número » '))
    elif select == 5:
        print('Até Logo!')
        break

    else:
        print('Entrada Inválida! Tente novamente!')

print('Fim do Programa')


# Programa mais evoluído

n1 = float(input('Digite o primeiro Número » '))
n2 = float(input('Digite o segundo Número » '))

menu('Somar',
     'Subtrair',
     'Multiplicar',
     'Dividir',
     'Repetir Números',
     'Sair do Programa'
     )

escolha = 0
while escolha != 6:
    escolha = validarInteiro((input('Digite a sua opção de acordo com o MENU » ')))

    if escolha == 1:
        print(f'O resultado da soma é {formatar(somar(n1, n2))}')
    elif escolha == 2:
        print(f'O resultado da subtração é {formatar(subtrair(n1, n2))}')
    elif escolha == 3:
        print(f'O resultado da multiplicação é {formatar(multiplicar(n1, n2))}')
    elif escolha == 4:
        print(f'O resultado da divisão é {formatar(dividir(n1, n2))}')
    elif escolha == 5:
        n1 = float(input('Digite o primeiro número » '))
        n2 = float(input('Digite o segundo número » '))
    elif escolha == 6:
        print('Saindo do Sistema...')
        break
    else:
        print('Você digitou um valor incorreto. Tente novamente')

print('Fim do Programa')
