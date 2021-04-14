# Importando um método da função MATH

from math import hypot
oposto = float(input('Digite o valor do Cateto Oposto: '))
adjascente = float(input('Digite o valor do Cateto Adjascente: '))
hipotenusa = hypot(oposto, adjascente)

print('O valor da Hipotenusa é {:.2f}.'.format(hipotenusa))
