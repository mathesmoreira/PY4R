# Programa recebe um valor número e informa se é impar ou par

x = int(input('Digite um numero: '))

resto = x % 2

if resto == 0:
    print("Esse numero é par!")
else:
    print("Esse numero é impar!")
