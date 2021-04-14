# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag.)

cont = soma = 0

while True:
    n = int(input('Digite um número » '))
    if n == 999:
        print()
        print('{:~^40}'.format(''))
        print('Programa finalizado com Sucesso.')
        print('{:~^40}'.format(''))
        break
    soma += n
    cont += 1
print()
print(f'O total de números digitados foram {cont} e a soma entre eles é >> {soma} <<')
