# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from time import sleep

ano = int(input('Que ano você deseja analisar » '))
print('Analisando...')
sleep(1)

if ano % 4 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO'.format(ano))

'''
PARA DEFINIR SE O ANO É BISSEXTO OU NÃO, BASTA SEGUIR ESSAS TRÊS REGRAS

* Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
* Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
* Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o 
resto igual a zero.
'''
