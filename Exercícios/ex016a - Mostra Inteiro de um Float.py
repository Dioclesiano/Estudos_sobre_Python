# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

import math
n = float(input('Digite um número: '))
n1 = math.floor(n)
print('O número {} tem a parte inteira {}.'.format(n, n1))
