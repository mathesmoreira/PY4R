import re
#x = "My 2 favorite numbers are 21 and 92  Josefino esta na segunda linha  Eu jah estou na terceira"
#y = re.findall('[0-9]+',x)
#print(y)

#hand = open('mbox-short.txt')
#for line in hand:
#    line = line.rstrip() #Retira as linhas vazias entre as linhas
#    if re.search("^From:.+@",line): # Acentuo circunflexo é utilizado para dar match, em nosso caso, linhas que comecam com From:
#        print(line)

#Procurando por strings com letras antes do @ e sem espaco, assim como depois deste.
#Obs.: Repare que "@2PM" nao entra na condicao
#y = "A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM"
#x = re.findall('\S+@\S+',y)
#print(x)


#Abrindo arquivo e procurando, linha por linha, caracteres que tem @
#hand = open("mbox-short.txt")
#for line in hand:
#    line = line.rstrip()
#   x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]',line)
#    if len(x)> 0:
#        print(x)



#COMBINING SEARCHING AND EXTRACTING 


#Procurando por floating-points 
#hand = open('mbox-short.txt')
#for line in hand:
#   line = line.rstrip()
#   x = re.findall('^X-.*: ([0-9.]+)',line)
#   if len(x)>0
#       print(x)


#Procurando data e hora que os e-mails foram enviados
#hand = open('mbox-short.txt')
#for line in hand:
#    line= line.rstrip()
#    x = re.findall('^From .* ([0-9][0-9]):',line)       
#    if len(x)> 0:
#        print(x)




#ESCAPE CHARACTER
#Achando o montante de dinheiro
#x = "Eu tenho R$32.12 sobrando em minha carteira"
#y = re.findall('\$[0-9.]+',x)

#print('Ele tem',y)

#Procurando por data de nascimento
#x = 'Eu nasci em 25.12.1994'
#y = re.findall('[0-9.]+',x)
#print('Sua data de nascimento é',y)


#Exercises
#1)Write a simple program to simulate the operation of the
#grep command on Unix. Ask the user to enter a regular expression and
#count the number of lines that matched the regular expression:

#i=0
#ref_expression = input('Enter a regular expression:')
#hand = open('mbox.txt')
#for line in hand:
#    line = line.strip()
#    x = re.findall(ref_expression,line)
#    if len(x) > 0:
#        i = i + 1 
#print('mbox.txt had',i)

#2)
i = 0
num = 0
numero = 0
total_num = 0
average = 0
j=0
#nome_arq = input('Digite o nome do arquivo: ')
hand = open('mbox.txt')
for line in hand:
    line = line.strip()
    num = re.findall('[0-9]+',line)
    while j < len(num):
        numero = int(num[j])
        total_num = total_num + numero
        i = i + 1
        j = j +1
avarege = (total_num/i)
print(total_num)
print(i)
