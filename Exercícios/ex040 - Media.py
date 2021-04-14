# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de
# acordo com a média atingida:
# * Média abaixo de 5.0: REPROVADO
# * Média entre 5.0 e 6.9: RECUPERAÇÃO
# * Média 7.0 ou superior: APROVADO.

n1 = float(input('Digite sua primeira nota [0 a 10]: '))
n2 = float(input('Digite sua seguanda nota [0 a 10]: '))

m = (n1 + n2)/2

if m < 5:
    print('Sua média foi ', m)
    print('\033[33m*\033[m'*12)
    print('\033[7;31m!REPROVADO!\033[m')
    print('\033[33m*\033[m' * 12)

elif 5 <= m < 6.9:
    print('Sua média foi', m)
    print('\033[32m=\033[m'*12)
    print('\033[31mRECUPERAÇÃO\033[m')
    print('\033[32m=\033[m' * 12)
else:
    print('Sua média foi ', m)
    print('\033[32m»\033[m'*10)
    print('\033[31mAPROVADO\033[m')
    print('\033[32m«\033[m'*10)
