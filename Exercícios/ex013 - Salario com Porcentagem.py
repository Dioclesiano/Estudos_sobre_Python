# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

print('Devido o grande crescimento da empresa, todos os funcionários receberão participação de lucro.')
n = float(input('Digite o valor do seu salário: '))

print('Para o próximo mês, você receberá {:.2f} correspondente a 15% de aumento '
      'no seu salário. \nObrigado por seu trabalho e esforço.'.format(n+(n*15/100)))
