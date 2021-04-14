# Importando Métodos da biblioteca MATH

from math import radians, sin, cos, tan

n = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(n))
print('O ângulo de {} tem o SENO de {:.2f}'.format(n, seno))
cosseno = cos(radians(n))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(n, cosseno))
tangente = tan(radians(n))
print('O ângulo {} tem a TANGENTE de {:.2f}'.format(n, tangente))
