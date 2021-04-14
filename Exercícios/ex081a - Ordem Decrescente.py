'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = list()

tem = 0
cont = 1
while True:
    n = int(input('Digite um valor » '))

# Comando para identificar o número 5 na lista
    if n == 5:
        lista.append(n)
        tem += 1
    else:
        lista.append(n)


# Comando para sair do Laço através do comando do Cliente.
    stop = ' '
    while stop not in 'sc':
        stop = input('Digite [C] para continuar ou [S] para sair » ').strip().lower()

    if stop == 's':
        break

# Contador das repetições totais
    cont += 1


print()
print('*'*90)
print(f'Foram digitados {cont} números')
print(f'Os número digitados foram {lista}')
print('Os números digitados em ordem crescente foram ',sorted(lista))

lista.sort(reverse=True)
print(f'Os números digitados em ordem decrescente foram {lista} ')



# Comando para mostrar quantas vezes o número 5 aparece e se não aparece na lista.
if tem > 0:
    print(f'O número 5 aparece na lista {tem} vez(es)')
else:
    print('O número 5 não aparece na lista')
print('*'*90)
