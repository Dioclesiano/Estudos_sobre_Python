# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

n = int(input('Digite um número inteiro: '))
print('Será exibido abaixo a tabuada de Multiplicação do número selecionado.')
'''
print('='*12)
print('{} x {:2} = {}'.format(n, 0, n*0))
print('{} x {:2} = {}'.format(n, 1, n*1))
print('{} x {:2} = {}'.format(n, 2, n*2))
print('{} x {:2} = {}'.format(n, 3, n*3))
print('{} x {:2} = {}'.format(n, 4, n*4))
print('{} x {:2} = {}'.format(n, 5, n*5))
print('{} x {:2} = {}'.format(n, 6, n*6))
print('{} x {:2} = {}'.format(n, 7, n*7))
print('{} x {:2} = {}'.format(n, 8, n*8))
print('{} x {:2} = {}'.format(n, 9, n*9))
print('{} x {:2} = {}'.format(n, 10, n*10))
print('='*12)
'''
# Abaixo está a maneira simplificada de resolver e Multiplicação
for c in range(0, 11):
    print(f'{n} x {c} = {n*c}')
