# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

n = float(input('Entre com o valor do produto: '))

print('O valor parcelado é R$ {:.2f} e R$ {:.2f} com 5% de desconto.'.format(n, (n-(n*5)/100)))
