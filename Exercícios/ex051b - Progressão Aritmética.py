primeiro = int(input('Digite o primeiro termo para iniciar a progressão aritmética » '))
razao = int(input('Digite o intervalo de salto » '))
decimo = primeiro + (10 - 1) * razao  # Fórmula matemática que identifica um número da PA

for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' b» ')
