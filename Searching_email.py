# Programa abre o arquivo 'mbox-short2.txt' e procura por
# endereco de emails imprimindo posteriormente a quantidade
# deles

import re


arquivo = open('mbox-short2.txt')

emails = 0

for linha in arquivo:
    # Separando o arquivo por linhas
    linha_arq = linha.rstrip()
    # Procurando linhas que contem comecem com '@'
    emails = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', linha_arq)

    # Imprimindo emails
    if len(emails) > 0:
        print(emails)
