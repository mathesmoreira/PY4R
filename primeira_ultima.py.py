# Programa lê arquivo 'teoria.cordas.txt' e imprimi
# primeira e última palavra de cada linha

arquivo = open('teoria.cordas.txt')

palavras = list()
n = 0

for linha in arquivo:
    # Separando o texto em linhas e depois em palavras
    linhas = linha.rstrip()
    linhas_lower = linhas.lower()
    palavras = linhas_lower.split()

    # Pegando a primeira e última palavra da linha atual

    tamanho_texto = len(palavras)
    primeira_palavra = palavras[0]
    ultima_palavra = palavras[tamanho_texto-1]

    print(f'{n}ª linha: Primeira palavra: {primeira_palavra}; Última palavra: {ultima_palavra}')
    n += 1
    