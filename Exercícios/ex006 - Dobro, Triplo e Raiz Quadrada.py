# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número inteiro: '))

print('O dobro do número digitado é » {} '.format(n*2), end=' ')
print('O triplo do número digitado é » {}'.format(n*3))
print('A raíz quadrada do número digitado é » {:.2f}'.format(n**(1/2)))
