# Programa que imprimi o maior número na lista

qtos_numeros = int(input('Digite quantos números a lista terá: '))

number = []
for n in range(qtos_numeros):
    numero = int(input(f"Digite o {n+1}º numero: "))
    number.append(numero)

largest_number = 0
for i in range(qtos_numeros):
    if i == 0:
        largest_number = number[i]
    else:
        if number[i] > number[i-1]:
            largest_number = number[i]

print("The largest number is: ", largest_number)
