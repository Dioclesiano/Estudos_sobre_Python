# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

from datetime import date

ano = int(input('Digite o ano de nascimento » '))
atual = date.today().year
n = atual - ano

print('O atleta tem {} anos e é: '.format(n))

if n <= 9:
    print('MIRIM')
elif 9 < n <= 14:
    print('INFANTIL')
elif 14 < n <= 19:
    print('JUNIOR')
elif 19 < n <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
