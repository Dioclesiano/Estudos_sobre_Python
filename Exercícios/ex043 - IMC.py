# Desenvolva uma lógica que leia o peso e a altura de uma pessoa. Calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo:
# * Abaixo de 18.5: Abaixo do Peso
# * Entre 18.50 e 25: Peso ideal
# * 25 até 30: Sobrepeso
# * 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida.

p = float(input('Digite seu peso » '))
a = float(input('Digite sua altura » '))

imc = p/a**2
print('Seu IMC é {:.2f}.'.format(imc), end=' ')
if imc <= 18.50:
    print('Você está abaixo do peso ideal.')
elif 18.50 < imc <= 25:
    print('Você está no peso ideal.')
elif 25 < imc <= 30:
    print('Você está no sobrepeso.')
elif 30 < imc <= 40:
    print('Você está na Obesidade.')
else:
    print('Você está na obesidade mórbida.')
