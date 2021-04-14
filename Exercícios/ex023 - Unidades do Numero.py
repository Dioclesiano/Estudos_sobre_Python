#  Faça um programa que leia um número de 0 a 9999 e mostre
#  na tela cada um dos dígitos separados.
#  ex.: Digite um número » 1834
#  unidade: 4
#  dezena: 3
#  centena: 8
#  milhar: 1

#  Esse seria o modo mais simples de resolver este exercício, mas precisaria aplicar estrutura de repetição

#  n = int(input('Digite um número inteiro de 0 a 9999 » '))

#  print('Unidade » {}'.format(n[3]))
#  print('Dezena » {} '.format(n[2]))
#  print('Centena » {}'.format(n[1]))
#  print('Milhar » {} '.format(n[0]))

#  porém este exercício será resolvido com matemática

#  n = int(input('Digite um número inteiro'))

'''
u = n//1 % 10
d = n//10 % 10
c = n//100 % 10
m = n//1000 % 10
print('Unidade » ', u)
print('Dezena » ', d)
print('Centena » ', c)
print('Milhar » ', m)
'''

#  Resolvendo o Exercício com comandos mais evoluído

soma = 1
while True:
    try:
        n = int(input('Digite um número inteiro [Até 6 dígitos] » '))

        lista = ['Unidade',
                 'Dezena',
                 'Centena',
                 'Unidade de Milhar',
                 'Dezena de Milhar',
                 'Centena de Milhar']

        tamanho = len(str(n))

        if tamanho <= 6:
            for c in range(0, tamanho):
                calculo = n // soma % 10
                tamanho -= 1
                soma *= 10
                print(f'O {tamanho+1}° número digitado foi {calculo} e corresponde a "{lista[c]}"')
            break
        else:
            print('\033[7;31m  ERRO!  \033[m \033[31m O número digitado excede os caracteres disponíveis. \033[m')
    except ValueError:
        print('\033[7;31m  ERRO!  \033[m \033[31m Digite apenas números. \033[m')
    except TypeError:
        print('\033[7;31m  ERRO!  \033[m \033[31m Digite apenas números. \033[m')

'''
* No exercício acima eu coloquei os códigos dentro de um while para que, quando a digitação fosse feita fora do que foi 
pedido ao usuário, ele pudesse receber uma informação de erro da minha programação, e não do sistema Pycharm.
* Usei o Try e Except para auxiliar na correçao dos erros.
* Solicitei a digitação do número e logo em seguida criei uma tupla com os dados que eu iria exibir para atender a
apenas seis dígitos.
* Criei também uma variável 'tamanho' que recebe a quantidade de dígitos feita com o método LEN. Essa variável 'tamanho'
foi muito útil para limitar o FOR.
* Se os dígitos forem menores que 6, a variável 'calculo' irá receber o resultado da divisão inteira do número que o 
cliente digitou com a quantidade de unidades, dezenas,..., valores estes que serão múltiplos de 10 através da variável
'soma' que armazena o resultado e aproveita o loop do for para multiplicar novamente o resultado por 10. Então o 
resultado da divisão de 'n' pela 'soma' será submetida a outra divisão por 10 para obter o resto da divisão. Este fato
repetira o tanto devezes que a variável 'tamanho' definir. O resultado na variável 'calculo', entregará corretamente
a identificação de cada dígito feito.
* No print que mostra o resultado, foram colocados 'tamanho', 'calculo' e 'lista. No tamanho eu somei 1 pois a contagem
inicia com zero. Como preciso indicar "primeiro", então somei um. O 'calculo' mostra o correto resultado. E a lista[c]
exibe o resultado do fatiamento das partes correspondente a contagem em c.
* O else e except foram colocados para eliminar erros de travamento, de modo que estes erros são traduzidos por 
mensagens ao usuário e este possa informar os valores corretamente. 
'''