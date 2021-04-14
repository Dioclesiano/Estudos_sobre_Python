# Refaça o desafio 009. Mostrando a tabuada de um número que o usuário escolher.
# Só que agora utilizando um laço FOR.

n = int(input('Digite um número para criar uma tabuada de multiplicação » '))

for c in range(1, 11):
    print('{} x {:2} = {:2}'.format(n, c, n*c))
