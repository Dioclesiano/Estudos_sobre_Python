# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule aumento de 10%.
# Para salários inferiores ou iguais a R$1.250,00, calcule um aumento de 15%.

n = float(input('Digite o valor do salário do colaborador(a) » '))

if n <= 1250:
    s = n + (n * 15) / 100
    print('O novo salário do colaborador(a) é de R$\033[36m{:.2f}\033[m'.format(s))

else:
    s = n + (n * 10) / 100
    print('O novo salário do colaborador(a) é de R$\033[31m{:.2f}\033[m'.format(s))
