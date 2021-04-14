# Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''
dicionario = {}

dicionario['nome'] = str(input('Digite o seu nome » '))
dicionario['matemática'] = float(input('Digite sua nota de Matemática » '))
dicionario['português'] = float(input('Digite sua nota de Português » '))

soma = (dicionario['matemática'] + dicionario['português']) / 2

if 7 <= soma <= 10:
    print(f'Parabéns! ', end=' ')

elif 4 <= soma <= 6:
    print('Recuperação', end=' ')

elif 0 <= soma <= 3:
    print('\033[31mReprovado\033[m', end=' ')

else:
    print("O dado informado não existe. ")

for k, v in dicionario.items():
    print(f'{k} corresponde a {v}', end=' ')
    print()

print(f'A média do aluno(a) {dicionario["nome"]} é {soma:0.2f}')
'''
boletim = {}

boletim['Nome'] = str(input('Digite o seu nome » '))
media = 11
while media >= 10:
    media = float(input('Digite a média escolar » '))

if media <= 4:
    boletim['Média'] = media
    boletim['Situaçao'] = 'Reprovado'
elif 5 <= media <= 6:
    boletim['Média'] = media
    boletim['Situaçao'] = 'Recuperação'
elif media >= 7:
    boletim['Média'] = media
    boletim['Situaçao'] = 'Aprovado'

for k, v in boletim.items():
    print(f'O {k} equivale a {v}.')