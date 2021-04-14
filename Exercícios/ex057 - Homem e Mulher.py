# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite seu sexo [M/F] » ')).strip().upper()

while sexo not in 'MASCULINOFEMININO':
    sexo = str(input('Informação incorreta, digite novamente » ')).strip().upper()

if sexo == 'M':
    sexo = 'Masculino'
elif sexo == 'F':
    sexo = 'Feminino'

print('Foi registrado sexo {} com sucesso.'.format(sexo))




