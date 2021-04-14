# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60,00 por dia e R$0,15 por km rodado.

n1 = float(input('Digite a quantidade de KM percorrido: '))
n2 = int(input('Digite a quantidade de dias que esteve com o carro alugado: '))

print('O total a pagar é: {:.2f}'.format(n2*60 + 0.15*n1))
