# Programa abre e lê arquivo inserido, coletando
# o valor numérico após a string especifica.
# Por fim, faz uma média da soma dos números.

# Arquivo de entrada 'mbox-short.txt'
fname = input("Enter file name: ")
fh = open(fname)

count = 0
soma = 0
string = 'X-DSPAM-Confidence: '
tam_string = len(string)


for line in fh:
    fy = line.strip()
    if fy.startswith(string):
        new_string = fy[tam_string:]
        new_float = float(new_string)
        soma += new_float
        count = count + 1

average = soma/count
print(average)
print("Done")
