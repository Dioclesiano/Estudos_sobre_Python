# Crie um programa que leia a idade e o sexo
# de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer
# ou não continuar. No final, mostre:
# A - Quantas pessoas tem mais de 18 anos.
# B - Quantos homens foram cadastrados.
# C - Quantas mulheres tem menos de 20 anos

'''
tot18 = tothomens = tot20 = 0

while True:
    idade = int(input('Digite sua idade » '))


# Feito a condição para receber somente 'M' ou 'F', se o usuário digitar outro dado que não for essas letras
# o while fará com que entre em loop infinito com a mesma pergunta, até atender uma das letras.
    sexo = ' ' # Sempre que usar o while 'not in' te que declarar a varíavel com espaço entre as aspas.
    while sexo not in 'mf':
        sexo = str(input('Digite seu sexo [M/F] » ')).strip().lower()[0]


    if idade >= 18:
        tot18 += 1

    if sexo == 'm':
        tothomens += 1

    if idade <= 20 and sexo == 'f':
        tot20 += 1

# Defini a condição para sair do programa usando duas letras: [S] para continuar ou [N] para sair
# No while abaixo, quando o usuário digitar 'N', atenderá a condição do primeiro While.
    parar = ' '
    while parar not in 'sn':
        parar = str(input('Digite [N] para sair ou [S] para continuar cadastrando')).strip().lower()[0]

    if parar == 'n':
        break

print()
print('{:=^80}'.format(''))
print(f'Encontramos >> {tot18} << pessoas acima de 18 anos.')
print(f'Encontramos >> {tothomens} << homens cadastrados.')
print(f'Encontramos >> {tot20} << mulheres castradas com idade inferior a 20 anos.')
print('{:=^80}'.format(''))
'''
from ex069.Defs import formatar

cont18 = contMasculino = contFeminino = 0
while True:
    nome = str(input('Digite o seu nome » '))
    idade = int(input('Digite a sua idade » '))
    if idade >= 18:
        cont18 += 1

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite M[Masculino] ou F[Feminino] » ')).upper()[0]
        if sexo == 'M':
            contMasculino += 1
        else:
            if sexo == 'F' and idade <= 20:
                contFeminino += 1

    # Esse comando é para perguntar se o usuário deseja continuar
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N] » ')).upper()[0]
    if continuar in 'N':
        break

formatar(f'    {cont18} pessoas maiores de 18 anos, sendo {contMasculino} Homens e {contFeminino} mulheres menores '
         f'de 20 anos')
