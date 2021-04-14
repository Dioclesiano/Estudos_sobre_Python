from ex115.Interface import *


def arquivoExiste(arquivo):
    try:
        a = open(arquivo, 'rt')  # O rt indica 'read' e 'text', significa um arquivo de texto em modo leitura
        a.close()  # Open e Close são comandos de abrir e fechar o arquivo respectivamente
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(arquivo):
    try:
        a = open(arquivo, 'wt+')  # O wt+ indica 'White', 'text' e 'criar'. Ou sejam escrita de texto/arquivo. O '+'
                                  # indica que se não houver nenhum arquivo, será então criado.
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {arquivo} criado com sucesso')


def lerArquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        titulo('PESSOAS CADASTRADAS')
        #print(a.read())
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arquivo, nome='Desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')  # O at é APPEND e TEXT.Comandos utilizados foram r,w,a e t(read, white, append e text)
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
