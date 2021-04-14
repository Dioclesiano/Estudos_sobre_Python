# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma progressão Aritmética,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

n = int(input('Digite o primeiro termo da PA para mostrar 10 termos » '))
razao = int(input('Digite a razão para a PA » '))

cont = 1
while cont < 11:
    n += razao
    cont += 1
    print(n)
