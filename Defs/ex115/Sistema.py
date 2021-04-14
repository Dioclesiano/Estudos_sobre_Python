'''
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastar uma nova pessoa e listar todas as pessoas cadastradas.
'''
#  Criando o Interface
from ex115.Interface import *
from ex115.Arquivo import *

arquivo = 'Cadastros'
'''
# Esse é o método mais completo de localizar o Arquivo
if arquivoExiste(arquivo):
    print('Arquivo encontrado com sucesso.')
else:
    print('Arquivo não encontrado.')
    criarArquivo(arquivo)
'''

# Esse método tem a mesma função do acima, porém mais resumido, pois no acima o que é útil é o ELSE, portanto eu posso
# iniciar um IF seguido do not. Lembrando que o if é verdadeiro e o else Falso.
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    titulo('CADASTRAMENTO')
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Programa'])

    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arquivo)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        titulo('NOVO CADASTR0')
        nome = str(input('Digite seu Nome » '))
        idade = leiaInt('Digite a sua Idade » ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        # Opção de sair do Sistema
        print(f'Saindo do Programa')
        break
    else:
        # Digitou opção errada no Menu
        print('ERRO! Comando Inválido. Tente Novamente')
