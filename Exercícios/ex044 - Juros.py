# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
# de pagamento:
# À vista dinheiro/Cheque: 10% de desconto
# À vista Cartão: 5% de desconto
# Em até 2x no cartão: Preço normal
# Em até 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' Lojas Diow '))

n = float(input('Digite o valor do produto » '))

print('Digite [1] para pagamento à vista (Dinheiro/Cheque)')
print('Digite [2] para pagamento à vista (Cartão de Débito)')
print('Digite [3] para pagamento em até 2x sem juros (Cartão de Crédito)')
print('Digite [4] para pagamento acima de 3x com juros (Cartão de Crédito)')

paga = str(input('Selecione a opção de [1 a 4]: '))

if paga == '1':
    s = n - (n * 10)/100
    print('Sua compra tem 10% de desconto. O novo valor a pagar é R${:.2f}'.format(s))
elif paga == '2':
    s = n - (n * 5)/100
    print('Sua compra tem 5% de desconto. O novo valor a pagar é R${:.2f}'.format(s))
elif paga == '3':
    p = int(input('Digite a quantidade de parcelas:'))
    s = n / p
    print('O valor total a pagar é R${:.2f} dividido em {} parcela(s) de R${:.2f}'.format(n, p, s))
elif paga == '4':
    p = int(input('Digite a quantidade de parcelas:'))
    j = n + (n * 20) / 100
    s = j / p
    print('O Valor a pagar é R${:.2f} dividido em {} parcelas de R${:.2f}'.format(j, p, s))
else:
    print('O número digitado não corresponde ao número informado.')
