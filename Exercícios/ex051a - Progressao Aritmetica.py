# Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética.
# No final, mostre os 10 primeiros termos dessa progressão.

n1 = int(input('Digite o primeiro número para a progressão » '))
n2 = int(input('Digite o segundo número para a progressão » '))

r = n2 - n1
p = n2 + r

cont = 0
for c in range(1, 11):
    cont = cont + r
    print(cont)
