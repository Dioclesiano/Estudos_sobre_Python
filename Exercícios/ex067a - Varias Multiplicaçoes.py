# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.


mult = 1
cont = 0
continuar = 1

while continuar > 0:
    print('{:~^100}'.format('INÍCIO'))
    n = int(input('Digite o número para montar a Tabuada de Multiplicação » '))

    for c in range(1, 11):
        print(f'{n} x {c:2} = {n*c:3}')

    cont += 1

    print()
    continuar = int(input('Digite um número positivo para continuar ou um número negativo para sair » '))
print('{:~^100}'.format('FIM'))


# Tabelas de Multiplicação de 0 à 10.
cont = 0
while cont < 11:
    print()
    for c in range(1, 11):
        print(f'{c:>2} x {cont:>2} = {c*cont:3}     ', end='')
    cont += 1
