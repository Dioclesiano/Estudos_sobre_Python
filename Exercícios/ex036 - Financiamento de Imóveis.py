#  Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar
#  o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#  Calcule o valor da prestação mensal. sabendo que ela não pode exceder 30% do salário ou então o empréstimo
#  será negado.

'''
casa = float(input('Digite o valor do Imóvel » '))
salario = float(input('Digite o valor do salário do comprador » '))
ano = int(input('Digite em quantos anos deseja pagar » '))

prestacao = casa / (ano * 12)
minimo = salario * 30 / 100

if prestacao <= minimo:
    print('\033[31mFinanciamento aprovado!\033[m')
    print('Você pagará em {} anos, prestações mensais de R$ {:.2f} no Imóvel avaliado'
          ' em {:.2f}.'.format(ano, prestacao, casa))
else:
    print('\033[7;31mFinanciamento não Aprovado\033[m')
'''
from ex036.função import *

casa = float(input('Digite o valor do imóvel » '))
salario = float(input('Digite seu salário » '))
tempo = ano(int(input('Digite em quantos anos irá pagar » ')))

print()
print(f'O patrimônio de {real(casa)} gera prestações de {real(prestacao(casa, tempo))} durante {tempo} meses.')
print(f'o valor das prestações devem estar abaixo de {real(condicao(salario))} equivalente a 70% do salário informado')
print(f'O resultado foi: ', end='')

if prestacao(casa, tempo) <= condicao(salario):
    print('\033[35mAprovado\033[m')
else:
    print('\033[7;31mReprovado\033[m')
