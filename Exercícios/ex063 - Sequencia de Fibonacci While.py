# Escreva um programa que leia um número N inteiro qualquer e mostre na tela
# os N primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8


n = int(input('Digite quantos termos termos da Sequencia de Fibonacci deseja exibir » '))

# A sequencia de Fibonacci implica  os dois números 0 e 1 inicial. Por isso posso criar duas variáveis para cada um
# deles. No caso as duas variáveis foram n1 e n2. Sabendo que a sequencia consiste na construção de um terceiro termo
# baseado na soma dos dois anteriores e assim sucessivamente, aplica-se assim:

n1 = 0
n2 = 1
print('{} - {} - '.format(n1, n2), end='')

cont = 3  # O contador não começou com 1 por que já defini n1 e n2, por isso o valor que quero é n3, para isso coloco o
# contador para iniciar com 3.


while cont <= n:
    n3 = n1 + n2  # Essa é a fórmula da Sequencia de Fibonacci, uma vez que já determinei o 1º e o 2º termo. Dentro do
    # laço while encontrei o valor de n3, agora basta alternar os valores através desta fórmula para obter outros
    # valores
    print(n3, end=' - ')
    n1 = n2  # Essa técnica permite alternar os valores mantendo uma só fórmula. Nesse caso, o valor de n1 passa a ser
    # n2 e o valor de n2 passa a ter o valor de n3 como no exemplo abaixo.
    n2 = n3
    cont += 1
print('Fim da exibição dos {} termos'.format(n))

# Usando FOR

n = int(input('Digite quantos algarismos deseja para mostrar a sequência de Fibonacci » '))

n1 = 1
n2 = 1
n3 = 0

lista = [0, 1, 1]

for c in range(0, n-3):
    n3 = n1 + n2
    n1 = n3
    n2 = (n3 - n2)
    lista.append(n3)

print(lista)

'''
Testando...
Sequencia de Fibonacci com Função

def proximoFibonacci(a, b):
    soma = a + b
    a = b
    b = soma
    return soma


n1 = 0
print(n1)
n2 = 1
print(n2)

for c in range(3, 10):
    n3 = proximoFibonacci(n1, n2)
    print(n3)
'''
