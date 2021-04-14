# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

n1 = input('1 » ')
n2 = input('2 » ')
n3 = input('3 » ')
n4 = input('4 » ')

lista = [n1, n2, n3, n4]
random.shuffle(lista)

print('A ordem sorteada de apresentação é: ')
print(lista)

# É um comando para embaralhar
