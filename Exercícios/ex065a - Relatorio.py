# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O
# programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

continuar = ''
cont = soma = maior = menor = 0

while continuar in 's sim':
    n = int(input('Digite números inteiros para serem somados » '))

    if cont == 0:
        menor = maior = n  # Esse comando é o mesmo         menor = n   e   maior = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n

    continuar = str(input('Deseja continuar? Digite [S] para Sim ou [N] para Não » ')).strip().lower()

    soma += n
    cont += 1

print()
print('{:~^50}'.format(' RELATÓRIO '))
print('Quantidade de Termos Digitados {}'.format(cont))
print('A soma de todos os valores digitados é {}'.format(soma))
print('A média de todos os valores digitados é {:.2f}'.format(soma/cont))
print('O maior número digitado foi {}'.format(maior))
print('o menor número digitado foi {}'.format(menor))
print('{:~^50}'.format(' FIM '))
