# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# * O primeiro valor é MAIOR
# * O segundo valor é MAIOR
# * Não existe valor maior, os dois são iguais

n1 = int(input('Digite um número inteiro » '))
n2 = int(input('Digite outro número inteiro » '))

if n1 < n2:
    print('O primeiro número (\033[4m{}\033[m) é o menor e o segundo número (\033[4m{}\033[m) é o '
          'maior valor.'.format(n1, n2))
elif n1 > n2:
    print('O segundo número (\033[4m{}\033[m) é o menor e o primeiro número (\033[4m{}\033[m) é o '
          'maior valor.'.format(n2, n1))
else:
    print('Os números digitados tem o mesmo valor.')
