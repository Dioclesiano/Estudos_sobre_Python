#  Crie um programa que leia o nome completo de uma pessoa e mostre:
#  * O nome com todas as letras maiúsculas
#  * O nome com todas as letras minúsculas
#  * Quantas letras ao topo (sem considerar espaços).
#  * Quantas letras tem o primeiro nome.


n = input('Digite seu nome completo [sem números] » ').strip()

print('Seu nome com todas as letras maiúsculas » ', n.upper())
print('Seu nome com todas as letras minúscuwlas » ', n.lower())
print('Seu nome possui » {} « letras totais, incluindo espaços.'.format(len(n)))
print('Seu nome possui » {} « espaço (s) e '
      '» {} « letras, sem considerar espaços.'.format(n.count(' '), len(n) - n.count(' ')))

print('Seu primeiro nome tem » {} « letras'.format(n.find(' ')))
#  Repare que usei a função .find(' ') com um espaço dentro das aspas simples, porque esse comando localiza o primeiro
#  o primeiro espaço antes da frase e o primeiro espaço após a primeira palavra. Essa lógica seleciona
#  o primeiro nome. Por isso, neste caso, o programa conseguiu contar quantas letras existe no primeiro nome.
#  Mas também posso separar por listas usando a função .split() Eu só preciso criar uma variável que será: separa

separa = n.split()

#  Se eu mandar imprimir a variável separa, será mostrado o nome que o usuário digitar separado palavra por palavra
#  entre colchete. Aí basta usar eu determinar a palavra que eu quero trabalhar especificando sua posição entre
#  colchetes e depois usar a função len() para contar as letras existente dentro da lista selecionada entre colchete
#  lista que eu deseje mostrar.


print('Seu primeiro nome é » {} « e tem » {} « letras'.format(separa[0], len(separa[0])))

#  A função FIND faz a contagem dos espeços existente de e até onde definir.
#  Ex.: Se eu digitar o nome DIOCLESIANO e fizer um find('a'), será reportado o valor 8, pois a contagem iniciará em D
#  e finalizará em A, totalizando 8 espaços ou dígitos.


#  Outros exemplos

lista = n.split()

for c in range(0, len(lista)):
    print(lista[c])

print()
print('Outros Exemplos')

n = 'Dioclesiano Wellerson Rodrigues da Paz'.replace(' ', '')  # Quando eu uso o método replace dessa forma, eu elimino
#  todos os espaços, pois estou mandodo trocar os espaços por sem espaços.


separaPalavras = n.split()  # Usei o comando que separa palavras em uma frase

contadorTotal = len(n)  # Usei o comando que faz a contagem de todos os caracteres

contadorEspacos = n.count(' ')  # Este comando faz a contagem do que for estabelecido entre parênteses:
#  Neste caso a contagem estabelecida foi espaços e será retornado quantos espaços existem na frase n.

contatorLetras = (len(n) - n.count(' '))  # Neste comando eu fiz uma conta subtraindo o total de strings subtraído
#  pelos espaços. Será retornado apenas a quantidade de letras nesta variável.
#  O método STRIP() também elimina espaços, mas somente os espaços do início e fim, aqueles no meio da frase não.


print(separaPalavras)
print(contadorTotal)
print(contadorEspacos)
print(contatorLetras)
print('-'.join(n))  # Este comando junta todas as letras a um símbolo ou o que eu definir entre aspas
print('-'.join(n.split()))  # Este junta as palavras, pois como usei o comando de fatiamento SPLIT(), entao o JOIN()
#  une as palavras colocando entre os espaços o símbolo que for determinado entre aspas.


n1 = int(input('Digite um número que representa a posição da letra a ser exibida » '))

print(n[n1 - 1])
#  Neste exemplo, pedi entrada de um número inteiro para exibir a letra que está na posição indicada por este número.
#  para isto, além de eliminar todos os espaços com o método REPLACE(), mostrei a string n subtraindo 1, pois a
#  contagem no python é diferente, e para isto tem-se que reduzir 1 valor.

n2 = str(input('Digite a letra para saber a posição que está na frase » ')).lower()
print(n.lower().find(n2) + 1)
#  Neste exemplo, pedi uma entrada de string para exibir a posição que esta string ocupa na frase. Para isto, fiz com
#  que a entrada e a exibição(print) fossem colocadas em minúsculas e usando o método FIND() somando 1, pôde exibir a
#  letra correta. O fato de ter que somar 1 no FIND() é o mesmo motivo de subtrair 1 no LEN().
