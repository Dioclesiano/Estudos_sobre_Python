'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras
que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas gerados.
'''

lista = []
pares = []
impares = []

# Comando para criar a lista
while True:
    n = int(input('Digite um valor » '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        n % 2 == 1
        impares.append(n)

# Comando para sair do programa
    stop = ' '
    while stop not in 'sc':
        stop = str(input('Digite [C] para Continuar ou [S] para Sair » ')).strip().lower()

    if stop == 's':
        break
print()
print(' * '*30)
lista.sort()
print(f'A lista digitada é {lista}')

pares.sort()
print(f'Os números pares dessa lista são {pares}')

impares.sort()
print(f'Os números ímpares dessa lista são {impares}')
print(' * '*30)
