# Cálculo da Hipotenusa através do MATH

import math

oposto = float(input('Comprimento do Cateto Oposto: '))
adjascente = float(input('Comprimento do Cateto Adjascente: '))
hipotenusa = math.hypot(oposto, adjascente)

print('A hipotenusa vai medir {:.2f}.'.format(hipotenusa))
