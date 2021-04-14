# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
# o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o flag - não vale como dado).


cont = cancelar = soma = 0  # Para economizar espaço, posso iguar todas essas variáveis, uma vez que todas sejam iguais
# ao mesmo valor.

cancelar = int(input('Digite um número para somar ou [999] para sair » '))

while cancelar != 999:
    soma += cancelar
    cont += 1
    cancelar = int(input('Digite um número para somar ou [999] para sair » '))

print('{:~^60}'.format(' RESULTADO '))
print('A soma de todos os {} números digitados é »» {} ««'.format(cont, soma))
print('{:~^60}'.format(''))
