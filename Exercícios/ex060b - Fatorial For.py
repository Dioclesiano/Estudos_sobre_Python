# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# ex: 5! = 5x4x3x2x1 = 120

n = int(input('Digite o número para Fatorar » '))

f = 1
for c in range(n, 0, -1):
    f *= c
    print(' {} '.format(c), end=' x ' if c > 1 else ' = ')
print(f)
