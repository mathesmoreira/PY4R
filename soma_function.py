# Funcao 'soma'

def Soma(a, b):
    res = a + b
    return res


x = int(input("Digite o primeiro numero: "))
y = int(input("Digite o segundo numero: "))

print(f"A soma dos dois valores é igual a {Soma(x, y)}")
