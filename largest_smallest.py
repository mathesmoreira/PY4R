# Programa recebe uma lista de números e retorna
# o menor e maior número desta

cont = 0
num = []

while True:
    print('When you finish write --Done--')
    number = input("Enter a number: ")
    if number == 'Done':
        break
    try:
        number = float(number)
        num.append(number)
        cont = cont + 1
    except TypeError:
        print("This is not a number!")
        continue

largest_number = num[0]
smallest_number = num[0]

for i in range(cont):
    if num[i] > largest_number:
        largest_number = num[i]
    elif num[i] < smallest_number:
        smallest_number = num[i]


print("Maximum is", largest_number)
print("Minimum is:", smallest_number)
