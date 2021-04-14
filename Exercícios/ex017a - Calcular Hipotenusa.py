# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa.

oposto = float(input('Digite o valor do Cateto Oposto: '))
adjascente = float(input('Digite o valor do Cateto Adjascente: '))
hipotenusa = (oposto**2 + adjascente**2) ** (1/2)
print('A hipotunusa vai medir {:.2f}.'.format(hipotenusa))
