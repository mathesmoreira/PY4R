# Programa recebe um número e imprime se
# ele é, ou não, um primo

num = int(input("Digite um numero: "))
i = num - 1

# Verificando se o numero é primo
while i >= 1:
    resto = num % i
    if resto == 0 and i != 1:
        print('Não é primo')
        break
    elif i == 1:
        print('É um número primo')

    i -= 1
