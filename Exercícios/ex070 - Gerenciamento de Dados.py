# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
# perguntar se o usuário vai continuar. No final, mostre:
# A - Qual é o total gasto na compra.
# B - Quantos produtos custam mais de R$ 1000.00
# C - Qual é o nome do produto mais barato.

from ex069.Defs import formatar
print('{:=^50}'.format(''))
print('{:-^50}'.format(' LOJA SUPER BARATÃO '))
print('{:=^50}'.format(''))

print()

total = totmil = menor = cont = 0

barato = ''  # Variável que contabiliza o produto de menor valor
parada = ' '  # Variável que define o final do loop quando for digitado 'n'.
while parada not in 'n':
    produto = str(input('Digite o nome do Produto » ')).strip().lower()

    preço = float(input('Digite o preço do produto R$ '))
    total += preço
    cont += 1

    if preço >= 1000:
        totmil += 1

    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto

    parada = ' '
    while parada not in 'sn':
        parada = str(input('Digite [N] para sair ou [S] para continuar » ')).strip().lower()[0]

print()
formatar(f'O total das compras foi R$ {total:.2f} \n'
         f'Encontramos >> {totmil} << compras com valores acima de R$ 1.000,00 \n'
         f'O produto mais barato é {barato} custando R$ {menor:.2f}')
