# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente
# de zero, o dicionário receberá também o ano de contratação e o salário. Calcule
# e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

'''
from datetime import datetime

dados = {}

dados['nome'] = str(input('Digite o seu Nome » '))
dados['nascimento'] = int(input('Digite o ano do seu nascimento » '))
dados['ctps'] = int(input('Digite o número de sua carteira de Trabalho » '))

# Importando a função datetime
dados['data'] = datetime.now().year
# Calculando a idade, subtraindo o ano de nascimento com o ano atual
dados['idade'] = dados['data'] - dados['nascimento']

if dados['ctps'] > 0:
    dados['contratação'] = int(input('Digite o ano em que foi contratado » '))
    dados['salario'] = int(input('Digite o valor do seu salário » '))

    # Calculando quantos anos de contribuição
    dados['contribuição'] = dados['data'] - dados['contratação']

    # Considerando que para aposentar precisa de 35 anos de contribuição
    dados['aposentadoria'] = 35 + dados['idade'] - dados["contribuição"]

    print()
    print(f'O colaborador {dados["nome"]} tem {dados["idade"]} anos de idade e aposentará com {dados["aposentadoria"]} anos')

else:
    print('A informação inserida está incorreta! ')
'''

from datetime import date

dados = {}

dados['Nome'] = str(input('Digite o se nome » '))
ano = int(input('Digite o ano de nascimento » '))
dados['Idade'] = date.today().year - ano
ctsp = int(input('Digite o número da Carteira de Trabalho [Digite 0 se não tiver] » '))
if ctsp == 0:
    dados['CTPS'] = 'Nulo'
else:
    dados['CTPS'] = ctsp
    dados['Contratação'] = int(input('Digite o ano de Contratação » '))
    dados['Salário'] = float(input('Digite o valor do salário » '))
    dados['Aposentadoria'] = (dados['Contratação'] + 35) - ano
# Para calcular a aposentadoria, levarei em consideração 35 anos de contribuição. Para isto, eu pego o ano de
# contratação somado com 35 e subtraindo pelo ano de nascimento

print()
print('-_'*30)
for k, v in dados.items():
    print(f'O {k} tem o valor {v}')
print('_-'*30)
