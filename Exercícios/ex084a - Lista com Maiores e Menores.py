'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

'''
# Lista de todas as listas
listatotal = []

# Listas de nome e peso separados
listanome = []
listapeso = []

# contador
cont = 1

# Definição da pessoa com menor peso
nomemenor = ''
listamenorpeso = []  # Criação da Lista do menor peso
listamenornome = []  # Criação da Lista da pessoa menos pesada

# Definição da pessoa com maior peso
nomemaior = ''
listamaiorpeso = []  # Criação da Lista do maior peso
listamaiornome = []  # Criação da Lista da pessoa mais pesada

menor = 0
maior = 0

# Estrutura formada para sair do programa quando o cliente digitar 'n' ou 'Não'
while True:
    nome = str(input('Digite o seu nome » ')) # Solicitação do nome do usuário
    listanome.append(nome)                    # Nome adicionado em uma lista

    peso = int(input('Digite o seu peso » ')) # Solicitação do peso do usuário
    listapeso.append(peso)                    # Peso adicionado em uma lista

# Condição para definir o maior e o menor peso respectivo ao nome
    if cont == 1:
        menor = peso
        nomemenor = nome

        maior = peso
        nomemaior = nome
    else:
        if peso < menor:
            menor = peso
            listamenorpeso.append(peso) # Menor peso adicionado na listamenorpeso

            nomemenor = nome
            listamenornome.append(nome) # Nome da pessoa de peso menor adicionado a listamenornome


        elif peso > maior:
            maior = peso
            listamaiorpeso.append(maior)  # Maior peso adicionado na listamaiorpeso

            nomemaior = nome
            listamaiornome.append(nomemaior)  # Nome da pessoa de peso maior adicionado a listamaiornome

    stop = str(input('Deseja fazer um novo cadastro [S/N] » ')).strip().lower()
    if stop == 's' or stop == 'sim':
        pass
    elif stop == 'n' or stop == 'nao' or stop == 'não':
        break

    cont += 1

print()

print(f'O total de cadastros foram de {cont} pessoas')
listatotal.append(listanome)
listatotal.append(listapeso)
print(listatotal)
print()
print(f'O maior peso é de {nomemaior} com {maior}kg')
print(f'O menor peso é de {nomemenor} com {menor}kg')
print()
print('Informação em Listas: ')
print(f'Pessoa(s) mais pesada » {listamaiornome} « com {listamaiorpeso}kg')
print(f'Pessoa(s) mais leve » {listamenornome} « com {listamenorpeso}kg')
'''
nomePeso = []

nMenor = nMaior = ''
menor = maior = cont = 0
stop = ' '
while stop not in 'N':
    nome = str(input('Digite o seu nome » ')).upper()
    peso = float(input('Digite o seu Peso » '))
    nomePeso.append(nome)
    nomePeso.append(peso)

    if cont == 0:
        menor = maior = peso
        nMenor = nMaior = nome
    else:
        if peso < menor:
            menor = peso
            nMenor = nome
        if peso > maior:
            maior = peso
            nMaior = nome

    stop = str(input('Deseja continuar S[Sim] ou N[Não] » ')).upper()

    cont += 1

print()
print(f'Detectamos {cont} registros.')
print(f'******* Nome{"":<5} Peso')
for k, v in enumerate(nomePeso):
    if k % 2 == 0:
        print(f'O peso de {v} é', end=' ')
    else:
        print(f'{v:0.2f} Kg'.replace(".", ","), end=' ')
        print()
print()
print(f'O(A) sr(sra) {nMenor} foi registrado com o menor peso {menor} kg.')
print(f'O(A) sr(sra) {nMaior} foi registrado com o maior peso {maior} kg.')
