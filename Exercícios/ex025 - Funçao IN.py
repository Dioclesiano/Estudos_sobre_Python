# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.


nome = str(input('Digite seu nome completo: ')).strip().lower()

print('Analisando o nome...')
print('O nome digitado tem "SILVA" ? » {} «'.format('silva' in nome.lower()))
