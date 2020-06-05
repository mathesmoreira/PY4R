# Programa verifica, no intervalo de 1 a 100, se o
# número é maior ou menor que 50


numero = input("Digite um numero de 1 a 100: ")

# Verificando se o usuario digitou um numero
try:
    num = int(numero)
except:
    num = 'nnum'

# Descobrindo em qual intervalo se encontra o numero
if num == 50:
    print("O numero digitado é igual a 50!")
elif num == 'nnum':
    print("Voce NAO digitou um numero!")
elif num < 1:
    print("O numero digitado NAO esta no intervalo solicitado!")
elif num > 100:
    print("O numero digitado NAO esta no intervalo solicitado!")
elif num < 50:
    print("O numero digitado é menor que 50!")
else:
    print("O numero digitado é maior que 50!")
