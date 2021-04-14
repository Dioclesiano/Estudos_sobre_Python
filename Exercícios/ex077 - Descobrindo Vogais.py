'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

n = ('Farmacia', 'Campo', 'Tenis', 'Mouse', 'Casa',
     'Teclado', 'Computador', 'Notebook', 'Cadeiras',
     'Tomadas', 'Mesa', 'Talheres', 'Caneta', 'Caderno')

for c in n:
    print('\n{:=^40}'.format(''))
    print(f'\033[31mA(s) vogal(is) da palavra \033[7;31m{c}\033[m é \n\033[m', end=' ')


    for letra in c:
        if letra in 'aeiou':
            print(letra, end=' ')

'''
# Fiz esse esboço para entender um pouco como os laços funcionam. Nesse caso eu usei o enumerate para e outro FOR
# Enquanto K faz a contagem e exibição do valores dentro da tupla, o V indica o tamanho da palavra, através do LEN
# combinado len(v), e em posse dessas informações poderei criar outro Laço para fazer o que eu quero.

for k, v in enumerate(n):
    for c in range(0, len(v)):
        print(f'{n[k]} tem {len(v)} letras.')

# Com esse FOR abaixo combinado com esses comandos, consegui unir todas as letras, facilitando a manipulação delas.
# A exibição das letras é feito uma letra embaixo da outro, se eu quiser que uma letra fique ao lado da outra
# terei que usar o comando end=''.
# No lugar de print(n[k][c])  basta mudar para  print(n[k][c], end='')

for k, v in enumerate(n):
    for c in range(0, len(v)):
        print(n[k][c], end='')

# Este FOR resume de forma limpa os de cima. São todos iguais. Este FOR não tem nenhuma formatação. Ele localiza
# uma parte de uma parte da lista.
# Aqui eu coloque a escrita: Palavra e Letra, para facilitar o entendimento do que vou buscar na lista.

for palavra in n:
    for letra in palavra:
        print(letra)
'''
