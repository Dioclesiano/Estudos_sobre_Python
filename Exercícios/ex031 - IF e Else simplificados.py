# Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem,
# cobrando R$ 0,50 por Km para viagens de até 200km e R$ 0,45 para viagens mais longas.

n = float(input('Digite a distância que pretende percorrer: '))
'''
if n <= 200:
    passagem = n*0.50
    print('O valor de sua passagem é » R$ {:.2f} «'.format(passagem))
else:
    passagem = n*0.45
    print('O valor de sua passagem é » R$ {:.2f} «'.format(passagem))
'''

# O código acima é a maneira estruturada de fazer o programa. A maneira simplificada é assim:

p = n * 0.5 if n < 200 else n * 0.45

print('O valor da passagem para {:.0f}km é de R${:.2f}'.format(n, p))
