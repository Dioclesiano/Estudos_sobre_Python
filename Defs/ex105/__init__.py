def notas(nomes, notas, situacao=False):
    boletim = {}

    boletim['Nomes'] = nomes
    boletim['Notas'] = notas
    mediaAluno = []  # Média de Cada Aluno
    menorNota = []  # Menor Nota de cada Aluno
    maiorNota = []  # Maior Nota de cada Aluno

    for k, v in enumerate(notas):
        menor = maior = 0
        for c in range(0, 4):
            if c == 0:
                menor = maior = v[c]
            else:
                if v[c] < menor:
                    menor = v[c]
                if v[c] > maior:
                    maior = v[c]
        menorNota.append(menor)
        maiorNota.append(maior)
    boletim['Menor Nota'] = menorNota
    boletim['Maior Nota'] = maiorNota


    cadastros = len(boletim['Nomes'])
    mediaTotal = 0  # Armazena a média total da turma
    somaTotal = 0  # 2 - Armazena a soma todas as notas
    for i, j in enumerate(boletim['Notas']):
        somar = 0  # 1 - Armazena o resultado da soma das notas de cada aluno
        for k, v in enumerate(j):
            somar += v  # 1 - Soma a nota de cada aluno
            somaTotal += v  # 2 - Soma todas as notas

        media = somar / 4
        mediaTotal = somaTotal / cadastros
        mediaAluno.append(media)

    boletim['Média do Aluno'] = mediaAluno  # Média de notas de cada aluno

    if situacao:
        resultado = []
        for k, v in enumerate(mediaAluno):
            if boletim["Média do Aluno"][k] < 5:
                resultado.append(f'{boletim["Nomes"][k]} >>> REPROVADO <<<')
            elif boletim['Média do Aluno'][k] <= 7:
                resultado.append(f'{boletim["Nomes"][k]} >>> RECUPERAÇÃO <<<')
            else:
                resultado.append(f'{boletim["Nomes"][k]} >>> APROVADO <<<')
        boletim['Situação'] = resultado

    boletim['Média da Turma'] = mediaTotal  # Média de notas da turma

    print(boletim)
