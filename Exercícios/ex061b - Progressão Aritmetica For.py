# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma progressão Aritmética,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

n = int(input('Digite o número para iniciar a Progressão Aritmética » '))
razao = int(input('Digite a razão para mostrar os 10 primeiros números da PA » '))

# Fórmula é o último número igualado ao primeiro + (total -1) * razão
for c in range(n, n + (11 - 1) * razao, razao):
    print(c, end=' - ')
print('Fim')
