'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.


lista = []

for c in range(0,5):
    n = int(input('Digite um valor » '))

    if c == 0:
        lista.append(n) # C = 0 significa o 1º valor. Portanto o primeiro valor digitado ficará na primeira posição.
    elif n > lista[-1]: # Foi usado len(lista)-1, para indicar o último ítem da lista. Deve-se ter em mente que quando
                        # uso a função 'len(lista)' é para saber a quantidade de ítens da lista. Enquanto 'lista[-1]'
                        # é para mostrar o valor ou dado que está na última posição dalista.

        lista.append(n) # Esse comando irá adicionar o número e, através da lógica criada no ELIF, este número será
                        # armazenado depois do último número.
    else:
        posicao = 0
        while posicao < len(lista):  # Essa função while especifica que o laço ira acontecer
                                     # enquanto o contador 'posicao' indicar um valor menor
                                     # que a quantidade de ítens da lista, ou seja, sendo que a
                                     # lista tem 5 ítens, enquanto o contador for menor que 5
                                     # o programa funcionará, e parará quando for igual a 5.
            if n <= lista[posição]
                lista.insert(posicao, n) # Este comando irá adicionar o número digitado pelo cliente (n)
                                         # na posição indicada pelo contador 'posicao'
                break
            posicao += 1
'''

        # Abaixo toda estrutura organizada

lista = []

for c in range(1, 6):
    n = int(input('Digite um valor » '))

    if c == 1 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        indice = 0
        while indice < len(lista):
            if n <= lista[indice]:
                lista.insert(indice, n)
                print(f'Adicionado na posição {indice+1} da lista...')
                break

            indice += 1
print()
print(' * '*20)
print(f'Os valores digitados em ordem foram {lista}')
print(' * '*20)

'''
Exemplo de Organização com Lógica

num = [10, 5, 6, 3, 8, 1, 0, 9, 7, 2, 4]

for i in range(0, len(num)):
    for j in range(0, len(num)):
        if num[i] < num[j]:
            aux = num[i]
            num[i] = num[j]
            num[j] = aux
print(num)
'''
