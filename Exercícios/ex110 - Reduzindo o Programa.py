'''
107 - Crie um módulo chamado MOEDA.PY que tenha as funções incorporadas AUMENTAR(), DIMINUIR().
Faça também um programa que importe esse módulo e use algumas dessas funções.

108 - Adapte o código do DESAFIO 107, criando uma função adicional chamada REAL() que consiga mostrar os valores como um
valor monetário formatado.

109 - Modifique as funções que foram criadas no DESAFIO 107 para que elas aceitem um parâmetro a mais, informando se o valor
retornado por elas vai ser ou não formatado pela função MOEDA(), desenvolvida no DESAFIO 108.

110 - Adicione ao módulo MOEDA.PY criado nos desafios anteriores, uma função chamada RESUMO(), que mostre na tela algumas
informações geradas pelas funções que já temos no módulo criado até aqui.

===> obs.: De acordo com os conhecimentos adquiridos ao longos dessas atividades com Módulo, tomei a liberdade de direcionar
     o exercício para a maneira que eu quiz.
'''
from ex110 import Def

n = float(input('Digite o valor do Produto » '))
aumento = int(input('Digite o percentual de Juros » '))
desconto = int(input('Digite o percentual de Desconto » '))

while True:
    moeda = str(input('Deseja o resultado convertido em Moeda? ')).upper()
    if moeda == 'S' or moeda == 'SIM':
        moeda = True
        Def.resumo(n, aumento, desconto, moeda)
        break

    elif moeda == 'N' or moeda == 'NÃO' or moeda == 'NAO':
        moeda = False
        Def.resumo(n, aumento, desconto, moeda)
        break

    else:
        print(f'\033[7;31mComando Inválido!\033[m \033[31mDigite somente [S] para Converter ou [N] para não Converter\033[m')
