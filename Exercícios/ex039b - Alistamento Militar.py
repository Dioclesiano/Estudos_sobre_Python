from datetime import date

atual = date.today().year
nasc = int(input('Digite o ano do seu nascimento: '))
idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade == 18:
    print('Você tem que se alistar \033[7;31mIMEDIATAMENTE\033[m.')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o seu alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
else:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
