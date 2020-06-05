# Programa que lê as strings dentro do arquivo 'romeo.txt'
# e informa quantas vezes a palavra aparece neste

fh = open('romeo.txt')

final = {}
count = 1

for line in fh:
    lines = line.strip()
    words = lines.split()
    for word in words:
        if word not in final:
            final[word] = 1
        else:
            final[word] = final[word] + 1

print(final)
