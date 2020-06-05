# Funcao que soma dois numeros

def soma(x, y):
    z = x + y
    return z


print('Para realizar a soma digite dois numeros!')
x = int(input('Digite o primeiro numero: '))
y = int(input('Digite o segundo numero: '))

print('O resultado da soma é: ', soma(x, y))
