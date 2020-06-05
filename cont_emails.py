# Contando emails enviados por uma pessoa
# em um arquivo txt e printando a pessoa que enviou
# mais msgs

arquivo = open('mbox-short2.txt')

linha_vetor = list()
nome = list()
email = dict()
maior_nome = None
maior_numero = None


for linha in arquivo:
    linha_limpa = linha.strip()
    if linha_limpa.startswith('From '):
        linha_vetor = linha.split()
        nome = linha_vetor[1]
        email[nome] = email.get(nome, 0) + 1


for nome, numero in email.items():
    if maior_nome is None or numero > maior_numero:
        maior_nome = nome
        maior_numero = numero

print(maior_nome, maior_numero)
