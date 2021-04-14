'''
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastar uma nova pessoa e listar todas as pessoas cadastradas.
'''
#  Criando o Interface
from ex115.Interface import *

while True:
    titulo('CADASTROS')
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Programa'])

    if resposta == 1:
        print(f'A opção selecionada foi "Ver Pessoas Cadastradas".')
    elif resposta == 2:
        print(f'A opção selecionada foi "Cadastrar Nova Pessoa".')
    elif resposta == 3:
        print(f'Saindo do Programa')
        break
    else:
        print('ERRO! Comando Inválido. Tente Novamente')
