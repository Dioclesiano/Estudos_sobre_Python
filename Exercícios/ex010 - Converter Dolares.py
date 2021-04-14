# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere U$$ 1.00 = R$ 3.27

n = float(input('Digite o valor que deseja converter em Dólares: '))

print('U$$ {:.2f} corresponde a »» R$ {:.2f}'.format(n, n*3.27).replace('.', ','))
