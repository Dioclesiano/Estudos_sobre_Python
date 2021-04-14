#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

n = int(input('Digite um número inteiro: '))

print('O antecessor do número digitado é {}'.format(n-1), end=' ')
print('e o sucessor do número digitado é {}'.format(n+1))
