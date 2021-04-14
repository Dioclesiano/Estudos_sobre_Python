# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O
# programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

continuar = ''
cont = 0
soma = 0
menor = 0
maior = 0
while continuar in 's sim':
    n = int(input('Digite um número inteiro para somar » '))

    if cont == 0:
        menor = n
        maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    soma += n
    cont += 1

    continuar = str(input('Deseja continuar? [S]Sim ou [N]Não » ')).strip().lower()


print('Média {}'.format(soma/cont))
print('Maior {} e menor {}'.format(maior, menor))
