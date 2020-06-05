# Aula de Strings

string = input('Digite algo: ')

# Len function gives us the length of a string
quant_letters = len(string)
last_letter = string[quant_letters - 1]
print('A última letra que vc digitou foi:', last_letter)

# 6.3 Travesal Exercise 1
string = input('Digite uma palavra: ')

last_index = len(string) - 1
print(last_index)

while last_index >= 0:
    letter = string[last_index]
    print(letter)
    last_index = last_index - 1

fruit = 'banana'
for letter in fruit:
    print(letter)

# Contando letras numa palavra
fruit = input('Digite uma palavra: ')
count = 0
for letter in fruit:
    if letter == 'a':
        count = count + 1

print("A palabra digitada tem", count, " As")


# 6.6 Exercise 3: Funcao para contar letrar numa string
def count(string, letra):
    string = input('Digite uma palavra: ')
    letra = input('Digite a letra que vc quer contar na palavra: ')
    count = 0
    for letter in string:
        if letter == letra:
            count = count + 1
    print('A palavra', string, 'tem', count, 'letras', letra)


# Transformando string em float
string = 'X-DSPAM-Confidence:    0.8475'
start_number = string.find(':')
new_string = string[start_number+1:]
new_string = float(new_string)
print(new_string)

count('Joselito', 'o')

# Slicing Strings
s = 'Monty Python'
print(s[0:4])
# or
print(s[:4])
# Mont
print(s[6:20])
# or
print(s[6:])
# Python

# Using IN as a logical operator
fruit = 'banana'
'a' in fruit
# True

# String Library
greet = 'Hello Bob'
# Make a copy of greet. lower(greet) change the original string
zap = greet.lower()
print(zap)

# Achar uma letra na palavra
fruit = 'banana'
pos = fruit.find('na')
print(pos)


# Procurar e trocar todos os "o"s da string por "#"
greet = 'Hello Bob'
nstr = greet.replace('o', '#')
print(nstr)


# Stripping Whitespace
greet = '   Hello Bob   '
greet.strip()
"Hello Bob"


# Prefixes
line = 'Please have a nice day'
line.startswith('Please')
# True
line.startswith('p')
# False

# Parsing and Extracting
data = input('Digite seu e-mail: ')
data = data + ' '

# Achando o domínio do e-mail
start_email = data.find('@')
end_email = data.find(' ')
domi = data[start_email + 1: end_email]
print('Seu dominio do email é:', domi)
