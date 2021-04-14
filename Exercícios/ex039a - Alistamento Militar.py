# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# * Se ele ainda vai se alistar ao serviço militar.
# * Se é a hora de se alistar.
# * Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

n = int(input('Digite o ano de nascimento » '))

if n > 2002:
    print('Ainda não chegou o período de Alistamento. Faltam {} anos.'.format(n-2002))
elif n < 2002:
    print('Devia ter feito o alistamento à {} anos atrás.'.format(2002-n))
else:
    print('É hora do seu alistamento militar.')
