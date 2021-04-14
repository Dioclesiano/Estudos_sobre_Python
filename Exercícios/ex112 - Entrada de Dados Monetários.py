'''
107 - Crie um módulo chamado MOEDA.PY que tenha as funções incorporadas AUMENTAR(), DIMINUIR().
Faça também um programa que importe esse módulo e use algumas dessas funções.

108 - Adapte o código do DESAFIO 107, criando uma função adicional chamada REAL() que consiga mostrar os valores como um
valor monetário formatado.

109 - Modifique as funções que foram criadas no DESAFIO 107 para que elas aceitem um parâmetro a mais, informando se o
valor retornado por elas vai ser ou não formatado pela função MOEDA(), desenvolvida no DESAFIO 108.

10 - Adicione ao módulo MOEDA.PY criado nos desafios anteriores, uma função chamada RESUMO(), que mostre na tela algumas
informações geradas pelas funções que já temos no módulo criado até aqui.

11 - Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados MOEDA e DADO. Transfira todas as
funções utilizadas nos DESAFIOS 107, 108 E 109 para o primeiro pacote e mantenha tudo funcionando.

===> Dentro do pacote utilidadeCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas
valores que sejam monetários.
'''
from ex111.utilidadesCeV.funcao import resumo
from ex112.utilidadesCeV.dado import leiaDinheiro

n = leiaDinheiro('Digite o valor do Produto » ')
credito = int(input('Digite a taxa de juros para parcelamento » '))
debito = int(input('Digite a taxa de juros para desconto » '))

while True:
    conversao = str(input('Deseja converter o resultado para formato Moeda? ')).upper()[0].strip()

    if conversao == 'S':
        brasao = str(input('Digite o brasao de sua moeda » ')).upper()
        resumo(n, credito, debito, brasao, True)
        break

    elif conversao == 'N':
        resumo(n, credito, debito, '')
        break

    else:
        print(f'\033[7;31m Entrada Inválida!!! \033[m  Digite somente \033[36m S[SIM] \033[m ou \033[31m N[NÃO] \033[m ')
