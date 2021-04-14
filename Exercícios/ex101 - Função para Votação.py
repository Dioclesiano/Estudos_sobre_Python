'''
Crie um programa que tenha uma função chamada VOTO() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.


def voto(ano):
    from datetime import date  #Importando uma biblioteca para uma DEF, economiza memória.
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f'Com {idade} anos » NÃO VOTA!'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos » VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos » VOTO OBRIGATÓRIO!'


# Programa Principal
num = int(input('Digite o seu ano de nascimento » '))
print()
print(voto(num))

'''
from ex101.Voto import voto

ano = int(input('Digite o seu ano de nascimento » '))
voto(ano)
