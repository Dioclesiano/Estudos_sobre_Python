# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

nome_velho = ''
somaidade = 0
maioridadehomem = 0
mulher20 = 0
mediaidade = 0
cont = 0
for c in range(1, 5):
    print('{:»^120}'.format(' Analisador de Dados '))
    nome = str(input('Digite o seu nome: ')).strip().lower()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite o genero [M/F]: ')).strip().lower()

    somaidade += idade

    if c == 1 and sexo == 'm':
        maioridadehomem = idade
        nome_velho = nome

    if sexo in 'm' and idade > maioridadehomem:
        maioridadehomem = idade
        nome_velho = nome

    if sexo in 'f' and idade < 20:
        mulher20 += 1

    cont += 1

mediaidade = somaidade / cont

print('A média da idade dos integrantes do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho é o sr(sra) {} com {} anos de idade.'.format(nome_velho, maioridadehomem))
print('Encontramos {} mulheres com idade abaixo de 20 anos.'.format(mulher20))
