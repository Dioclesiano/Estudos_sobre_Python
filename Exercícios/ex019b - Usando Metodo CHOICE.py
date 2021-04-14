from random import choice

n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')

lista = [n1, n2, n3, n4]

print('O ganhador é »» {}'.format(choice(lista)))

'''
Outra maneira simplificada de resolver

lista = []
for c in range(0, 4):
    lista.append(input('Digite o nome do Aluno » '))

print(f'O aluno sorteado foi {choice(lista)}')
'''
# É um comando que escolhe uma opção
