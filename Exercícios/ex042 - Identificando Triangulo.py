# Reforça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo
# de triângulo será formado:
# Equilátero: Todos os lados iguais
# Isósceles: Dois lados iguais
# Escaleno: Todos os lados diferentes

n1 = int(input('Digite o valor do lado A do Triângulo » '))
n2 = int(input('Digite o valor do lado B do Triângulo » '))
n3 = int(input('Digite o valor do lado C do Triângulo » '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('='*80)
    print('Os valores informados possibilita a formação de um triângulo ', end='')
    if n1 == n2 == n3:
        print('EQUILÁTERO.')
        print('='*80)

    elif n1 != n2 != n3 != n1:
        print('ESCALENO.')
        print('='*80)

    else:
        print('ISÓSCELES.')
        print('='*80)
else:
    print('*'*80)
    print('Os valores informados não possibilita a formação de um triângulo.')
    print('*'*80)
