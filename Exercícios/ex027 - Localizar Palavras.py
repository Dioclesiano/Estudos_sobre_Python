# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
# nome separadamente.
# ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = str(input('Digite seu nome completo: ')).lower().strip()
dividido = nome.split()
print('O seu primeiro nome é » {} «'.format(dividido[0]))
print('O seu último nome é » {} «'.format(dividido[len(dividido)-1]))
