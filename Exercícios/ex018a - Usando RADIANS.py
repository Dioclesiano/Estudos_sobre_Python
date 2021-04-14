# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
# Foi necessário converter em radiano
import math

n = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(n))
print('O ângulo de {:.2f} tem o SENO de {:.2f}.'.format(n, seno))
cosseno = math.cos(math.radians(n))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(n, cosseno))
tangente = math.tan(math.radians(n))
print('O ângulo de {:.2f} tem a TANGENTE de {:.2f}'.format(n, tangente))

'''
CURIOSIDADE

*RADIANOS - O cálculo do radiano é feito a partir de uma cifcunferência. O radiano surge das medidas do Arco e Raio.

*CATETOS - São os dois lados menores do triângulo retângulo, sendo que o maior é a hipotenusa.
SENO - É a razão entra a medida do cateto oposto ao ângulo agudo e a medida da hipotenusa de um triângulo retângulo.
sen = (cateto Oposto) / hipoteunusa

*COSSENO - É a razão entre a medida do cateto adjacente ao ângulo agudo e a medida da hipotenusa de um 
triângulo retângulo.
cos = (cateto adjjacente)/hipotenusa

*TANGENTE - É a razão entre a medida do cateto oposto e a medidad do cateto adjacente ao ângulo agudo de um triângulo
retângulo.
tg = (cateto oposto)/cateto adjacente
'''
