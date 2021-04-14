from math import sin, cos, tan, radians

n = float(input('Digite o valor do ângulo: '))

print('O valor do Seno é {:.2f}'.format(sin(radians(n))))
print('O valor do Cosseno é {:.2f}'.format(cos(radians(n))))
print('O valor da Tangente é {:.2f}'.format(tan(radians(n))))
